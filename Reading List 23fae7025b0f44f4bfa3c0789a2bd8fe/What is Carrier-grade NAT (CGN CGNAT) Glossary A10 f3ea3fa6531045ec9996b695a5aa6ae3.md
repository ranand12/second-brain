# What is Carrier-grade NAT (CGN/CGNAT)? | Glossary | A10 Networks

Column: https://www.a10networks.com/glossary/what-is-carrier-grade-nat-cgn-cgnat/
Processed: No
created on: March 2, 2023 11:46 AM
topics: networking, tech-stuff

![standard-network-address-translation-800px.png](What%20is%20Carrier-grade%20NAT%20(CGN%20CGNAT)%20Glossary%20A10%20f3ea3fa6531045ec9996b695a5aa6ae3/standard-network-address-translation-800px.png)

Way back in the early days of the internet (the 1980s) every connected computer was intended to have its own unique public IP address. IP addressing was originally defined by four octets—four groups of eight bits, a [standard called IPv4](https://www.a10networks.com/glossary/what-is-ipv4/)—which resulted in over four billion unique values (actually, 4,294,967,296), so at the time it seemed we’d never run out.

By late 1980’s, however, it became apparent that the dramatic adoption rate of the internet would eventually deplete this large pool of addresses. [IPv6 was envisioned](https://www.a10networks.com/glossary/what-is-ipv6/) as a successor protocol to IPv4 and would solve the limited address space. However, IPv6 was not made to be backward compatible, and the problem of limited addresses still became an issue. Carrier Grade NAT (CGNAT) was created as a solution to address this problem, primarily for service providers.

## IPv4 Exhaustion – The History

In June 1992, as a result of the astounding growth of the internet, RFC 1338, [Supernetting: an Address Assignment and Aggregation Strategy](https://www.rfc-editor.org/rfc/rfc1338), was published. This memo was the first to discuss the consequences of the “eventual exhaustion of the 32-bit IP address space.” Two years later RFC 1631, The IP [Network Address Translator (NAT)](https://www.rfc-editor.org/rfc/rfc1631), was published which proposed a solution:

> “Until the long-term solutions are ready, an easy way to hold down the demand for IP addresses is through address reuse. This solution takes advantage of the fact that a very small percentage of hosts in a stub domain are communicating outside of the domain at any given time. (A stub domain is a domain, such as a corporate network, that only handles traffic originated or destined to hosts in the domain). Indeed, many (if not most) hosts never communicate outside of their stub domain. Because of this, only a subset of the IP addresses inside a stub domain, need be translated into IP addresses that are globally unique when outside communications is required.”
> 

### Proven CGNAT Solutions

A10 Networks’ IPv4 preservation with carrier-grade NAT (CGNAT) and [IPv6 migration](https://www.a10networks.com/glossary/what-is-ipv6-migration-and-why-is-it-necessary/) technologies are proven solutions to meet your increased subscriber and IoT network expansion demands and ensure connectivity.

[Learn More](https://www.a10networks.com/solutions/service-provider/cgnat-ipv6-to-ipv4-migration/)

### International Communications Service Providers Insights 2021

This research was conducted to understand the challenges and issues facing communications service providers when it comes to the lasting impact that COVID-19 has had on their subscribers and enterprises. It identifies trends in demand and usage patterns, expectations around security and resiliency in what has been an unprecedented year. It examines communications service providers’ plans for investment, adoption of new technologies, and the complexity of operating in the current hybrid environment.

[Get the Report](https://www.a10networks.com/resources/white-papers/end-ipv4-migration-paths-ipv6)

### The End of IPv4? Migration Paths to IPv6

The advent of new Internet-connected locations and Internet-connected devices has precipitated IPv4 exhaustion, because each device places greater pressure on the existing IPv4 infrastructure. Learn about various techniques for IPv6 Migration, IPv4 Preservation and IPv4/IPv6 Translation.

[Learn More](https://www.a10networks.com/resources/white-papers/end-ipv4-migration-paths-ipv6/)

### CGNAT Isn’t a Capability, It’s a Lifecycle Strategy

Exponential subscriber growth and connected IoT devices has forced service providers to investing in infrastructure to support increased traffic. With the global IPv4 exhaustion and the adoption of IPv6, service providers are facing challenges in sustaining growth and business continuity. This white paper provides an overview of the various components that are required for a CGNAT and IPv6 migration solution.