# A Guide to Navigating the AKS Enterprise Documentation & Scripts – Buchatech.com

Column: https://www.buchatech.com/2022/08/a-guide-to-navigating-the-aks-enterprise-documentation-scripts/
Processed: No
created on: August 8, 2022 4:21 PM
topics: azure, kubernetes, tech-stuff

![](A%20Guide%20to%20Navigating%20the%20AKS%20Enterprise%20Documenta%2007d8c81551c442e7af4a23ce2ad57f8b/AKS-Doc-Guide-Header-1.png)

**NOTE:** *As with all of my blog posts the views and opinions on this post are my own and are not that of my employer.*

The goal of this blog is to serve as Guidance on Microsoft AKS Enterprise Documentation.

Before joining Microsoft, I was in the F500/F100 consulting world. I was focused on Azure, DevOps, and Kubernetes. Many organizations had an interest in utilizing a managed Kubernetes service. This would often lead them to Azure Kubernetes Service (AKS). We spent time guiding organizations on how to get started with AKS including the **design of the architecture**, **deployment**, and **operation of it**.

Like with Azure and other platforms that have a lot of moving parts, AKS has many design areas that need to be covered as a part of the design and implementation. The core areas are:

- IAM (Identity and access management)
- Networking (topology, IP addressing, Ingress, load balancing, service mesh, Web App Firewall, etc.)
- Governance (Resource organization, taxonomy, etc.)
- Security (platform security, image security, runtime security, secrets management, etc.)
- Management and Operations (monitoring, backup, DR, etc.)
- Automation and DevOps (Orchestration, service discovery, Configuration, Autoscaling, CI/CD/GitOps, etc.)

These are in addition to the core but come into play with the apps that will run on top of Kubernetes:

- Applications
- Data

*In order to simplify Kubernetes projects, you can funnel them down to **three phases**; **Design**, **Deploy**, and **Operate**.*

This is a lot of ground to cover on top of gaining a solid understanding of Kubernetes itself. Microsoft has created a set of resources that can simplify and accelerate the adoption of Kubernetes. This is a set of resources that help you build out landing zones for AKS and some for Azure. These resources live in the Azure Architecture Center (AAC). The AAC is where you get guidance for architecting solutions on Azure using established patterns and practices.

I highly recommend any team and organization that plans to adopt Kubernetes utilize these artifacts from Microsoft to help you along your journey. This will ensure your AKS clusters are enterprise ready. When starting with AKS it can be confusing when and in what order to use these resources.

Again, the goal of this blog post is to give you a guide on how to use these resources. I will list these resources here in order with a brief description of them, when to use them, and how to use them:

# DESIGN-

Part #1 is to start with architecting. You will need to start with designing your AKS architecture. There are several documents that can assist with this as you work through your AKS architecture design. You will want to start with the Baseline architecture for an Azure Kubernetes Service (AKS) document. This document is core for designing AKS, however, there are some additional AKS documents that you will want to utilize in addition to the Baseline architecture for an Azure Kubernetes Service (AKS). These additional documents will depend on your organization’s specific use case.

### Baseline architecture for an Azure Kubernetes Service (AKS) cluster

**What it is:**

The AKS baseline gives you detailed recommendations for networking, security, identity, management, and monitoring of AKS clusters. This baseline takes you through all the needed facets of AKS to come up with a plan for implementing AKS across your enterprise. The final result will be based on your organization’s business requirements.

**How to use it:**

This document will take you through 6 core areas divided up into sections with sub-sections.

![](A%20Guide%20to%20Navigating%20the%20AKS%20Enterprise%20Documenta%2007d8c81551c442e7af4a23ce2ad57f8b/AKS-doc-guide-1.jpg)

You will start with your networking and work your way through the sections finishing off with operations.

This document has a Visio file of the AKS architecture you can download to get you started. You can download this right away and build it out with specifics to your needs as you work through this document. In fact, there are multiple Visio templates you can download to help.

![](A%20Guide%20to%20Navigating%20the%20AKS%20Enterprise%20Documenta%2007d8c81551c442e7af4a23ce2ad57f8b/AKS-doc-guide-2.jpg)

A common area that folks really struggle with when getting started with AKS is planning the IP addresses. Teams need help deciding to use Kubenet or Azure CNI for the networking model. You cannot change this on an AKS cluster after it is deployed so you have to make this decision upfront. The only way to go from one networking model to another is to deploy a new cluster. Admins often worry about IP exhaustion when utilizing Azure CNI. There is a Visio and another sub-doc to help with all of this within the IP Address section. It has a link to this: repo ([https://github.com/mspnp/aks-baseline/blob/main/networking/topology.md](https://github.com/mspnp/aks-baseline/blob/main/networking/topology.md)) that has a markdown file that has a table to help with planning your subnets for AKS and this document that helps you determine to go with Kubenet or Azure CNI as well as critical information on each model type and IPs.

This document also covers GitOps, multi-tenancy, and cost management with AKS.

***LINK TO THE DOCUMENT:** [https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks/secure-baseline-aks](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks/secure-baseline-aks)*

The next four documents I am going to mention fit different scenarios so you may or may not need them. I will call out in the “How to use it” sections below each reference.

### AKS Secure Baseline with Private Cluster

**What it is:**

This document helps you deploy a secure AKS cluster, compliant with Enterprise-Scale for AKS guidance and best practices. This document also contains links to reference scripts for deploying a private AKS cluster.

**How to use it:**

In practice in the real world, you will want to deploy a private AKS cluster 99% of the time. There needs to be a very solid reason not to. By doing this alone you will greatly improve the security posture of your AKS cluster. By default, when you deploy AKS the API server is accessible via a public IP. Deploying a private AKS cluster makes the AKS API Server private and only accessible on the Azure or when connected to your Azure VNet that the private cluster is on i.e. if you are connected via ExpressRoute. I would recommend you plan to deploy your clusters as private and utilize this document right along the baseline document when designing your AKS architecture.

***LINK TO THE DOCUMENT:** [https://github.com/Azure/AKS-Landing-Zone-Accelerator/tree/main/Scenarios/AKS-Secure-Baseline-PrivateCluster](https://github.com/Azure/AKS-Landing-Zone-Accelerator/tree/main/Scenarios/AKS-Secure-Baseline-PrivateCluster)*

### AKS baseline for multi-region clusters

**What it is:**

This reference architecture details how to run multiple instances of an Azure Kubernetes Service (AKS) cluster across multiple regions in an active/active and highly available configuration.

**How to use it:**

If you need multi-region AKS clusters with greater high availability then this is a document you will want to look at to guide you with this. If you don’t need multi-region-based clusters skip this document.

*LINK TO THE DOCUMENT: [https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-multi-region/aks-multi-cluster](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-multi-region/aks-multi-cluster)*

### AKS regulated cluster for PCI

**What it is:**

Microsoft has built a 9-part series of articles to help when organizations need to run PCI workloads on AKS. Below are the first 3 of those articles as this is where you start. You will want to reference all 9 parts of the series though.

**Introduction of an AKS regulated cluster for PCI-DSS 3.2.1** – This reference architecture describes the considerations for an Azure Kubernetes Service (AKS) cluster designed to run a sensitive workload. The guidance is tied to the regulatory requirements of the Payment Card Industry Data Security Standard (PCI-DSS 3.2.1).

**Architecture of an AKS regulated cluster for PCI-DSS 3.2.1 –** This article describes a reference architecture for an Azure Kubernetes Service (AKS) cluster that runs a workload in compliance with the Payment Card Industry Data Security Standard (PCI-DSS 3.2.1). This architecture is focused on the infrastructure and not the PCI-DSS 3.2.1 workload.

**Configure networking of an AKS regulated cluster for PCI-DSS 3.2.1** – This article describes the networking considerations for an Azure Kubernetes Service (AKS) cluster that’s configured in accordance with the Payment Card Industry Data Security Standard (PCI-DSS 3.2.1).

**How to use it:**

If your organization plans to run any workloads that need PCI compliance on AKS then you will want to check out this document and utilize it when designing for your AKS clusters. It gets into topics such as TLS, DDoS protection, pop-to-pod security, and more.

***LINK TO THE DOCUMENT/s:***

***Introduction of an AKS regulated cluster for PCI-DSS 3.2.1** – [https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-pci/aks-pci-intro](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-pci/aks-pci-intro)*

**Architecture of an AKS regulated cluster for PCI-DSS 3.2.1 –** [https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-pci/aks-pci-ra-code-assets](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-pci/aks-pci-ra-code-assets)

**Configure networking of an AKS regulated cluster for PCI-DSS 3.2.1** – [https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-pci/aks-pci-network](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-pci/aks-pci-network)

### Advanced Azure Kubernetes Service (AKS) microservices architecture

**What it is:**

This reference architecture details several configurations to consider when running microservices on Azure Kubernetes Services. Topics include configuring network policies, pod autoscaling, and distributed tracing across a microservice-based application.

**How to use it:**

The chances are high that you will be running microservice-based workloads on your AKS cluster. Utilize this document in your design process to ensure your architecture is ready to handle microservices-based workloads. It also includes a Visio file to help you get started.

***LINK TO THE DOCUMENT:** [https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-microservices/aks-microservices-advanced](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-microservices/aks-microservices-advanced)*

# DEPLOY-

Part #2 is to deploy the architecture you designed. The best option for deploying Azure infrastructure and AKS clusters is to script it as IaC (Infrastructure as Code). Scripting the deployment vs manually deploying allows you to have documentation via code, standardization, and a templatized deployment for repeatability. You can take this code and place it in a pipeline for ease of deployment, in a service catalog for access to teams across your org, or as an inner source for use among DevOps teams.

Microsoft has built something called the AKS Landin Zone Accelerator as a starting point to use for building out your IaC for AKS. The idea is that you can utilize the Azure Kubernetes Service (AKS) Baseline documentation as a reference when designing your AKS and use the AKS Landing Zone Accelerator to deploy. Now your architecture should be based on the AKS baseline with some modifications to fit your specific needs. The AKS Landing Zone Accelerator may need to be modified to fit your specific needs as well. As long as your architecture is based on the AKS Baseline then you should not have to make a ton of modifications to the AKS Landing Zone Accelerator code. In fact, 80% or more of the work should be done for you already when utilizing the AKS Landing Zone Accelerator IaC code.

The AKS Landing Zone Accelerator contains IaC code for both bicep and terraform. It also has instructions on how to deploy the AKS Baseline using either of the two languages.

### AKS landing zone accelerator

**What it is:**

This solution provides an architectural approach and reference implementation to prepare landing zone subscriptions for a scalable Azure Kubernetes Service (AKS) cluster. The implementation adheres to the architecture and best practices of the Cloud Adoption Framework’s Azure landing zones with a focus on the design principles of enterprise-scale.

![](A%20Guide%20to%20Navigating%20the%20AKS%20Enterprise%20Documenta%2007d8c81551c442e7af4a23ce2ad57f8b/AKS-doc-guide-5.jpg)

A key point is that the Accelerator goes beyond just AKS and can be used to also deploy architecture that is in your Azure landing zone i.e. deployment of a hub and AKS deployed in a spoke. The Accelerator takes principles from the Azure CAF (Cloud Adoption Framework) helping with landing zone architecture if needed. The Accelerator takes a modular approach allowing you the flexibility to use what you need and skip what you don’t need or what you already have deployed.

**How to use it:**

The AKS landing zone accelerator is an accelerator based on the AKS baseline as well as an open-source collection of ARM, Bicep, and Terraform templates that can be used to deploy AKS clusters in an automated IaC way.

The Accelerator has 3 Deployment Models. These models are spread across three separate repositories that are based on the AKS Baseline and Azure Landing Zone. These are:

1. [https://github.com/Azure/AKS-Landing-Zone-Accelerator](https://github.com/Azure/AKS-Landing-Zone-Accelerator) (Step-by-step guidance on scenario-based deployments focused on the separation of duties, modularized IaC. i.e. private cluster, HA clusters, Blue/Green AKS, and more.)
2. https://github.com/Azure/Aks-Construction (Bicep based. Focused on expediting AKS deployment complete with a Wizard parameter config. Put configurations into the Wizard and it gives you the code to use for deployment. Check out the Wizard here: https://azure.github.io/AKS-Construction/.)
3. https://github.com/Azure/aks-baseline-automation (This one is focused on the separation of concerns and automating the deployment of the typical AKS components.)

Here is what the AKS Deploy Helper Wizard looks like:

![](A%20Guide%20to%20Navigating%20the%20AKS%20Enterprise%20Documenta%2007d8c81551c442e7af4a23ce2ad57f8b/AKS-doc-guide-6.jpg)

***LINK TO THE DOCUMENT:** [https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/app-platform/aks/landing-zone-accelerator](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/app-platform/aks/landing-zone-accelerator)*

# OPERATE-

Part #3 is to operate your AKS clusters. To assist with this Microsoft has two great documents to help. The first document has a list of operations you need to consider as you move into the management of your AKS cluster. The second document is a day-2 operation guide that you can reference to ensure you are not missing anything in regards to the ongoing operations of your AKS cluster. The day-2 operations cover the following:

Here are the links to both documents:

### Operations management considerations for Azure Kubernetes Service

***LINK TO THE DOCUMENT:** [https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/app-platform/aks/management](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/app-platform/aks/management)*

### Azure Kubernetes Services (AKS) day-2 operations guide

***LINK TO THE DOCUMENT:** [https://docs.microsoft.com/en-us/azure/architecture/operator-guides/aks/day-2-operations-guide](https://docs.microsoft.com/en-us/azure/architecture/operator-guides/aks/day-2-operations-guide)* Well that wraps up this post. My hope is that you found this blog post helpful and that you can use this guide to help navigate the AKS Enterprise Documentation. Stay tuned