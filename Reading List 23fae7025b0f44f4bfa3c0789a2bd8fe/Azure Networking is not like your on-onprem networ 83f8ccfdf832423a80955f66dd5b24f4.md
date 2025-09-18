# Azure Networking is not like your on-onprem network – Cloudtrooper

Column: https://blog.cloudtrooper.net/2023/01/21/azure-networking-is-not-like-your-on-onprem-network/
Processed: No
created on: January 26, 2023 5:35 PM
topics: azure, tech-stuff

I often get asked about the differences between Azure Networking and a traditional, on-premises network. I have been hit with a flu the last few days, so I had some time to think about this, and I decided to start writing whatever thoughts were not actually the result of the fever. In this post I will focus on main difference: routing is performed in the NICs. Additionally I will comment on other more subtle ones, such as the fact that Azure does not perform recursive routing lookups, how ARP is not needed and the lack of endpoint data plane learning.

## Azure NICs are actually routers

The most frequent routing problem I see in designs involving 3rd-party appliances such as SD-WAN devices and firewalls is failing at considering Azure NICs routing.

If you want to know more about how those NICs actually work you can start with the posts of [Toni Pasanen](https://www.linkedin.com/in/toni-pasanen-a303a16), such as [this one](https://nwktimes.blogspot.com/2023/01/azure-SDN-vNIC-Architecture.html). TL;DR: Azure NICs can do 3 networking functions: routing, traffic filtering and Network Address Translation.

I have already discussed about this in the past. This picture might look familiar as a representation of a VNet, if you have read [this post](https://blog.cloudtrooper.net/2022/02/06/azure-route-server-to-encap-or-not-to-encap-that-is-the-question/):

![](Azure%20Networking%20is%20not%20like%20your%20on-onprem%20networ%2083f8ccfdf832423a80955f66dd5b24f4/image-1.png)

Essentially, you shouldn’t look at a VNet as a massive virtual router where your VMs are somehow connected to, but instead as a full mesh of small micro-routers, one per VM. There are two routers between every two virtual machines in Azure, living in each VM’s NIC. Of these two routers, the crucial one is the NIC in the source VM, which needs to know where to send the traffic. In other words, when a VM1 sends a packet to a VM2, from a routing perspective this is what happens:

![](Azure%20Networking%20is%20not%20like%20your%20on-onprem%20networ%2083f8ccfdf832423a80955f66dd5b24f4/image-2.png)

In VM-to-VM communications these details are normally not important, but if we are talking about Network Virtual Appliances it is critical understanding this. For example, imagine a firewall NVA that receives a packet from an Azure VM addressed to a system available in a remote branch, connected to Azure through an SD-WAN appliance. The following picture illustrates this topology for the egress (Azure to on-prem) and ingress (on-prem to Azure):

![](Azure%20Networking%20is%20not%20like%20your%20on-onprem%20networ%2083f8ccfdf832423a80955f66dd5b24f4/image-3.png)

As you can see, there are 3 NICs involved in this communication, that need to have proper routing:

- The VM NIC typically has a 0.0.0.0/0 route pointing to the firewall, this is normally not a problem
- The firewall NIC (using only one here, but there could be a trusted/untrusted pair of NICs) needs to know both IP addresses, because it is involved in both directions. It will naturally know the VM’s IP addres from the route injected by the VNet peering, but it has no obvious way of knowing the IP address space of the SDWAN branches. If the firewall NIC can’t route to the SDWAN IP address, it will just use its default routing (probably to the Internet), which is a bad thing.
- Lastly, the SDWAN NIC needs to know how to route to the source VM through the firewall. If the SDWAN NVA is in the hub peered to the spoke, you would need to overwrite with a UDR the route introduced by the VNet peering to the system routes.

It might be an obvious corollary, but this implies that the SDWAN NVA and the firewall NVA need to be in different subnets, otherwise you cannot override the peering routes for the SDWAN NIC with UDRs without affecting the firewall NIC too.

If you don’t feel like “teaching” the firewall and SDWAN NICs reachability information, you can always resort to the solution of the lazy: build an overlay between the firewall and the SDWAN NVAs with IPsec or VXLAN, so that those NICs/routers in the middle only see the tunnel endpoints (the firewall and SDWAN NVA IP addresses).

## Route tables configure Azure NICs

After realizing the point in the previous section, that routing is performed in the Azure NICs, the next logical question is why are route tables assigned to subnets? This is one of the facts that made my brain melt when I first saw Azure networking, since in traditional routers you configure static routes for the whole thing, and not on an per-interface basis.

Knowing now that “the whole thing” in Azure would be the NIC, it would be logical thinking that route tables should be assigned to individual NICs. And that would be technically possible, only that Azure architects thought that that would be too much of a hassle: if you have thousands of NICs, you would have to do thousands of route table assignments. Hence, they looked for a way of aggregating NICs that had the same routing policy, and the rest is history.

So in essence, a subnet in Azure is not a L2 broadcast domain, but just a logical group of NICs that share the same routing policy. When doing your network designs, make sure that systems that might have different routing policies (and this is almost always the case with Network Virtual Appliances that have dedicated goals) live in their own dedicated subnets.

## Azure doesn’t do recursive routing lookups

On most routers and L3 devices routing lookups are recursive. That means that if the next hop for a route is not directly connected to the router, an additional lookup will be carried out to find out which interface to use for that next hop. However, Azure doesn’t behave this way, which is apparent in the following example.

One of the scenarios where this lack of recursive routing becomes apparent is when trying to use a private endpoint as next hop for a User-Defined Route. Imagine the following topology:

![](Azure%20Networking%20is%20not%20like%20your%20on-onprem%20networ%2083f8ccfdf832423a80955f66dd5b24f4/image-5.png)

You have an NVA exposing some services via an Azure Load Balancer. You create a private link service in the LB’s frontend, and a corresponding endpoint in some other VNet. You define an UDR pointing to the private endpoint. Will it work? Now you know that it won’t. But why?

In the client NIC you see these effective routes:

```
❯ az network nic show-effective-route-table --ids $client_nic_id -o table
Source    State    Address Prefix    Next Hop Type      Next Hop IP
--------  -------  ----------------  -----------------  -------------
Default   Active   10.13.76.0/24     VnetLocal
Default   Active   0.0.0.0/0         Internet
[...]
User      Active   10.13.77.0/24None10.13.76.68Default   Active   10.13.76.68/32    InterfaceEndpoint
```

Other than the local VNet and the Internet route, there are two interesting routes:

- The last route is the /32 route that is created by the private endpoint at `10.13.76.68`, so that the NIC knows how to reach it
- The `User` route has as next hop the IP address of the endpoint, but the next hop type is marked as `None`. Why? Because 10.13.76.68 is not a valid VM in the VNet, and Azure will not do the recursive lookup that would be required to find out that it is actually a private endpoint.

## No endpoint data plane learning, no ARP

Although I haven’t seen many people tripping over this one lately, it does belong in this collection. Most non-SDN networks have endpoint data plane learning. This means that a system only needs to be connected to a network to be able to use it. It will start sending out traffic, and when the network sees the packets coming from the newcomer, it will “learn” its MAC and IP addresses, so that it can now forward traffic that is addressed to it.

Azure doesn’t have data plane learning. Let’s say you have a virtual machine in Azure, and you change the IP address that was allocated by Azure. You start sending traffic from the new IP address, but nothing comes back. Why? Because Azure doesn’t know anything about the new IP address.

This is for example the reason why systems that proxy MAC addresses such as LISP routers or the [Azure Subnet Extension](https://learn.microsoft.com/azure/virtual-network/subnet-extension) NVAs do need to configure every IP address for which they want to proxy-ARP as a secondary IP in Azure, so that the Azure control plane can send packets there.

We know now that subnets are mere administrative boundaries to group NICs that have the same routing policies, but they have no meaning for L2 or L3 forwarding. We know as well that every VM is attached to its own personal router, the NIC, so you could say that L2 domains contain single VMs in Azure. Does ARP has any purpose here? No: since every single packet that exits the VM will have to go through it, our NIC-router can safely proxy-ARP every ARP request with its own MAC address.

## No L3 multicast

So no unknown unicast flooding in Azure, since the only way to reach a system is explicitly telling the Azure control plane where to find it. No L2 broadcast, since there is little reason for it when ARP has no meaning. Additionally no L3 broadcast (often considered a bad practice), and no L3 multicast.

Why no L3 multicast though? You should probably ask the Azure architects, but my educated guess is that implementing multicast properly in the SDN would be a huge effort for “just a bunch of applications”. By the way, a prominent example of those applications using multicast are clustering protocols, from VRRP or HSRP to SQL Server Availability Groups.

Azure Load Balancers have traditionally been the method of choice to replace the lack of HA protocols in Azure. For example, you can read [here](https://learn.microsoft.com/azure/azure-sql/virtual-machines/windows/availability-group-load-balancer-portal-configure?view=azuresql) how to use Azure Load Balancers with SQL Server Availability Groups. For Network Virtual Appliances, I wrote an article some time ago to summarize the different existing approaches: [Deploy highly-available NVAs](https://learn.microsoft.com/azure/architecture/reference-architectures/dmz/nva-ha). There you can see the afore mentioned approach with Azure Load Balancers, as well as other more sophisticated ones such as BGP-injected routes or the Gateway Load Balancer. And I still miss HSRP (sniff sniff).

## So what?

This is probably one of the posts I have written with less applicability to real designs, since all I am doing here is showing how Azure is different as compared to on-premises networks. Still, hopefully this will help you to ease your brain into the transition from on-premises networking to the cloud.

This document provides a comprehensive overview of the differences between Azure Networking and traditional on-premises networks. One of the most significant differences is that routing is performed in the NICs in Azure, which can lead to issues when using third-party appliances that may not consider Azure NICs routing. This means that when designing network architectures, it is essential to keep in mind that Azure NICs can perform three networking functions: routing, traffic filtering, and Network Address Translation.

Another critical difference is that Azure does not perform recursive routing lookups, which is apparent in scenarios where a private endpoint is used as the next hop for a User-Defined Route. When a system is connected to a network in traditional networks, it can start sending traffic, and the network will "learn" its MAC and IP addresses, enabling it to forward traffic that is addressed to it. However, Azure does not have data plane learning, which means that if a virtual machine's IP address is changed, Azure will not know anything about the new IP address.

Additionally, Azure does not require ARP, which is a protocol that is necessary for most non-SDN networks' endpoint data plane learning. Instead, since every packet that exits the VM will have to go through it, the NIC-router can safely proxy-ARP every ARP request with its MAC address. Furthermore, Azure lacks endpoint data plane learning, which means that subnets are administrative boundaries to group NICs that have the same routing policies, but they have no meaning for L2 or L3 forwarding.

Lastly, the document touches on the lack of L3 multicast in Azure, which is probably because implementing multicast in the SDN would be a massive effort for "just a bunch of applications." Instead, Azure Load Balancers have traditionally been the method of choice to replace the lack of HA protocols in Azure.

Overall, understanding these differences is essential when transitioning from on-premises networking to the cloud, and it can help in designing more effective network architectures in Azure.