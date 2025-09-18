# Journey Of The Geek | The chronicles of a Bostonian tech geek navigating through life, technology, and general geekiness.

Column: https://journeyofthegeek.com/
Processed: No
created on: November 4, 2022 12:25 PM
topics: azure, tech-stuff

Welcome to part 2 of my series on Azure Backup and Resource Guard. In [my first post](https://journeyofthegeek.com/2022/10/18/protecting-azure-backups-with-resource-guard-part-1/), I gave some background on the value proposition Resource Guard provides. In this post I’ll be walking through how to configure it and demonstrating it in action. I’ll be using the lab pictured below which is based off the Azure Backup [demo lab I have up on GitHub](https://github.com/mattfeltonma/azure-backup-demo).

![](Journey%20Of%20The%20Geek%20The%20chronicles%20of%20a%20Bostonian%20%204f9369f8cff0405b89e20716bdfcc0b4/azure-backup-lab-2.png)

Lab used to demonstrate Resource Guard

For this demonstration, I used my jogcloud.com Azure AD tenant as the primary tenant where the Recovery Service Vaults will be stored. I have a small environment in my at home lab that is configured with a Windows Active Directory forest that is synchronized to that tenant. The geekintheweeds.com Azure AD tenant acted as the secondary tenant containing the Resource Guard. Homer Simpson will act as the owner of the Resource Guard (perhaps he is someone in Information Security) in the geekintheweeds.com tenant and Maggie Simpson will own the subscription containing the workload and Recovery Services Vault (emulating a typical application owner) in the jogcloud.com tenant.

Since both users are sourced from my on-premises Windows Active Directory forest and synchronized to jogcloud.com, I used [Azure AD’s B2B feature](https://learn.microsoft.com/en-us/azure/active-directory/external-identities/what-is-b2b) to invite Homer Simpson into the geekintheweeds.com tenant. Once added through the B2B process, I setup an RBAC assignment granting Homer Simpson Owner of the subscription containing the Resource Guard.

![](Journey%20Of%20The%20Geek%20The%20chronicles%20of%20a%20Bostonian%20%204f9369f8cff0405b89e20716bdfcc0b4/azure-backup-lab-1-1.png)

Role Assignment in geekintheweeds.com tenant

Next up I went to create the Resource Guard in the GIW tenant and received the error below when attempting to create the Resource Guard resource in the GIW Tenant.

![](Journey%20Of%20The%20Geek%20The%20chronicles%20of%20a%20Bostonian%20%204f9369f8cff0405b89e20716bdfcc0b4/azure-backup-lab-3.png)

Error creating Resource Guard

The error message was pretty useless (not atypical of Azure errors). In this case, this error is due to the Microsoft.DataProtection r[esource provider](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-providers-and-types) not being registered in this subscription. Once registering the resource provider in question, the Resource Guard was provisioned without issue. One thing to note is that while the Resource Guard can exist within a different resource group, subscription, or tenant, it must be in the same region as the Recovery Services Vault it is protecting.

![](Journey%20Of%20The%20Geek%20The%20chronicles%20of%20a%20Bostonian%20%204f9369f8cff0405b89e20716bdfcc0b4/azure-backup-lab-4.png)

Registering Microsoft.DataProtection resource provider

Once the Resource Guard resource was provisioned, I needed to give Maggie Simpson appropriate access over the Recovery Services Vault in the jogcloud.com tenant. For that, I provisioned a role assignment for the Contributor role on the subscription to the System Operators group synchronized from on-premises that Maggie is a member of.

![](Journey%20Of%20The%20Geek%20The%20chronicles%20of%20a%20Bostonian%20%204f9369f8cff0405b89e20716bdfcc0b4/azure-backup-lab-5.png)

Role Assignment in jogcloud.com tenant

Navigating to the Recovery Services Vault, Maggie Simpson is capable of modifying the soft delete feature (note it’s disabled for the purposes of this lab so the resources can be easily removed).

![](Journey%20Of%20The%20Geek%20The%20chronicles%20of%20a%20Bostonian%20%204f9369f8cff0405b89e20716bdfcc0b4/azure-backup-lab-6.png)

Prior to Resource Guard, Maggie Simpson can modify Soft Delete

Switching over to Homer Simpson and logging into the jogcloud.com tenant, I attached the Resource Guard to the Recovery Services Vault. The interface allowed me to select the tenant (directory) and the Resource Guard resource.

![](Journey%20Of%20The%20Geek%20The%20chronicles%20of%20a%20Bostonian%20%204f9369f8cff0405b89e20716bdfcc0b4/azure-backup-lab-7.png)

Enabling Resource Guard

I had configured the Resource Guard to protect [all the operations it was able to](https://learn.microsoft.com/en-us/azure/backup/multi-user-authorization?pivots=vaults-recovery-services-vault#select-operations-to-protect-using-resource-guard). This is confirmed with the confirmation in the screenshot below.

![](Journey%20Of%20The%20Geek%20The%20chronicles%20of%20a%20Bostonian%20%204f9369f8cff0405b89e20716bdfcc0b4/azure-backup-lab-8.png)

Resource Guard configured to protect sensitive operations

Once the Resource Guard is enabled, navigating back to the Security Settings of the Recovery Services Vault displays a message that Resource Guard is now enabled.

![](Journey%20Of%20The%20Geek%20The%20chronicles%20of%20a%20Bostonian%20%204f9369f8cff0405b89e20716bdfcc0b4/azure-backup-lab-9.png)

Switching back to Maggie Simpson, I then attempted to modify a backup policy which is considered a sensitive operation and is restricted via the association to the Resource Guard. As expected, Maggie Simpson cannot make the modifications to the Recovery Services Vault without authenticating to the GIW tenant and being authorized on the Resource Guard.

![](Journey%20Of%20The%20Geek%20The%20chronicles%20of%20a%20Bostonian%20%204f9369f8cff0405b89e20716bdfcc0b4/azure-backup-lab-10.png)

Maggie Simpson blocked from using Resource Guard

Success! Here we demonstrated how we can restrict sensitive operations on an Azure Backup Vault even when a user has a high level of permissions on the vault itself. Resource Guard provides a great security mechanism to establish the blast radius that works best for your organization. I could even add [Azure AD PIM](https://learn.microsoft.com/en-us/azure/backup/multi-user-authorization?pivots=vaults-recovery-services-vault#authorize-critical-protected-operations-using-azure-ad-privileged-identity-management) to the mix in the support just-in-time access of the Resource Guard. The support for cross-tenant specifically is very unique because there are very few (if any) other Azure resources that allow you to leverage a cross-tenant security boundary.

If you’re using Azure Backup, you should be using Resource Guard as an additional security control to add to the controls you are enforcing with Azure RBAC and Azure Policy. With the introduction into [preview of the immutable vaults](https://azure.microsoft.com/en-gb/updates/azure-backup-immutable-vaults-preview/), Microsoft is providing a variety of tools to take a defense-in-depth approach using the technical features that make the most sense to the needs of your organization. WIth that bit of sales speak, I’m out for the weekend.

Thanks for reading!

[Revisiting UDR improvements for Private Endpoints](https://journeyofthegeek.com/2022/09/25/revisiting-udr-improvements-for-private-endpoints/)

![](Journey%20Of%20The%20Geek%20The%20chronicles%20of%20a%20Bostonian%20%204f9369f8cff0405b89e20716bdfcc0b4/peudr4-2.png)

![](Journey%20Of%20The%20Geek%20The%20chronicles%20of%20a%20Bostonian%20%204f9369f8cff0405b89e20716bdfcc0b4/peudr1-2.png)

PaaS with no Private Endpoint

![](Journey%20Of%20The%20Geek%20The%20chronicles%20of%20a%20Bostonian%20%204f9369f8cff0405b89e20716bdfcc0b4/peudr2.png)

PaaS with Private Endpoint

![](Journey%20Of%20The%20Geek%20The%20chronicles%20of%20a%20Bostonian%20%204f9369f8cff0405b89e20716bdfcc0b4/peudr3.png)

Common workaround for inspection of Private Endpoint traffic

![](Journey%20Of%20The%20Geek%20The%20chronicles%20of%20a%20Bostonian%20%204f9369f8cff0405b89e20716bdfcc0b4/peudr4-2%201.png)

Lab environment

![](Journey%20Of%20The%20Geek%20The%20chronicles%20of%20a%20Bostonian%20%204f9369f8cff0405b89e20716bdfcc0b4/peudr6.png)

Request without new Private Endpoint features turned on

![](Journey%20Of%20The%20Geek%20The%20chronicles%20of%20a%20Bostonian%20%204f9369f8cff0405b89e20716bdfcc0b4/peudr8.png)

Request with new routing features enabled

![](Journey%20Of%20The%20Geek%20The%20chronicles%20of%20a%20Bostonian%20%204f9369f8cff0405b89e20716bdfcc0b4/nsg-lab.png)

Lab environment