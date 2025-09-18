# GitHub - GoogleCloudPlatform/microservices-demo: Sample cloud-native application with 10 microservices showcasing Kubernetes, Istio, gRPC and OpenCensus.

Column: https://github.com/GoogleCloudPlatform/microservices-demo
Processed: No
created on: August 24, 2022 5:51 PM
topics: Gcp, tech-stuff

![](GitHub%20-%20GoogleCloudPlatform%20microservices-demo%20Sa%2088303ba906294c67aa0d8717341dedd0/Hipster_HeroLogoCyan.svg)

![](GitHub%20-%20GoogleCloudPlatform%20microservices-demo%20Sa%2088303ba906294c67aa0d8717341dedd0/badge.svg)

**Online Boutique** is a cloud-first microservices demo application. Online Boutique consists of an 11-tier microservices application. The application is a web-based e-commerce app where users can browse items, add them to the cart, and purchase them.

**Google uses this application to demonstrate use of technologies like Kubernetes/GKE, Istio, Stackdriver, gRPC and OpenCensus**. This application works on any Kubernetes cluster, as well as Google Kubernetes Engine. It’s **easy to deploy with little to no configuration**.

If you’re using this demo, please **★Star** this repository to show your interest!

> 
> 
> 
> ![](GitHub%20-%20GoogleCloudPlatform%20microservices-demo%20Sa%2088303ba906294c67aa0d8717341dedd0/1f453.png)
> 
> **Note to Googlers:**
> 
> [go/microservices-demo](http://go/microservices-demo)
> 

## Screenshots

[Untitled](GitHub%20-%20GoogleCloudPlatform%20microservices-demo%20Sa%2088303ba906294c67aa0d8717341dedd0/Untitled%20a07d772d9c32485c888f2428dcd1a158.csv)

## Quickstart (GKE)

[](GitHub%20-%20GoogleCloudPlatform%20microservices-demo%20Sa%2088303ba906294c67aa0d8717341dedd0/68747470733a2f2f677374617469632e636f6d2f636c6f75647373682f696d616765732f6f70656e2d62746e2e737667)

1. [**Create a Google Cloud Platform project**](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project) or use an existing project. Set the `PROJECT_ID` environment variable and ensure the Google Kubernetes Engine and Cloud Operations APIs are enabled.

```
PROJECT_ID="<your-project-id>"
gcloud services enable container.googleapis.com --project ${PROJECT_ID}
gcloud services enable monitoring.googleapis.com \
 cloudtrace.googleapis.com \
 clouddebugger.googleapis.com \
 cloudprofiler.googleapis.com \
 --project ${PROJECT_ID}

```

1. **Clone this repository.**

```
git clone https://github.com/GoogleCloudPlatform/microservices-demo.git
cd microservices-demo

```

1. **Create a GKE cluster.**
- GKE autopilot mode (see [Autopilot overview](https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) to learn more):

```
REGION=us-central1
gcloud container clusters create-auto onlineboutique \
 --project=${PROJECT_ID} --region=${REGION}

```

- GKE Standard mode:

```
ZONE=us-central1-b
gcloud container clusters create onlineboutique \
 --project=${PROJECT_ID} --zone=${ZONE} \
 --machine-type=e2-standard-2 --num-nodes=4

```

1. **Deploy the sample app to the cluster.**

```
kubectl apply -f ./release/kubernetes-manifests.yaml

```

1. **Wait for the Pods to be ready.**

```
kubectl get pods

```

After a few minutes, you should see:

```
NAME READY STATUS RESTARTS AGE
adservice-76bdd69666-ckc5j 1/1 Running 0 2m58s
cartservice-66d497c6b7-dp5jr 1/1 Running 0 2m59s
checkoutservice-666c784bd6-4jd22 1/1 Running 0 3m1s
currencyservice-5d5d496984-4jmd7 1/1 Running 0 2m59s
emailservice-667457d9d6-75jcq 1/1 Running 0 3m2s
frontend-6b8d69b9fb-wjqdg 1/1 Running 0 3m1s
loadgenerator-665b5cd444-gwqdq 1/1 Running 0 3m
paymentservice-68596d6dd6-bf6bv 1/1 Running 0 3m
productcatalogservice-557d474574-888kr 1/1 Running 0 3m
recommendationservice-69c56b74d4-7z8r5 1/1 Running 0 3m1s
redis-cart-5f59546cdd-5jnqf 1/1 Running 0 2m58s
shippingservice-6ccc89f8fd-v686r 1/1 Running 0 2m58s

```

1. **Access the web frontend in a browser** using the frontend's `EXTERNAL_IP`.

```
kubectl get service frontend-external | awk '{print $4}'

```

*Example output - do not copy*

```
EXTERNAL-IP
<your-ip>

```

**Note**- you may see `<pending>` while GCP provisions the load balancer. If this happens, wait a few minutes and re-run the command.

1. [Optional] **Clean up**:

```
gcloud container clusters delete onlineboutique \
 --project=${PROJECT_ID} --zone=${ZONE}

```

## Other Deployment Options

- **Google Cloud Operations** (Monitoring, Tracing, Debugger, Profiler): [See these instructions](https://github.com/GoogleCloudPlatform/microservices-demo/blob/main/docs/gcp-instrumentation.md).
- **Workload Identity**: [See these instructions.](https://github.com/GoogleCloudPlatform/microservices-demo/blob/main/docs/workload-identity.md)
- **Istio**: [See these instructions.](https://github.com/GoogleCloudPlatform/microservices-demo/blob/main/docs/service-mesh.md)
- **Anthos Service Mesh**: ASM requires Workload Identity to be enabled in your GKE cluster. [See the workload identity instructions](https://github.com/GoogleCloudPlatform/microservices-demo/blob/main/docs/workload-identity.md) to configure and deploy the app. Then, use the [service mesh guide](https://github.com/GoogleCloudPlatform/microservices-demo/blob/main/docs/service-mesh.md).
- **non-GKE clusters (Minikube, Kind)**: see the [Development Guide](https://github.com/GoogleCloudPlatform/microservices-demo/blob/main/docs/development-guide.md)
- **Memorystore**: [See these instructions](https://github.com/GoogleCloudPlatform/microservices-demo/blob/main/docs/memorystore.md) to replace the in-cluster `redis` database with hosted Google Cloud Memorystore (redis).
- **Cymbal Shops Branding**: [See these instructions](https://github.com/GoogleCloudPlatform/microservices-demo/blob/main/docs/cymbal-shops.md)
- **NetworkPolicies**: [See these instructions](https://github.com/GoogleCloudPlatform/microservices-demo/blob/main/docs/network-policies/README.md)

## Architecture

**Online Boutique** is composed of 11 microservices written in different languages that talk to each other over gRPC. See the [Development Principles](https://github.com/GoogleCloudPlatform/microservices-demo/blob/main/docs/development-principles.md) doc for more information.

![](GitHub%20-%20GoogleCloudPlatform%20microservices-demo%20Sa%2088303ba906294c67aa0d8717341dedd0/architecture-diagram.png)

Find **Protocol Buffers Descriptions** at the [`./pb` directory](https://github.com/GoogleCloudPlatform/microservices-demo/blob/main/pb).

[Untitled](GitHub%20-%20GoogleCloudPlatform%20microservices-demo%20Sa%2088303ba906294c67aa0d8717341dedd0/Untitled%200c183e750585421bb2d4773a83743e1c.csv)

## Features

- [**Kubernetes](https://kubernetes.io/)/[GKE](https://cloud.google.com/kubernetes-engine/):** The app is designed to run on Kubernetes (both locally on "Docker for Desktop", as well as on the cloud with GKE).
- [**gRPC](https://grpc.io/):** Microservices use a high volume of gRPC calls to communicate to each other.
- [**Istio](https://istio.io/):** Application works on Istio service mesh.
- [**OpenCensus](https://opencensus.io/) Tracing:** Most services are instrumented using OpenCensus trace interceptors for gRPC/HTTP.
- [**Cloud Operations (Stackdriver)](https://cloud.google.com/products/operations):** Many services are instrumented with **Profiling**, **Tracing** and **Debugging**. In addition to these, using Istio enables features like Request/Response **Metrics** and **Context Graph** out of the box. When it is running out of Google Cloud, this code path remains inactive.
- [**Skaffold](https://skaffold.dev/):** Application is deployed to Kubernetes with a single command using Skaffold.
- **Synthetic Load Generation:** The application demo comes with a background job that creates realistic usage patterns on the website using [Locust](https://locust.io/) load generator.

## Local Development

If you would like to contribute features or fixes to this app, see the [Development Guide](https://github.com/GoogleCloudPlatform/microservices-demo/blob/main/docs/development-guide.md) on how to build this demo locally.

## Demos featuring Online Boutique

- [From edge to mesh: Exposing service mesh applications through GKE Ingress](https://cloud.google.com/architecture/exposing-service-mesh-apps-through-gke-ingress)
- [Take the first step toward SRE with Cloud Operations Sandbox](https://cloud.google.com/blog/products/operations/on-the-road-to-sre-with-cloud-operations-sandbox)
- [Deploying the Online Boutique sample application on Anthos Service Mesh](https://cloud.google.com/service-mesh/docs/onlineboutique-install-kpt)
- [Anthos Service Mesh Workshop: Lab Guide](https://codelabs.developers.google.com/codelabs/anthos-service-mesh-workshop)
- [KubeCon EU 2019 - Reinventing Networking: A Deep Dive into Istio's Multicluster Gateways - Steve Dake, Independent](https://youtu.be/-t2BfT59zJA?t=982)
- Google Cloud Next'18 SF
    - [Day 1 Keynote](https://youtu.be/vJ9OaAqfxo4?t=2416) showing GKE On-Prem
    - [Day 3 Keynote](https://youtu.be/JQPOPV_VH5w?t=815) showing Stackdriver APM (Tracing, Code Search, Profiler, Google Cloud Build)
    - [Introduction to Service Management with Istio](https://www.youtube.com/watch?v=wCJrdKdD6UM&feature=youtu.be&t=586)
- [Google Cloud Next'18 London – Keynote](https://youtu.be/nIq2pkNcfEI?t=3071) showing Stackdriver Incident Response Management

This is not an official Google project.