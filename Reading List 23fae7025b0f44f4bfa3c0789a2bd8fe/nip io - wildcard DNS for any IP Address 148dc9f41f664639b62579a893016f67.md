# nip.io - wildcard DNS for any IP Address

Column: https://nip.io/
Processed: No
created on: February 3, 2022 12:08 PM
topics: tech-stuff

Stop editing your `etc/hosts` file with custom hostname and IP address mappings.

[nip.io](https://nip.io/) allows you to do that by mapping any IP Address to a hostname using the following formats:

Without a name:

- `10.0.0.1.nip.io` maps to `10.0.0.1`
- `192-168-1-250.nip.io` maps to `192.168.1.250`
- `0a000803.nip.io` maps to `10.0.8.3`

With a name:

- `app.10.8.0.1.nip.io` maps to `10.8.0.1`
- `app-116-203-255-68.nip.io` maps to `116.203.255.68`
- `app-c0a801fc.nip.io` maps to `192.168.1.252`
- `customer1.app.10.0.0.1.nip.io` maps to `10.0.0.1`
- `customer2-app-127-0-0-1.nip.io` maps to `127.0.0.1`
- `customer3-app-7f000101.nip.io` maps to `127.0.1.1`

[nip.io](https://nip.io/) maps `<anything>[.-]<IP Address>.nip.io` in **"dot"**, **"dash"** or **"hexadecimal"** notation to the corresponding `<IP Address>`:

- dot notation: `magic.127.0.0.1.nip.io`
- dash notation: `magic-127-0-0-1.nip.io`
- hexadecimal notation: `magic-7f000001.nip.io`

The "dash" and "hexadecimal" notation is especially useful when using services like [LetsEncrypt](https://letsencrypt.org/) as it's just a regular sub-domain of [nip.io](https://nip.io/)

## About this service

[nip.io](https://nip.io/) is powered by [PowerDNS](http://www.powerdns.com/) with a simple, custom [PipeBackend](https://doc.powerdns.com/authoritative/backends/pipe.html) written in Python: [backend.py](https://github.com/exentriquesolutions/nip.io/blob/master/nipio/backend.py)

It's open source, licensed under Apache 2.0: [https://github.com/exentriquesolutions/nip.io](https://github.com/exentriquesolutions/nip.io) — pull requests are welcome.

This is a free service provided by [Exentrique Solutions](http://exentriquesolutions.com/) (the same people who run [XP-Dev.com](https://xp-dev.com/) which offer [Git, Mercurial and Subversion hosting](https://xp-dev.com/)).

Feedback is appreciated, just  [raise an issue in GitHub](https://github.com/exentriquesolutions/nip.io/issues) .

## Troubleshooting

### DNS Rebinding Protection

Some DNS resolvers, forwarders and routers have [DNS rebinding protection](https://en.wikipedia.org/wiki/DNS_rebinding) which may result in failure to resolve local and private IP addresses. This service won't work in those situations.

- [localtls](https://github.com/Corollarium/localtls): A DNS server in Python3 to provide TLS to webservices on local addresses. It resolves addresses such as '192-168-0-1.yourdomain.net' to 192.168.0.1 and has a valid TLS certificate for them.
- [sslip.io](https://sslip.io/): Alternative to this service, supports IPv6 and custom domains.
- [local.gd](https://local.gd/): Alternative to this service, where everything is mapped to localhost/127.0.0.1.