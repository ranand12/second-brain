# Azure Firewall’s sidekick to join the BGP superheroes – Cloudtrooper

Column: https://blog.cloudtrooper.net/2022/05/02/azure-firewalls-sidekick-to-join-the-bgp-superheroes/
Processed: No
created on: May 3, 2022 4:51 PM
topics: azure

[Azure Firewall](https://docs.microsoft.com/azure/firewall/overview) is a fantastic product: oversimplifying, an architecture that scales out great, provides traffic forwarding and security in Azure, and is very easy to integrate in a network. Some times you need to manipulate the default routing of Azure VNets, and [Azure Route Server](https://docs.microsoft.com/azure/route-server/overview) offers an invaluable tool for that. However, Azure Route Server requires BGP to interact with it, which Azure Firewall does not support. At first sight it looks like an oil-and-water problem: they don’t mix well.

In this post I will explore a simple technique that can be used to leverage the simplicity and scalability of Azure Firewall with the power of Azure Route Server. As usual, the full code for this test is in my Github repository [here](https://github.com/erjosito/azcli/blob/master/routeserver-vmss-selfcontained.azcli).

## What’s the problem?

To illustrate it, I will use the following example: I recently had a discussion about one of the designs documented in the Azure Route Server page on [how to route traffic between on-premises networks and AVS](https://docs.microsoft.com/azure/route-server/vmware-solution-default-route). The question is whether it would be possible at all using Azure Firewall instead of a 3rd-party Network Virtual Appliance (NVA). Essentially, the documented design consists of an NVA injecting a prefix via BGP that will be advertised to both on-premises and AVS, but how to do this with an Azure Firewall, if it does not support BGP?

![](Azure%20Firewall%E2%80%99s%20sidekick%20to%20join%20the%20BGP%20superher%20ebaa82ecfe1b4a4a95e8e9744a8b480e/image.png)

Design to hairpin traffic between AVS and onprem to an NVA

One very important feature of Azure Route Server, which was recently added, is that it honors the next-hop that BGP peers set in their route advertisements (before this feature, Route Server used to hard code the next hop to the BGP peer’s IP address).

With this information, we come to the basic idea behind this post: you could have a cheap set of VMs (what I call “Route Generator” in the diagram below) whose only job is advertising routes to Azure Route Server, where Azure Firewall is the next hop:

![](Azure%20Firewall%E2%80%99s%20sidekick%20to%20join%20the%20BGP%20superher%20ebaa82ecfe1b4a4a95e8e9744a8b480e/image-1.png)

“Route Generator” VMs announce routes with the Azure Firewall as next hop

Note that these VMs would be quite cheap, since they do not need to transport any traffic. For example, in my test I am using B1s instances, at $8.25 per month in North Europe (and even much cheaper with [Reservations](https://docs.microsoft.com/azure/cost-management-billing/reservations/save-compute-costs-reservations)). And as far as resource utilization goes, these small VMs do not seem to be challenged at all:

![](Azure%20Firewall%E2%80%99s%20sidekick%20to%20join%20the%20BGP%20superher%20ebaa82ecfe1b4a4a95e8e9744a8b480e/image-3.png)

Resource utilization for Route Generator VMs

In case you are wondering, the CPU peaks are due to a self-configuration script that runs every 5 minutes (read further for more details on this), and even these peaks are consistently below 10%. Secondly, that event that happened at around 11:15am in the charts is a self-repair event that I tested as explained further below.

## How resilient is this?

That is the big question, isn’t it? This “route generator” needs to be up all the time, otherwise if the routes disappeared from Azure Route Server, connectivity would be impaired. Some thoughts about the solution I tested:

- The Route Generator should be at least two VMs. Ideally three, distributed across Availability Zones (if your Azure region has them). For this purpose I use a **Virtual Machine Scale Set** with three instances to deploy the solution.
- The VMSS should heal itself, in case one of the instances had an issue. Luckily VMSS has this feature integrated, called [VMSS Automatic Instance Repairs](https://docs.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-automatic-instance-repairs).
- VMSS automatic instance repairing needs a way to verify that the instance is healthy. We could just use the BGP TCP port, and assume that if BGP is up our route generator is running. However, we can go further, and configure an intelligent probe that will only be successful if the BGP adjacencies to both Azure Route Server instances are established. This is what [this small Flask application](https://github.com/erjosito/azcli/blob/master/routeserver-vmss-selfcontained-healthcheck.py) does.
- To check the health of the application, calling that small HTTP healthcheck endpoint in the VM, you can use either Azure Load Balancer health probes or the Azure [Application Health Extension](https://docs.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-health-extension). I went for the latter, because you don’t need any external component, only installing a small agent in the VM (which you can do over the VMSS API)
- The instances should self-configure: if the VMSS engine decides to bring up a new VMSS instance, it should add the new BGP peering to the Azure Route Server, and possibly delete the old one. While this is possible using Azure automation constructs such as Logic Apps and Azure Automation (see my previous blog [Azure Route Server and NVAs on scale sets](https://blog.cloudtrooper.net/2021/05/31/azure-route-server-and-nvas-running-on-scale-sets/)), in this case I went for a more self-contained solution, where each instance itself can reconfigure the Azure Route Server. This is our final piece of the puzzle, the [self-configuration script](https://github.com/erjosito/azcli/blob/master/routeserver-vmss-selfcontained-config.sh).

## Does this work?

Let’s have a look! I have deployed my Route Generator with just one instance (so no high availability yet). After the VM is created, the self-configuration script has automatically configured the Azure Route Server to talk to it (in this case the peering is still being created, as indicated by the provisioning state `Updating`):

```
❯ az network routeserver peering list --routeserver rs -g $rg -o table

Name    PeerAsn    PeerIp    ProvisioningState    ResourceGroup
------  ---------  --------  -------------------  ---------------
nva_1   65001      10.1.2.5  Updating             rsvmss

```

Azure Route Server is receiving a route that we defined for our Route Generator to advertise (10.0.0.0/8), where the next hop is `10.1.3.4`, the IP address of our Azure Firewall:

```
 az network routeserver peering list-learned-routes -n nva_1 --routeserver rs -g $rg --query 'RouteServiceRole_IN_0' -o tsv
65001   10.1.1.4        10.0.0.0/8      10.1.3.4        EBgp    10.1.2.5        32768

```

If we have a look at the effective routes of a Virtual Machine in the ARS’ VNet, it will see this route pointing to 10.1.3.4:

```
❯ az network nic show-effective-route-table -n azurevmVMNic -g $rg -o table

Source                 State    Address Prefix     Next Hop Type          Next Hop IP
---------------------  -------  -----------------  ---------------------  -------------
Default                Active   10.1.0.0/16        VnetLocal
VirtualNetworkGateway  Active   10.0.0.0/8         VirtualNetworkGateway  10.1.3.4
Default                Active   0.0.0.0/0          Internet
User                   Active   93.104.185.129/32  Internet
Default                Active   100.64.0.0/10      None
[...]

```

Let’s now scale out our route generator to three instances, spread over Availability Zones. I will use this command:

```
az vmss scale -n $nva_name -g $rg --new-capacity 3 -o none

```

Now we should see two additional BGP peerings popping up in our Azure Route Server configuration, and Azure Route Server is getting the 10.0.0.0/8 route from each of them:

```
❯ az network routeserver peering list --routeserver rs -g $rg -o table

Name    PeerAsn    PeerIp    ProvisioningState    ResourceGroup
------  ---------  --------  -------------------  ---------------
nva_1   65001      10.1.2.5  Succeeded            rsvmss
nva_3   65001      10.1.2.6  Succeeded            rsvmss
nva_4   65001      10.1.2.7  Failed               rsvmss

```

As you can see, one of the neighbors failed to provision. This is due to the fact that Azure Route Server does not particularly enjoy concurrent write operations to its API. But this is where the self-healing of this setup kicks in. We just need to sit, relax, and wait for a bit. After a while, if we run the command again, the adjacency is now healthy (`Succeeded`):

```
❯ az network routeserver peering list --routeserver rs -g $rg -o table

Name    PeerAsn    PeerIp    ProvisioningState    ResourceGroup
------  ---------  --------  -------------------  ---------------
nva_1   65001      10.1.2.5  Succeeded            rsvmss
nva_3   65001      10.1.2.6  Succeeded            rsvmss
nva_4   65001      10.1.2.7  Succeeded            rsvmss

```

What happened? If we look at the log of the self-configuration utility (in `/root/routeserver.log`), it gives us a hint:

```
root@nva0bab06000004:~# more routeserver.log
2022-05-02T07:47:27+00:00 Starting configuration process...
2022-05-02T07:47:31+00:00 Logged into subscription ID e7da9914-9b05-4891-893c-546cb7b0422e
2022-05-02T07:47:33+00:00 Deleting existing peer null with IP 10.1.2.7 and ASN null, does not match nva_4 and 65001...
2022-05-02T07:47:34+00:00 Configuring ARS rs in RG rsvmss to peer to nva_4 on IP address 10.1.2.7 and ASN 65001...
2022-05-02T07:47:46+00:00 0 routes downloaded from https://raw.githubusercontent.com/erjosito/azcli/master/routeserver-vmss-selfcontained-routes.txt, adding now to BIRD configuration...
2022-05-02T07:47:46+00:00 Adding route for 10.0.0.0/8 to BIRD configuration...
2022-05-02T07:47:48+00:00 Seeing if RS peer 10.1.2.5 can be deleted...
2022-05-02T07:47:48+00:00 Seeing if RS peer 10.1.2.6 can be deleted...
2022-05-02T07:47:48+00:00 Seeing if RS peer 10.1.2.7 can be deleted...
2022-05-02T07:50:01+00:00 Starting configuration process...
2022-05-02T07:50:04+00:00 Logged into subscription ID e7da9914-9b05-4891-893c-546cb7b0422e
2022-05-02T07:50:06+00:00 Peer nva_4 already found in ARS rs with state Failed, deleting and recreating...
```

Let’s now verify that the route server is getting the routes from all BGP peers:

```
❯ az network routeserver peering list --routeserver rs -g $rg -o table
Name    PeerAsn    PeerIp    ProvisioningState    ResourceGroup
------  ---------  --------  -------------------  ---------------
nva_1   65001      10.1.2.5  Succeeded            rsvmss
nva_3   65001      10.1.2.6  Succeeded            rsvmss
nva_4   65001      10.1.2.7  Succeeded            rsvmss
❯
❯ az network routeserver peering list-learned-routes -nnva_1 --routeserver rs -g $rg --query 'RouteServiceRole_IN_0' -o tsv
65001   10.1.1.4        10.0.0.0/8      10.1.3.4        EBgp    10.1.2.5        32768
❯ az network routeserver peering list-learned-routes -nnva_3 --routeserver rs -g $rg --query 'RouteServiceRole_IN_0' -o tsv
65001   10.1.1.4        10.0.0.0/8      10.1.3.4        EBgp    10.1.2.6        32768
❯ az network routeserver peering list-learned-routes -nnva_4 --routeserver rs -g $rg --query 'RouteServiceRole_IN_0' -o tsv
65001   10.1.1.4        10.0.0.0/8      10.1.3.4        EBgp    10.1.2.7        32768

```

You can see that the prefix is always the same (`10.0.0.0/8`), the next-hop is always the same (the Azure Firewall’s IP, `10.1.3.4`), but the advertising IP depends on the VMSS instance (`10.1.2.5`, `10.1.2.6`, `10.1.2.7`).

## Automatic instance repair in action

We can get into one of the instances, and see the Application Health Extension working. The health check logic is listening on port 8080, using the path `/api/healthcheck`:

```
jose@nva0bab06000001:~$ curl http://localhost:8080/api/healthcheck
{
  "health": "OK",
  "rs0_status": "Established",
  "rs1_status": "Established"
}

```

You can see in the `/var/log/syslog` that the Application Health Extension is probing our health check every 30 seconds (after the initial ones):

```
ose@nva0bab06000001:~$ tail -f /var/log/syslog
May  2 07:45:56 nva0bab06000001 systemd[9402]: Listening on GnuPG network certificate management daemon.
May  2 07:45:56 nva0bab06000001 systemd[9402]: Listening on D-Bus User Message Bus Socket.
May  2 07:45:56 nva0bab06000001 systemd[9402]: Reached target Sockets.
May  2 07:45:56 nva0bab06000001 systemd[9402]: Reached target Basic System.
May  2 07:45:56 nva0bab06000001 systemd[1]: Started User Manager for UID 1000.
May  2 07:45:56 nva0bab06000001 systemd[9402]: Reached target Default.
May  2 07:45:56 nva0bab06000001 systemd[9402]: Startup finished in 100ms.
May  2 07:46:17 nva0bab06000001 cloud-init[1600]: 127.0.0.1 - - [02/May/2022 07:46:17] "GET /api/healthcheck HTTP/1.1" 200 -
May  2 07:46:21 nva0bab06000001 cloud-init[1600]: 127.0.0.1 - - [02/May/2022 07:46:21] "GET /api/healthcheck HTTP/1.1" 200 -
May  2 07:46:47 nva0bab06000001 cloud-init[1600]: 127.0.0.1 - - [02/May/2022 07:46:47] "GET /api/healthcheck HTTP/1.1" 200 -
May  2 07:47:17 nva0bab06000001 cloud-init[1600]: 127.0.0.1 - - [02/May/2022 07:47:17] "GET /api/healthcheck HTTP/1.1" 200 -

```

After the grace period for Automatic Instance Repairs expires (30 minutes per default, after each change to the VMSS it is the time it takes for automatic repairs to start working). We can now break one of them. For example, I will delete the BGP peering adjacency from the Azure Route Server to the first instance `nva_1`:

```
az network routeserver peering delete --routeserver rs -g $rg -n nva_1 -y

```

This will trigger healthcheck failures, that can be seen in `/var/log/syslog`:

```
May  2 08:28:17 nva0bab06000001 cloud-init[1600]: 127.0.0.1 - - [02/May/2022 08:28:17] "GET /api/healthcheck HTTP/1.1" 200 -                                                                                                                May  2 08:28:18 nva0bab06000001 bird: rs0: Received: Administrative shutdown                                                                                                                                                                May  2 08:28:18 nva0bab06000001 bird: Next hop address 10.1.1.5 resolvable through recursive route for 10.1.0.0/16                                                                                                                          May  2 08:28:18 nva0bab06000001 bird: rs1: Received: Administrative shutdown                                                                                                                                                                May  2 08:28:47 nva0bab06000001 cloud-init[1600]: 127.0.0.1 - - [02/May/2022 08:28:47] "GET /api/healthcheck HTTP/1.1" 503 -
May  2 08:29:17 nva0bab06000001 cloud-init[1600]: 127.0.0.1 - - [02/May/2022 08:29:17] "GET /api/healthcheck HTTP/1.1" 503 -
May  2 08:29:47 nva0bab06000001 cloud-init[1600]: 127.0.0.1 - - [02/May/2022 08:29:47] "GET /api/healthcheck HTTP/1.1" 503 -

```

The Application Health Extension will declare the instance as unhealthy, and the VMSS will start creating a new one:

```
❯ az vmss list-instances -n $nva_name -g $rg -o table
InstanceId    LatestModelApplied    Location    ModelDefinitionApplied    Name    ProvisioningState    ResourceGroup    VmId
------------  --------------------  ----------  ------------------------  ------  -------------------  ---------------  ------------------------------------
1             True                  westeurope  VirtualMachineScaleSet    nva_1   Succeeded            rsvmss           d6eb7753-6972-4219-aea4-d1fb3ddc143b
3             True                  westeurope  VirtualMachineScaleSet    nva_3   Succeeded            rsvmss           f018c3ed-9700-43ae-9723-75e837480ae1
4             True                  westeurope  VirtualMachineScaleSet    nva_4   Succeeded            rsvmss           84c82d4a-637a-4682-ae70-1afe914f465d
5             True                  westeurope  VirtualMachineScaleSet    nva_5   Creating             rsvmss           a249da25-ea41-4122-ac75-f980b85fe887
```

When the new instance is up and running, the unhealthy one will be retired:

```
❯ az vmss list-instances -n $nva_name -g $rg -o table
InstanceId    LatestModelApplied    Location    ModelDefinitionApplied    Name    ProvisioningState    ResourceGroup    VmId
------------  --------------------  ----------  ------------------------  ------  -------------------  ---------------  ------------------------------------
3             True                  westeurope  VirtualMachineScaleSet    nva_3   Succeeded            rsvmss           f018c3ed-9700-43ae-9723-75e837480ae1
4             True                  westeurope  VirtualMachineScaleSet    nva_4   Succeeded            rsvmss           84c82d4a-637a-4682-ae70-1afe914f465d
5             True                  westeurope  VirtualMachineScaleSet    nva_5   Succeeded            rsvmss           a249da25-ea41-4122-ac75-f980b85fe887

```

The self-configuration script running on the VMSS instances will take care of creating the new BGP peering in the Azure Route Server, and even cleaning up the old one if they need to (in this particular case they don’t need to, because that how we introduced the failure):

```
❯ az network routeserver peering list --routeserver rs -g $rg -o table

Name    PeerAsn    PeerIp    ProvisioningState    ResourceGroup
------  ---------  --------  -------------------  ---------------
nva_3   65001      10.1.2.6  Succeeded            rsvmss
nva_4   65001      10.1.2.7  Succeeded            rsvmss
nva_1   65001      10.1.2.5  Deleting             rsvmss
nva_5   65001      10.1.2.4  Succeeded            rsvmss

```

## Operationalizing this

If you want to put this in production, there are a couple of things you would probably need to consider:

- In order to speed up the creation time of new instances, you probably want to create custom images with the required software dependencies pre-installed (mostly Azure CLI, that is the bit taking most time). [Azure Image Builder](https://docs.microsoft.com/azure/virtual-machines/image-builder-overview) is one thing you want to look at
- The current self-configuration script tries to locate an Azure Route Server in the same resource group as the VMSS. However, you probably want to pass the ARM ID of an Azure Route Server, to support more flexible designs where the VMSS and the ARS are in different resource groups.
- Similarly, the instances have a couple of variables hard-coded, such as the IP of the next hop (the Azure Firewall in this case), or the Autonomous System number (`65001` in the outputs above). You probably want to make this customizable.
- One way to do this is how I inject the routes, which is by changing [a file in a Github repo](https://github.com/erjosito/azcli/blob/master/routeserver-vmss-selfcontained-routes.txt) that the self-configuration script reads every 5 minutes, so that you don’t need to redeploy the whole thing every time you want to change the advertised routes. Other possibilities include passing variables to the VMSS instances from an Azure Key Vault, for example.
- Something else you probably would want to do is integrating the VMSS instances with Azure Monitor and Log Analytics, to get the logs and more visibility on what is going on.

## What did we learn?

Even if Azure Firewall does not speak BGP, you can use an Azure VMSS to advertise prefixes via BGP to Azure Route Server, with the Azure Firewall next hop. This provides an easy, cost-effective and scalable way to do traffic engineering with Azure Firewall, since the VMSS is not in the data plane.

What do you think? Thanks for reading!

### *Related*