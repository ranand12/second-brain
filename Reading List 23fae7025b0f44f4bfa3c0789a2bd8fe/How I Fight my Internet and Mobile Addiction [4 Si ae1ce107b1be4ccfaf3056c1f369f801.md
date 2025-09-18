# How I Fight my Internet and Mobile Addiction [4 Simple Tips]

Column: https://pawelurbanek.com/mobile-internet-addiction-focus
Processed: No
created on: July 12, 2021 3:07 PM
topics: mind, self-improvement

![](How%20I%20Fight%20my%20Internet%20and%20Mobile%20Addiction%20%5B4%20Si%20ae1ce107b1be4ccfaf3056c1f369f801/internet-distractions-switch-d8fb49fea8e48d3d26806c000234f5bb85991c848db568ba4a66ea4a731dfd29.jpg)

Disconnecting from internet distractions when working remotely is represented by a switch. Photo by twinsfisch on Unsplash.

Hire me

I'm available to conduct a performance tuning and security audit of your Rails app.

[Tune Your Performance](https://pawelurbanek.com/index.html)

Mindlessly checking social networks, watching YouTube, and permanently distracted by push notifications. Have you been there? In my least technical post so far, I’m going to share a couple of tips on tackling the internet and smartphone addiction.

## How I limit the distractions when working remotely?

As a full-time remote worker, I spend the majority of my waking hours in front of a desktop computer. I’m not very good at resisting the temptation to compulsively check the social media, news, or usage stats of my apps. Instead, I use a simple hack to limit my habit of mindlessly visiting the same websites again and again.

It’s the `/etc/hosts` file. Without going too technical, you can *break* any website by adding the following two lines to this file:

`0.0.0.0 example.com
:: example.com`

Removing the line will immediately restore access to the website. The trick is that it requires you to take several deliberate steps i.e., open the editor, type password, etc. For me, it was more than enough not to bother visiting distracting websites regularly. I also use a bash script to easily restore the blacklist after disabling it every once in a while.

`~/block.sh`

`echo '##############  block ###########
0.0.0.0 www.facebook.com
:: www.facebook.com
0.0.0.0 twitter.com
:: twitter.com
0.0.0.0 www.reddit.com
:: www.reddit.com
#############' >> /etc/hosts`

On MacOS you can also use the popular [SelfControl app](https://selfcontrolapp.com/) to achieve a similar effect. You can check out [this article](https://www.howtogeek.com/howto/27350/beginner-geek-how-to-edit-your-hosts-file/) for more details about modifying the hosts file on different operating systems.

### Blocking ads and distractions with Pi-hole

A bit more sophisticated tool in my battle against the internet distractions is the fantastic [Pi-hole](https://pi-hole.net/) program. Running on a $10 [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) it blocks the ads, trackers and has a configurable blacklist.

![](How%20I%20Fight%20my%20Internet%20and%20Mobile%20Addiction%20%5B4%20Si%20ae1ce107b1be4ccfaf3056c1f369f801/raspberry-pi-zero-62ecd02f09e22edee5c0a5370263649eb16eefe787b1aa1e14ece5c01df6a846.png)

This tiny device can protect your home network from ads and distractions

Currently, I divide distracting websites into two categories. E.g., I check the Twitter couple of times a day, so it is only blocked by Pi-hole. I can disable the blacklist for five minutes using a simple UI:

![](How%20I%20Fight%20my%20Internet%20and%20Mobile%20Addiction%20%5B4%20Si%20ae1ce107b1be4ccfaf3056c1f369f801/pi-hole-ui-fa77f034493559139ca8bb3ae1a5cfb1902ffecb86ea87db3aa60a102b13398f.png)

Five minutes of Twitter button

On the contrary, e.g., the Polish news websites that I consider a total waste of time, but still feel somehow attracted to checking, are on a *semi-permanent* blacklist. I disable them in both Pi-hole and `/etc/hosts`. Restoring access means ~2 minutes of clicking and typing passwords, so I rarely do it.

Pi-hole also works for Wi-Fi connected smartphone, as long as you configure a custom DNS proxy. You can check out the instructions for [iOS](https://appleinsider.com/articles/18/04/22/how-to-change-the-dns-server-used-by-your-iphone-and-ipad) and [Android](https://www.androidpolice.com/2019/12/14/make-android-use-dns-server-choice/).

### Breaking the websites UI

Another trick I use is to cherry-pick and remove the most distracting parts of the sites using the [uBlock origin](https://github.com/gorhill/uBlock) extension.

Example. I’ve realized that I was regularly visiting HackerNews with the intention of just to find articles to read later on my Kindle (I’m using [Push to Kindle 2](https://www.patreon.com/posts/push-to-kindle-2-31045662) extension). Instead, I was getting sucked into reading the discussion threads. I’ve hidden the `comments` button, and now the daily browsing of HackerNews takes much less time.

![](How%20I%20Fight%20my%20Internet%20and%20Mobile%20Addiction%20%5B4%20Si%20ae1ce107b1be4ccfaf3056c1f369f801/hackernews-no-comments-809a3c58470bf3e527c0c3b7d8997377cd89d7390f84910a917d6d7639daf9d4.png)

HackerNews without comments

Another trick I’m using for HackerNews is only to display stories that passed the certain points threshold by using the [special bookmarked URL](https://news.ycombinator.com/over?points=100).

Sample parts of distracting UI that are worth cherry-picking away are Twitter’s *Trends for you* and Youtube’s *Recommended videos*

With your desktop device safely disarmed now, let’s look at even a greater threat to the daily focus: your smartphone.

## Reducing the smartphone usage

I’m using a bit of a *hardcode* approach to overcoming my mobile addiction. Over two years ago, I stopped using an internet-connected smartphone. Ever since a good ol Samsung Solid (let’s call it a *dumb phone* from now on) has been my primary device and I have no plans of turning back.

Before you decide that it’s not possible not to use a smartphone and stop reading, please bear with me for a couple more paragraphs.

Yeah, I kind of lied. I still own an iPhone, but it’s *crippled*. It does not have a SIM card inside. It means that I only can connect it to the internet via Wi-Fi. It might sound silly to carry two mobile phones around, so let me explain.

I use Samsung Solid as my primary device for calls and SMS. I use my iPhone mainly for work and on holidays for photos and [offline maps](https://apps.apple.com/us/app/maps-me-offline-map-nav/id510623322).

In case I’m in an *internet needed emergency*, I can always connect to a Wi-Fi in a nearby cafe, swap the SIM card, or even talk (!) to the stranger and ask for a hotspot. So far I’ve never been in an *internet needed emergency*.

### What’s the point of disconnecting smartphone from the internet?

For me, it was a total gamechanger. Without internet access, there’s not much interesting you can do with a smartphone. Push notifications cannot reach you; news and Twitter are not loading. It kind of turns you off from the state of constant alertness. Regularly disconnecting from all the internet turmoil out there is like a holiday break for the usually overloaded consciousness.

### Can you not turn on the airplane mode instead?

Maybe it will work for you. It did not work for me. I went as far as developing two iOS apps that were supposed to keep me away from my smartphone:

[Block Distracting Websites on iPhone](https://selfcontrol.apki.io/)

It’s not a content marketing post. I really think they are not that effective so I don’t recommend you to buy them.

For me, it was just too simple to turn off all the blockers and return to mindlessly browsing the never-ending content whenever I lost my *mental guard*. Only migrating to a *dumb phone* did the trick and helped me break the habit.

### How to start limiting your smartphone usage?

If you are a daily smartphone user, I highly encourage you to try a *smartphone detox* day.

Buy a simple $50 *dumb phone*, e.g., the new [Nokia 3310](https://www.nokia.com/phones/en_int/nokia-3310). You can go all fancy with [The Light Phone](https://www.thelightphone.com/) or [Mudita](https://mudita.com/), but they are a bit pricey for the similar lack of features. You might also need a [SIM card adapter](https://www.amazon.com/slp/sim-card-adapter/2yfyy6vwye7d7m5).

I bet your daily work commute will feel different. At least it did for me. Your family and friends can still reach you, but push notifications and endless social media streams cannot.

Even if your *dumb phone* has a simple web browser, you might notice that consuming news with the inferior UI is not that tempting at all. Like the content itself did not really matter but rather the shiny box that it’s wrapped in.

## Summary

A lot of smart people out there are building products that are designed from the ground up to be addictive. Business models and profits depend on capturing enough of users’ attention. I’m still a victim of getting my focus highjacked dozens of times each day, but the tools I describe above can help.

Your focus and attention are invaluable. They could be the best advantage or the biggest obstacle in reaching your goals. Don’t give them away without a fight.

![](How%20I%20Fight%20my%20Internet%20and%20Mobile%20Addiction%20%5B4%20Si%20ae1ce107b1be4ccfaf3056c1f369f801/ec2-ssh-access-keys-015c5109473d3d9bfc808b2ec179052f5715e5d19e261285ea21a37056aa84c4.jpg)

Secure SSH access to AWS EC2 instances using temporary security is represented all the keys. Photo by Sergij from Pexels

Hire me

I'm available to conduct a performance tuning and security audit of your Rails app.

[Tune Your Performance](https://pawelurbanek.com/index.html)

Leaving inbound EC2 SSH ports open greatly increases the risk of unauthorized entities running commands on the server. In the perfect world, each developer with access rights would use only a single static IP address. You could whitelist it in an AWS security group firewall in addition to using standard SSH keys based authentication.

In practice, distributed remote dev teams often need to SSH into the servers from constantly changing IP addresses. In this tutorial, I’ll describe how to grant temporary SSH access for dynamic IP addresses using simple AWS CLI bash scripts.

Your EC2 security group firewall currently whitelists `0.0.0.0/0` for port `22`? You’d like to improve the security of this setup without getting lost in AWS complexities? Than this tutorial is for you.

## Why not AWS Session Manager?

AWS offers [an excellent tool](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) for solving exactly this issue, e.i. granting temporary SSH access rights without opening the SSH ports in security groups.

Unfortunately, it comes with a lot of additional complexity involving Cloud Trail, S3, Cloud Watch, and SNS. It also requires you to install additonal software on both server and client, and manage multiple complex IAM roles to orchestrate access logs, etc.

The solution I’d like to propose is significantly simpler to implement. It requires only a standard AWS CLI with minimal permission installed on the client.

Advert

[Heroku migartion to RDS eBook cover](https://pawelurbanek.com/heroku-migrate-postgres-rds)

![](How%20I%20Fight%20my%20Internet%20and%20Mobile%20Addiction%20%5B4%20Si%20ae1ce107b1be4ccfaf3056c1f369f801/title_page_rds-09086cfd2798a34b0f20c30febf5a0e4272a703efa6c269ecd0a1c27e6db1af6.jpg)

My RDS migration guide is now out!

This is the eBook that I wish existed when I was first tasked with moving the Heroku database to AWS as a developer with limited dev ops experience.

[More details](https://pawelurbanek.com/heroku-migrate-postgres-rds)

Let’s get started.

## Check SSH access logs

Before you continue, you might want to check if uninvited guests are knocking on your server’s doors.

Every server instance with publicly facing IP address and opened ports is constantly targeted by malicious network scanning bots. Those bots are usually harmless but they can always start a DDoS attack or discover a vulnerability.

You can check how often your server is targeted by scanner bots by SSHing into it and running these commands:

`grep "invalid" /var/log/auth.log
grep "failed" /var/log/auth.log`

`/var/log/auth.log` is the default SSH log file for Ubuntu systems

you should see the similar output:

`Oct 25 07:15:44 : Disconnected from invalid user test 1.2.3.4 port 43401 [preauth]
Oct 25 08:07:33 : Disconnected from invalid user user 1.2.3.4 port 34930 [preauth]
Oct 25 09:20:01 : Disconnected from invalid user admin 1.2.3.4 port 38688 [preauth]
Oct 25 09:53:27 : Disconnected from invalid user guest3 1.2.3.4 port 59294 [preauth]`

Bot login attempts are failing in the `preauth` phase because they are using passwords, and your server is configured only to accept [public/private key](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) based logins.

If you’ve enabled password authentication to your server by adding this line to `/etc/ssh/sshd_config` file:

`PasswordAuthentication yes`

you could also see a similar output:

`Oct 25 10:06:19 : Failed password for ubuntu from 1.2.3.4 port 50703 ssh2
Oct 25 10:22:32 : Failed password for admin from 1.2.3.4 port 50703 ssh2
Oct 25 10:22:36 : Failed password for user from 1.2.3.4 port 50703 ssh2`

Unless absolutely necessary enabling password-based login should be avoided.

If you don’t see any output, looks like your server if currently not targeted. It was not the case for my AWS EC2 instances. All of them started receiving *unwanted visitors* just minutes after provisioning.

Completing this tutorial will permanently cut off all the scanner bots, and other unauthorized access attempts to your server.

## Prequisities

The rest of this tutorial assumes that you already have a running EC2 instance on public IP with SSH access for your user.

Also make sure to install the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) before continuing.

Now you should remove all the security groups rules that allow connection to your EC2 instance with SSH port 22. Confirm that you can no longer connect by running this command:

`ssh -o ConnectTimeout=5 -v ubuntu@123.123.123.123`

Replace `ubuntu` and `123.123.123.123` with the public IP and user of your EC2 server.

It should fail with the following output:

`debug1: Connecting to 123.123.123.123 [123.123.123.123] port 22.
debug1: connect to address 123.123.123.123 port 22: Operation timed out
ssh: connect to host 123.123.123.123 port 22: Operation timed out`

If you managed to connect, it means that there’s still some security group whitelisting inbound connections on port 22, so make sure to remove it before continuing.

## Setup ephemeral security group firewall and IAM user

In **EC2** section of AWS console go to **Security groups** and click **Create security group**. You can name the new group `ephemeral-ec2-ssh-access`, and assign it to the same VPC as your EC2 instance. Don’t add any inbound rules.

New security group with no inbound rules

Now go to **Instances**, select your EC2 instance, click **Actions > Networking > Change Security Groups** and assign your newly created `ephemeral-ec2-ssh-access` security group.

Let’s move on to creating an IAM user now. Go to **IAM** section and click **Users > Add user**.

You can call it whatever you want, e.g., `SSHEphemeralEC2AccessGroupManager`.

Make sure to select only `Programmatic access`

Complete the user creating wizard without granting him any policies and write down `Access key ID` and `Secret access key` .

Now go to the newly created user details and click **Add inline policy**. Select **JSON** policy format and paste the following content:

`{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:RevokeSecurityGroupIngress"
            ],
            "Resource": [
                "arn:aws:ec2:[REGION]:[ACCOUNT_NUMBER]:security-group/[SECURITY_GROUP_ID]",
                "arn:aws:ec2:[REGION]:[ACCOUNT_NUMBER]:security-group/[SECURITY_GROUP_ID]"
            ]
        }
    ]}`

You have to replace:

`REGION` with the code of your AWS region, e.g., `us-west-1` for North California.

`ACCOUNT_NUMBER` is your AWS account ID. You can find it in **My account** tab e.g. `123123123123`.

`SECURITY_GROUP_ID` is the ID of the `ephemeral-ec2-ssh-access` security group you just created e.g. `sg-07bbca7652e83a101`.

If your JSON correct in the policy review screen you should see the **Summary** mentioning your security group displayed:

If you can see a warning that policy does not grant any permissions than double-check your region, account number, and security group ID.

So much for clicking in the AWS UI. The rest of the setup can be done straight from the terminal.

## Configure AWS CLI scripts

One more thing we need to do is to write two simple bash scripts, literally:

`bin/open_ssh`

and

`bin/close_ssh`

Running them will toggle the inbound rule in `ephemeral-ec2-ssh-access` security group for your current IP address and port 22.

I usually add those scripts in `bin` directory of each of my projects. Every project has a separate security group and IAM user assigned.

Let’s start by configuring your AWS CLI with the profile:

`aws configure --profile your-profile-name`

You need to provide correct access credentials for your new `SSHEphemeralEC2AccessGroupManager` IAM user.

Now add the scripts doing the actual opening and closing of SSH ports:

`bin/open_ssh`

`#!/bin/sh

WHITELISTED_IP=$(curl https://ifconfig.me 2> /dev/null)

echo "Opening SSH for ${WHITELISTED_IP}"

aws ec2 authorize-security-group-ingress \
--profile your-profile-name \
--group-name ephemeral-ec2-ssh-access \
--region us-west-1 --protocol tcp --port 22 \
--cidr "${WHITELISTED_IP}/32" 2> /dev/null`

`bin/close_ssh`

`#!/bin/sh

WHITELISTED_IP=$(curl https://ifconfig.me 2> /dev/null)

echo "Closing SSH for ${WHITELISTED_IP}"

aws ec2 revoke-security-group-ingress \
--profile your-profile-name \
--group-name ephemeral-ec2-ssh-access \
--region us-west-1 --protocol tcp --port 22 \
--cidr "${WHITELISTED_IP}/32" 2> /dev/null`

Replace `us-west-1` with the code of your AWS region

That’s it! Now execute your script and confirm that you can SSH into your server:

`bin/open_ssh
ssh ubuntu@123.123.123.123`

If you have trouble getting it to work, you can remove silencing the output of `aws` command (`2> /dev/null`) to help you debug. AWS CLI error messages are usually quite descriptive.

Inbound SSH port is now opened for your IP. Even if you forget to run `bin/close_ssh`, no other IP address can access your EC2. It’s an additional security factor, so the correct SSH keys are still necessary. The risk of sometimes leaving the port open for a single IP is negligible. The potential attacker would first have to access the same IP as you. You should be safe, unless your next-door neighbor is up to something.

### Automate toggling SSH access

You can wrap your common server tasks in those open/close scripts. I do it for deploys and console access of my Rails side project [Abot for Slack](https://abot.app/) that’s hosted with [Dokku](https://github.com/dokku/dokku).

`bin/prod_deploy`

`#!/bin/sh

bin/open_ssh
git push dokku master
bin/close_ssh`

`bin/rails_console`

`#!/bin/sh

bin/open_ssh
dokku --rm run rails c
bin/close_ssh`

I use this approach as a one-man team, but it should scale for more developers working on the same project. Each team member could use his ephemeral security group managed by a separate IAM user.

## Summary

The additional security of constantly closed SSH ports hardly affects my workflow. I don’t have to use VPN, 2FA, or login into a special bastion host to access the production system securely. It’s just the good ol’ SSH and two simple scripts. Once configured, they are barely noticeable but guarantee to keep the bad guys out.

This approach might not grant your project the PCI compliance certificate, but should be good enough for many use cases.