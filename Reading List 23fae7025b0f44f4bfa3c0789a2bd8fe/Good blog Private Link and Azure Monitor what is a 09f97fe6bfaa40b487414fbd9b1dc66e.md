# Good blog Private Link and Azure Monitor: what is an AMPLS? – Cloudtrooper

Column: https://blog.cloudtrooper.net/2022/03/11/private-link-and-azure-monitor-what-is-an-ampls/
Processed: No
created on: March 21, 2022 7:00 PM
topics: azure, tech-stuff

Today I came across a concept while not being too new in Azure, I had not met before: Private Link Scopes. This is something that specific services do, more concretely Azure Arc and Azure Monitor (see [here](https://docs.microsoft.com/azure/azure-monitor/logs/private-link-configure) for the official docs on how to configure this for Azure Monitor). In the case of the latter, the full legal name is “Azure Monitor Private Link Scope”, or AMPLS for friends. But what is it actually?

### What was Private Link again?

Let’s recap: a Private Link is a unidirectional connection between two resources in different VNets. Unidirectional means that there is a “client side” (called Private Endpoint) and a “server side” (called Private Link Service). However, for Microsoft-managed services, the “server side” is not visible by the user, and you only see the Private Endpoint in your Virtual Network as a representation of the service (Azure SQL in this example) with a private IP address in your VNet range:

![](Good%20blog%20Private%20Link%20and%20Azure%20Monitor%20what%20is%20a%2009f97fe6bfaa40b487414fbd9b1dc66e/image.png)

Private Link to an Azure service

You might be wondering what is that green pipe between the VM and Azure SQL? Well, in the previous paragraph I described how the private endpoint (and its associated NIC) is a “representation” of the service, but the actual traffic flows straight from the Virtual Machine to the destination service encapsulated in IPv6. Why am I telling you this? More to this later.

### So what is a Private Link Scope?

Certain services (today Azure Monitor and Arc) do not support the architecture above. For example, in Azure Monitor you cannot just create a Private Endpoint directly connected with a Log Analytics Workspace. Instead, you use something in between: the Private Link Scope:

![](Good%20blog%20Private%20Link%20and%20Azure%20Monitor%20what%20is%20a%2009f97fe6bfaa40b487414fbd9b1dc66e/image-1.png)

Azure Monitor Private Link architecture

This Azure Monitor Private Link Scope will be associated on one side to the Private Endpoint, and on the other to certain Log Analytics and Application Insight workspaces.

From the perspective of the Virtual Machines in the VNets, nothing changes: they talk to the private IP address of the private endpoint, and traffic is magically sent using private IP addresses to the destination Log Analytics workspace.

### Reminder: Why is DNS so important?

You don’t want to have to touch anything inside the Virtual Machine so that it talks to the private endpoint, otherwise it would be very difficult to manage Private Link in environments with hundreds or thousands of VMs.

How to do it then? Easy, you don’t change the name of the service the VMs are trying to access, but the IP address it resolves to. In our previous example with the database, if the VM is talking to the server `myserver.database.windows.net`, you need to make it resolve it to the private IP instead of the public IP, and then everything works magically.

There is one more little trick: you could just override all `*.database.windows.net` names, but then you would potentially break services that have no private link configured. Hence, Private Link introduces an indirection: all services with a private link configured will first resolve to an alias (in DNS jargon a CNAME), so you only need to override the alias zone. For example, again with the SQL example, if your database server is at `myserver.database.windows.net`, Azure DNS will redirect to `myserver.privatelink.database.windows.net` after you configure Private Link, so you only need to override this one with a zone for `.privatelink.database.windows.net` records.

Don’t worry if this doesn’t make too much sense at the beginning. If you want to dive deeper, you might want to look at [this great post by Matt Felton](https://journeyofthegeek.com/2020/03/06/azure-private-link-and-dns-part-2/). In this post I will move forward with Azure Monitor.

### Let’s get our hands dirty

Of course, I built a lab to test how all this works (no blog post without code!). If you want to try yourself you can see the script here: [https://github.com/erjosito/azcli/blob/master/ampls.azcli](https://github.com/erjosito/azcli/blob/master/ampls.azcli). It is a hub and spoke architecture with the spokes using a DNS server in the hub, and a single Private Endpoint deployed in the hub VNet.

![](Good%20blog%20Private%20Link%20and%20Azure%20Monitor%20what%20is%20a%2009f97fe6bfaa40b487414fbd9b1dc66e/image-2.png)

Test bed with a hub and spoke VNet design

Before configuring Private Link, Azure Monitor would see the logs from the VMs coming from their public IP addresses (the second column in the following output), showing that the traffic is still going over the public Internet:

```
$ query='Heartbeat
| where TimeGenerated > ago(15m)
| extend PrivateIP = tostring(ComputerPrivateIPs[0])
| summarize count() by Computer, ComputerIP, PrivateIP'
$ az monitor log-analytics query -w $logws_customerid --analytics-query $query -o tsv
spoke3  52.143.1.180    192.168.3.4     PrimaryResult   14
spoke4  51.138.43.73    192.168.4.4     PrimaryResult   14
spoke2  52.143.0.191    192.168.2.4     PrimaryResult   14
hub     52.143.1.26     192.168.0.4     PrimaryResult   15
spoke1  52.143.0.42     192.168.1.4     PrimaryResult   14

```

By the way, I built my lab with four spokes, even if the diagram above only shows two, but that shouldn’t bother you. What might be jumping to your eye is that there are multiple private DNS zones. In the drawing I put three, but it is actually five. When you create a Private Endpoint for Azure Monitor (remember that the Private Endpoint will be linked to the AMPLS, not to Azure Monitor itself), in the Virtual Network step of the creation wizard it will offer to create the five private zones that are required for the setup to work:

![](Good%20blog%20Private%20Link%20and%20Azure%20Monitor%20what%20is%20a%2009f97fe6bfaa40b487414fbd9b1dc66e/image-3.png)

Creating a Private Link for Azure Monitor

You can create the zones with the wizard or manually, as I do in the script. If you are automating this with Azure CLI like me, or with any other technology like Terraform, ARM, bicep or PowerShell, you want to keep reading.

### Thank you zone groups!

After creating the private DNS zones, you need to create the DNS records in those zones. Azure SQL or Azure Storage are easy, you only need to create one A record to make it work. How many do we need with Azure Monitor? Let’s find out.

The best way to add the A records is being lazy and letting Azure do it for you, associating your private endpoint (which knows its private IP address) with the zone(s). The mechanism to do that is called “Zone Groups”, which “connects” one private endpoint to a group of multiple zones. For example, in my GitHub script, first I create the zone group with the first zone, and then I add the remaining four to the zone group:

```
zone=privatelink.agentsvc.azure-automation.net
zone_dash=$(echo $zone | tr '.' '-')
az network private-endpoint dns-zone-group create --endpoint-name ampls -g $rg -n default --zone-name $zone_dash --private-dns-zone $zone -o none
for zone in privatelink.blob.core.windows.net privatelink.monitor.azure.com privatelink.ods.opinsights.azure.com privatelink.oms.opinsights.azure.com
do
    zone_dash=$(echo $zone | tr '.' '-')
    az network private-endpoint dns-zone-group add --endpoint-name ampls -g $rg -n default --zone-name $zone_dash --private-dns-zone $zone -o none
done

```

Other that the strange `zone-dash` variable (which is a name for the zone assignment, where I replace the dots by dashes since the dot is a forbidden character for the name), it is pretty straight forward: you just connect the private endpoint to the private zones. How many A records have been created? Let’s find out:

```
$ for zone in privatelink.agentsvc.azure-automation.net privatelink.blob.core.windows.net privatelink.monitor.azure.com privatelink.ods.opinsights.azure.com privatelink.oms.opinsights.azure.com
do
    az network private-dns record-set a list -z $zone -g $rg --query '[].[aRecords[0].ipv4Address, fqdn]' -o tsv
done

192.168.0.70    36b87820-3c7e-41fe-851a-86d2a26e7cc2.privatelink.agentsvc.azure-automation.net.
192.168.0.77    scadvisorcontentpl.privatelink.blob.core.windows.net.
192.168.0.72    global.in.ai.privatelink.monitor.azure.com.
192.168.0.71    api.privatelink.monitor.azure.com.
192.168.0.78    global.handler.control.privatelink.monitor.azure.com.
192.168.0.75    diagservices-query.privatelink.monitor.azure.com.
192.168.0.74    live.privatelink.monitor.azure.com.
192.168.0.73    profiler.privatelink.monitor.azure.com.
192.168.0.76    snapshot.privatelink.monitor.azure.com.
192.168.0.69    36b87820-3c7e-41fe-851a-86d2a26e7cc2.privatelink.ods.opinsights.azure.com.
192.168.0.68    36b87820-3c7e-41fe-851a-86d2a26e7cc2.privatelink.oms.opinsights.azure.com.

```

Wow, not bad, it almost filled my /26 subnet. Good that we didn’t have to find out all those endpoints: Thanks zone groups!

### Those IPv6 addresses were not invited to the party!

Alright, so we have our DNS in place for all the Fully Qualified Domain Names that the VMs need to send logs to a Log Analytics workspace. Feel free to check out the script in [https://github.com/erjosito/azcli/blob/master/ampls.azcli](https://github.com/erjosito/azcli/blob/master/ampls.azcli) for more details on how to create the AMPLS itself, deploy the `dnsmasq` server in the hub or other minutiae. After a while, we can run our query on the Log Analytics workspace to check the source IPs of the messages:

```
$ query='Heartbeat
| where TimeGenerated > ago(5m)
| extend PrivateIP = tostring(ComputerPrivateIPs[0])
| summarize count() by Computer, ComputerIP, PrivateIP'
$ az monitor log-analytics query -w $logws_customerid --analytics-query $query -o tsv

hub     fd40:1085:12:6d79:7712:100:c0a8:4       192.168.0.4     PrimaryResult   5
spoke4  fd40:1085:12:6c07:7412:100:c0a8:404     192.168.4.4     PrimaryResult   5
spoke1  fd40:1085:12:b979:7712:100:c0a8:104     192.168.1.4     PrimaryResult   5
spoke3  fd40:1085:12:c879:7712:100:c0a8:304     192.168.3.4     PrimaryResult   5
spoke2  fd40:1085:12:b879:7712:100:c0a8:204     192.168.2.4     PrimaryResult   5

```

Alright, the public IP addresses are gone, but why do we see IPv6 addresses in their place? I am not too sure, but my educated guess is that those IPv6 are the endpoints of the actual tunnels that transports the traffic from the VM to Azure Monitor, and are not in your VNet address space (I didn’t even configure IPv6 in my VNets).

### Adding up

So what have I learnt?

- Azure Monitor Private Link Scopes sit between the Private Endpoint and Azure Monitor
- The DNS names required for Azure Monitor Private Link are a few, so you want to use zone groups to create the A records automatically
- The private IP addresses of the VMs do not appear in the `ComputerIP` field of the heartbeat messages in Log analytics, but a meaningless IPv6 address shows up there. Kind of important if your queries look at that specific field

I hope you learnt something too!