# Auto-scaling + Kubernetes = KEDA — Part 2 | by Evgeny Grishchenko | Dev Genius

Column: https://blog.devgenius.io/auto-scaling-kubernetes-keda-part-2-72fb3fc21c27
Processed: No
created on: April 11, 2022 8:27 PM
topics: azure, kubernetes, tech-stuff

![](Auto-scaling%20+%20Kubernetes%20=%20KEDA%20%E2%80%94%20Part%202%20by%20Evgen%209d0bc88fe31049649c611b54d4dd65a4/1urJ_QDzPorqD9hgnxUfwnw.png)

*Prerequisites for this article — Kubernetes, Azure Function App, Docker knowledge*

In the [Part 1](https://medium.com/dev-genius/auto-scaling-kubernetes-keda-part-1-d7638d67ea17) I have explained the high level ideas of KEDA. In this part we will see the practical implementation.

**Use Case**

There is a web app, which uploads files from end users and puts them in a cloud storage. The goal is to process those files with the minimum delays. To do that we want the job to be scaled, based on the queue size.

**Components**

- Web App to get user inputs (files)
- Azure Blob Storage to keep files
- Kubernetes Cluster with KEDA (really, v 2.0)
- Azure Function App as a JOB, hosted in the Kubernetes Cluster, to process the files from the storage
- Container Registry to host your docker images

The implementation of the web app in this case does not matter. Let’s focus on the azure function app.

## You could use [this](https://github.com/egrish/sample-dotnet-worker-storage-queue) github repo to get all the details.

1. **Installation**

As soon as you have your Kubernetes cluster, you have to make sure that the KEDA is installed. This is very easy — just follow the official guidelines [here](https://keda.sh/docs/2.0/deploy/).

In the end you would have the Kubernetes namespace “keda” and a couple of deployments.

![](Auto-scaling%20+%20Kubernetes%20=%20KEDA%20%E2%80%94%20Part%202%20by%20Evgen%209d0bc88fe31049649c611b54d4dd65a4/1nIwBiOWQzDBfJp17zCw-dA.png)

**2. Job initiation**

The key reasons to select Azure Function App as an execution framework are:

- efficiency — you do not need to take care of coding queue iterations — peaking, reading,…;
- flexibility — you could run it as a docker container in your Kubernetes cluster or directly on Azure platform.

```
func init --worker-runtime dotnet --docker
func new -n Demo -l C#
```

Update the file Demo.cs to indicate where the connection string is stored (parameter **Connection**):

```
[FunctionName("Demo")]
        public static void Run([QueueTrigger("myqueue-items", Connection = "AzureWebJobsStorage")]string myQueueItem, ILogger log)
        {
            log.LogInformation($"C# Queue trigger function processed: {myQueueItem}");
        }
```

If you properly configure **local.settings.json**,and add a mesage into your queue “myqueue-items”, then you could test your function by launching it form the command line:

```
func start
```

**3. Preparing a docker image**

The docker image would be used to host the Azure function app, which we have created previously.

```
docker build -t <your registry name>/demo-keda .
```

“demo-keda” is the name of the image.

And oush it to the registry:

```
docker push <your registry name>/demo-keda:latest
```

**4. Preparing Kubernetes**

You could create your deployment file “deploy.yaml” for the namespace “demo” by the following command.

```
func kubernetes deploy --name demo-keda --namespace demo \
  --image-name <your registry name>/demo-keda:latest --dry-run > deploy.yaml
```

To deploy your job to your kubernetes cluster:

```
kubectl apply -f deploy.yaml
```

**Important**! if you use KEDA v.2.0, please, update the deployment file (the section “ScaledObject”:

```
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: demo-keda
  namespace: demo
spec:
  scaleTargetRef:
    name: demo-keda
  cooldownPeriod:  180
  minReplicaCount: 0
  maxReplicaCount: 2
  advanced:
    restoreToOriginalReplicaCount: true
  triggers:
  - type: azure-queue
    metadata:
      connectionFromEnv: AzureWebJobsStorage
      queueName: myqueue-items
      queueLength: '1'
```

**5. Testing and monitoring**

Initially, the number of active pods should 0 in your namespace “demo”.

If you launch the command, you could start monitoring the pods, which would be created by KEDA, if you start quickly adding messages to the queue:

```
kubectl get pods -w -n demo
```

**6. Troubleshooting**

If your job is not scaling, it makes sence to troubleshoot the KEDA.

For that, we need the logs from the pod “keda-operator-*”.

To find the required pod’s name to get the logs from:

```
kubectl get pods -n keda
```

To get the KEDA scaling logs:

```
kubectl logs <keda operator pod name> -n keda
```