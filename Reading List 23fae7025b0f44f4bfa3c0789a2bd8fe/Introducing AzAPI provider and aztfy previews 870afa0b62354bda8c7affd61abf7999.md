# Introducing AzAPI provider and aztfy previews

Column: https://techcommunity.microsoft.com/t5/azure-tools-blog/announcing-azure-terrafy-and-azapi-terraform-provider-previews/ba-p/3270937
Processed: No
created on: May 4, 2022 6:57 PM
topics: azure, tech-stuff

Infrastructure modernization these days typically involves one or more public clouds which enables the most agility, innovation and future proof for your business. A key component that enables businesses to manage their cloud infrastructure in a repeatable, understandable, and safe way is Infrastructure as Code (IaC) Tooling.

On Azure, businesses may choose many flavors of IaC tooling to manage their Azure resources including [HashiCorp Terraform,](https://docs.microsoft.com/en-us/azure/developer/terraform/) [Bicep,](https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview?tabs=bicep) [ARM templates,](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/overview) [Ansible](https://docs.microsoft.com/en-us/azure/developer/ansible/overview) and many more. We encourage you to choose the IaC tool that best suits your needs. Our mission is to ensure that no matter which tool you choose, you have the best experience and integration with Azure.

To that end, we’re making it easier for you to use HashiCorp Terraform with Azure in two significan ways:

- By strengthening some of the challenges that our customers have shared with us around Azure Terraform resource support and coverage.
- By helping export Azure resources into HCL files so that you can manage your infrastructure declaratively using Terraform with Azure.

We are excited to be releasing preview versions of a few new tools that we hope and expect will make your experience with using Terraform on Azure even better than it already is.

## Scenarios

Before we dive into the details of the new tooling, let’s take a look at a few scenarios that may resonate with you.

Even if you are familiar with Terraform and Azure, sometimes it can be a challenge to determine how to author a Terraform configuration that will result in the exact infrastructure that you are looking for. This typically results in an iterative process where you define a configuration, apply it, then visit the portal to determine if the infrastructure looks like you expected. This is very time consuming, and we are here to help.

### Existing Infrastructure

Your current infrastructure was set up by you or someone who came before you. It may have been around “forever,” so who really knows exactly what the settings are now. You’ve adopted IaC for all new deployments and need to make some minor changes to this existing infrastructure or maybe even duplicate it. This sort of task looks daunting, but we’re here to help.

The Azure team works hard to add features and functionality that will make your jobs easier. This new functionality is ordinarily released in phases, starting with private and then public preview and, finally, it is stable and made generally available. Many customers, like you, use Terraform to manage their infrastructure and are eager to adopt these new features. Terraform does not usually support these features until the final, generally available stage. This can results in clunky IaC workarounds, but we are here to help.

Azure has a vast cornucopia of services and features that are continually expanding and changing. Terraform supports the vast majority of them, but when you need to manage a features or service that is not yet supported, you end up having to fall back on imperfect work arounds, or “escape hatches,” that do not take advantage of all of the goodness you expect from Terraform. This is less than ideal, but we are here to help.

With the aforementioned escape hatches are put in place, you can breathe a sigh of relief and get on with the rest of your work. Then the day comes when the “official” support is added to Terraform, and you want to remove those workarounds. The trick nw is to remove the workarounds without having to destroy your infrastructure and redeploy it. This process is anything but straight forward, but we are here to help.

We want your experience using Terraform with Azure to be delightful, and are super excited to share these open-source tools with you. The preview versions of these tools are available to use today. We invite you to download them and get started.

*Scenarios: Getting Started with Terraform, Migrating Existing Infrastructure*

With Azure Terrafy, you can quickly and easily turn existing Azure infrastructure into Terraform HCL and will import to Terraform state. After you have completed importing your infrastructure, you can be manage it with your standard IaC processes.

Here’s how:

1. Verify that the AzureRM resource types and resource names are what you expect,
    
    [](Introducing%20AzAPI%20provider%20and%20aztfy%20previews%20870afa0b62354bda8c7affd61abf7999/large)
    
    aztfy will do the hard work of creating the HCL, complete with dependencies, and updating the state.
    
2. 
    
    [](Introducing%20AzAPI%20provider%20and%20aztfy%20previews%20870afa0b62354bda8c7affd61abf7999/medium)
    
    Finally, validate that your configuration matches your infrastructure by running.
    
3. 
    
    [](Introducing%20AzAPI%20provider%20and%20aztfy%20previews%20870afa0b62354bda8c7affd61abf7999/large%201)
    

Learn more about [aztfy](https://github.com/azure/aztfy) from the GitHub repo and download the [latest binaries](https://github.com/Azure/aztfy/releases) for your OS.

*Scenarios: Azure Preview Functionality, Escape Hatch, Remove Escape hatch*

The AzAPI provider is a very thin layer on top of the Azure ARM REST APIs. Use this new provider to authenticate to - and manage - Azure resources and functionality using the Azure Resource Manager APIs directly. This provider compliments the Azure Resource Manager provider (AzureRM provider) by enabling the management of Azure resources that are not yet or might never be supported in the AzureRM provider, such as private and public preview services and features.

Unlike some of the workarounds that you might currently be using to manage preview features and functionality such as a null resource to call the Azure CLI, this provider and resources are fully compatible with Terraform. This compatibility ensures that you get all the benefits of Terraform that you rely on.

To allow you to manage all Azure resources and features with this provider without requiring updates, the provider includes the following generic resources:

[Untitled](Introducing%20AzAPI%20provider%20and%20aztfy%20previews%20870afa0b62354bda8c7affd61abf7999/Untitled%20c78aa993be1048bb88ddda548c5da6dd.csv)

1. Configure a resource that does not currently exist in the AzureRM provider.
    
    [](Introducing%20AzAPI%20provider%20and%20aztfy%20previews%20870afa0b62354bda8c7affd61abf7999/large%202)
    
    Configure a preview property for an existing resource from AzureRM.
    
2. 
    
    [](Introducing%20AzAPI%20provider%20and%20aztfy%20previews%20870afa0b62354bda8c7affd61abf7999/large%203)
    

Finally, to ensure your experience using the AzAPI provider — from authoring your configuration to migrating to the AzureRM provider—is as easy and streamlined as possible, we’ve created the following tools:

- The Visual Studio Code extension and language server provides a rich authoring experience, complete with intellisense, code completion, hints, syntax validation, quick info and many other key features.
- The AzureRM provider provides the best and most integrated Terraform experience for managing Azure resources. Although the AzAPI provider may be used while a service or feature is in preview, we expect customers to move to the AzureRM provider once the service is officially released. To streamline this migration from the AzAPI provider to the AzureRM provider, we have created the AzAPI2AzureRM tool to automate the process of converting AzAPI resources to AzureRM resources.

Learn more about [AzAPI provider and associated tools](https://docs.microsoft.com/en-us/azure/developer/terraform/overview-azapi-provider) on Microsoft Docs.

## Let us hear from you

We look forward to hearing your feedback! Feel free to ask a question, report a problem or suggest a feature by opening an issue in our [GitHub repo](https://github.com/Azure/terraform/issues). If someone else has already mentioned the issue you want to report, let us know it is important to you as well by reacting to the issue with a thumbs-up emoji. To help ensure these tools perform well for you and everyone else, consider tracking the status of your issue and working with us directly in the discussions area.

We would love your continued feedback on Azure Terraform deployments. If you are interested in deeper conversations with the engineering team, [sign up for our Azure Terraform community calls](https://aka.ms/aztfcommunity).