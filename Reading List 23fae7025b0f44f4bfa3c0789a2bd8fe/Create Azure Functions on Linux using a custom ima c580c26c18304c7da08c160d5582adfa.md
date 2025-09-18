# Create Azure Functions on Linux using a custom image | Microsoft Docs

Column: https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-function-linux-custom-image?tabs=in-process%2Cbash%2Cazure-cli&pivots=programming-language-python
Processed: No
created on: April 11, 2022 8:33 PM
topics: azure, tech-stuff

In this tutorial, you create and deploy your code to Azure Functions as a custom Docker container using a Linux base image. You typically use a custom image when your functions require a specific language version or have a specific dependency or configuration that isn't provided by the built-in image.

Deploying your function code in a custom Linux container requires [Premium plan](https://docs.microsoft.com/en-us/azure/azure-functions/functions-premium-plan) or a [Dedicated (App Service) plan](https://docs.microsoft.com/en-us/azure/azure-functions/dedicated-plan) hosting. Completing this tutorial incurs costs of a few US dollars in your Azure account, which you can minimize by [cleaning-up resources](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-function-linux-custom-image?tabs=in-process%2Cbash%2Cazure-cli&pivots=programming-language-python#clean-up-resources) when you're done.

You can also use a default Azure App Service container as described on [Create your first function hosted on Linux](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-csharp?pivots=programming-language-python). Supported base images for Azure Functions are found in the [Azure Functions base images repo](https://hub.docker.com/_/microsoft-azure-functions-base).

In this tutorial, you learn how to:

- Create a function app and Dockerfile using the Azure Functions Core Tools.
- Build a custom image using Docker.
- Publish a custom image to a container registry.
- Create supporting resources in Azure for the function app
- Deploy a function app from Docker Hub.
- Add application settings to the function app.
- Enable continuous deployment.
- Enable SSH connections to the container.
- Add a Queue storage output binding.

You can follow this tutorial on any computer running Windows, macOS, or Linux.

## Configure your local environment

Before you begin, you must have the following:

You also need an Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/free/?ref=microsoft.com&utm_source=microsoft.com&utm_medium=docs&utm_campaign=visualstudio).

## Create and test the local functions project

The `--docker` option generates a `Dockerfile` for the project, which defines a suitable custom container for use with Azure Functions and the selected runtime.

To test the function locally, start the local Azure Functions runtime host in the root of the project folder:

Once you see the `HttpExample` endpoint appear in the output, navigate to `http://localhost:7071/api/HttpExample?name=Functions`. The browser should display a "hello" message that echoes back `Functions`, the value supplied to the `name` query parameter.

Use **Ctrl**-**C** to stop the host.

## Build the container image and test locally

In the root project folder, run the [docker build](https://docs.docker.com/engine/reference/commandline/build/) command, and provide a name, `azurefunctionsimage`, and tag, `v1.0.0`. Replace `<DOCKER_ID>` with your Docker Hub account ID. This command builds the Docker image for the container.

```
docker build --tag <DOCKER_ID>/azurefunctionsimage:v1.0.0 .

```

When the command completes, you can run the new container locally.

To test the build, run the image in a local container using the [docker run](https://docs.docker.com/engine/reference/commandline/run/) command, replacing again `<DOCKER_ID` with your Docker ID and adding the ports argument, `-p 8080:80`:

```
docker run -p 8080:80 -it <docker_id>/azurefunctionsimage:v1.0.0

```

After you've verified the function app in the container, stop docker with **Ctrl**+**C**.

## Push the image to Docker Hub

Docker Hub is a container registry that hosts images and provides image and container services. To share your image, which includes deploying to Azure, you must push it to a registry.

1. Depending on your network speed, pushing the image the first time might take a few minutes (pushing subsequent changes is much faster). While you're waiting, you can proceed to the next section and create Azure resources in another terminal.

## Create supporting Azure resources for your function

Before you can deploy your function code to Azure, you need to create three resources:

- A [resource group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview), which is a logical container for related resources.
- A [Storage account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create), which is used to maintain state and other information about your functions.
- A function app, which provides the environment for executing your function code. A function app maps to your local function project and lets you group functions as a logical unit for easier management, deployment, and sharing of resources.

Use the following commands to create these items. Both Azure CLI and PowerShell are supported.

1. If you haven't done so already, sign in to Azure:
2. Create a resource group named `AzureFunctionsContainers-rg` in your chosen region:  
    
    ```
    az group create --name AzureFunctionsContainers-rg --location <REGION>
    
    ```
    
    The [az group create](https://docs.microsoft.com/en-us/cli/azure/group#az-group-create) command creates a resource group. In the above command, replace `<REGION>` with a region near you, using an available region code returned from the [az account list-locations](https://docs.microsoft.com/en-us/cli/azure/account#az-account-list-locations) command.
    
3. Create a general-purpose storage account in your resource group and region: 
    
    In the previous example, replace `<STORAGE_NAME>` with a name that is appropriate to you and unique in Azure Storage. Names must contain three to 24 characters numbers and lowercase letters only. `Standard_LRS` specifies a general-purpose account, which is [supported by Functions](https://docs.microsoft.com/en-us/azure/azure-functions/storage-considerations#storage-account-requirements).
    
4. Use the command to create a Premium plan for Azure Functions named `myPremiumPlan` in the **Elastic Premium 1** pricing tier (`-sku EP1`), in your `<REGION>`, and in a Linux container (`-is-linux`).  
    
    We use the Premium plan here, which can scale as needed. To learn more about hosting, see [Azure Functions hosting plans comparison](https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale). To calculate costs, see the [Functions pricing page](https://azure.microsoft.com/pricing/details/functions/).
    
    The command also provisions an associated Azure Application Insights instance in the same resource group, with which you can monitor your function app and view logs. For more information, see [Monitor Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-monitoring). The instance incurs no costs until you activate it.
    

## Create and configure a function app on Azure with the image

A function app on Azure manages the execution of your functions in your hosting plan. In this section, you use the Azure resources from the previous section to create a function app from an image on Docker Hub and configure it with a connection string to Azure Storage.

1. Create a functions app using the following command:   
    
    ```
    az functionapp create --name <APP_NAME> --storage-account <STORAGE_NAME> --resource-group AzureFunctionsContainers-rg --plan myPremiumPlan --deployment-container-image-name <DOCKER_ID>/azurefunctionsimage:v1.0.0
    
    ```
    
    In the [az functionapp create](https://docs.microsoft.com/en-us/cli/azure/functionapp#az-functionapp-create) command, the *deployment-container-image-name* parameter specifies the image to use for the function app. You can use the [az functionapp config container show](https://docs.microsoft.com/en-us/cli/azure/functionapp/config/container#az-functionapp-config-container-show) command to view information about the image used for deployment. You can also use the [az functionapp config container set](https://docs.microsoft.com/en-us/cli/azure/functionapp/config/container#az-functionapp-config-container-set) command to deploy from a different image. NOTE: If you are using a custom container registry then the *deployment-container-image-name* parameter will refer to the registry URL.
    
    In this example, replace `<STORAGE_NAME>` with the name you used in the previous section for the storage account. Also replace `<APP_NAME>` with a globally unique name appropriate to you, and `<DOCKER_ID>` with your DockerHub ID. When deploying from a custom container registry, use the `deployment-container-image-name` parameter to indicate the URL of the registry.
    
2. Use the following command to get the connection string for the storage account you created: 
    
    Replace `<STORAGE_NAME>` with the name of the storage account you created previously.
    
3. Add this setting to the function app by using the following command: 
    
    In this command, replace `<APP_NAME>` with the name of your function app and `<CONNECTION_STRING>` with the connection string from the previous step. The connection should be a long encoded string that begins with `DefaultEndpointProtocol=`.
    
4. The function can now use this connection string to access the storage account.

## Verify your functions on Azure

With the image deployed to your function app in Azure, you can now invoke the function as before through HTTP requests. In your browser, navigate to a URL like the following:

Replace `<APP_NAME>` with the name of your function app. When you navigate to this URL, the browser should display similar output as when you ran the function locally.

## Enable continuous deployment to Azure

You can enable Azure Functions to automatically update your deployment of an image whenever you update the image in the registry.

1. Enable continuous deployment and get the webhook URL by using the following commands:   
    
    ```
    az functionapp deployment container config --enable-cd --query CI_CD_URL --output tsv --name <APP_NAME> --resource-group AzureFunctionsContainers-rg
    
    ```
    
    The [az functionapp deployment container config](https://docs.microsoft.com/en-us/cli/azure/functionapp/deployment/container#az-functionapp-deployment-container-config) command enables continuous deployment and returns the deployment webhook URL. You can retrieve this URL at any later time by using the [az functionapp deployment container show-cd-url](https://docs.microsoft.com/en-us/cli/azure/functionapp/deployment/container#az-functionapp-deployment-container-show-cd-url) command.
    
    As before, replace `<APP_NAME>` with your function app name.
    
2. Copy the deployment webhook URL to the clipboard.
3. Open [Docker Hub](https://hub.docker.com/), sign in, and select **Repositories** on the nav bar. Locate and select image, select the **Webhooks** tab, specify a **Webhook name**, paste your URL in **Webhook URL**, and then select **Create**: 
    
    ![](Create%20Azure%20Functions%20on%20Linux%20using%20a%20custom%20ima%20c580c26c18304c7da08c160d5582adfa/dockerhub-set-continuous-webhook.png)
    
    With the webhook set, Azure Functions redeploys your image whenever you update it in Docker Hub.
    

## Enable SSH connections

SSH enables secure communication between a container and a client. With SSH enabled, you can connect to your container using App Service Advanced Tools (Kudu). To make it easy to connect to your container using SSH, Azure Functions provides a base image that has SSH already enabled. You need only edit your Dockerfile, then rebuild and redeploy the image. You can then connect to the container through the Advanced Tools (Kudu)

1. Rebuild the image by using the `docker build` command again, replacing `<docker_id>` with your Docker ID: 
    
    ```
    docker build --tag <docker_id>/azurefunctionsimage:v1.0.0 .
    
    ```
    
2. Push the updated image to Docker Hub, which should take considerably less time than the first push only the updated segments of the image need to be uploaded. 
    
    ```
    docker push <docker_id>/azurefunctionsimage:v1.0.0
    
    ```
    
3. Azure Functions automatically redeploys the image to your functions app; the process takes place in less than a minute.
4. In a browser, open `https://<app_name>.scm.azurewebsites.net/`, replacing `<app_name>` with your unique name. This URL is the Advanced Tools (Kudu) endpoint for your function app container.
5. Sign in to your Azure account, and then select the **SSH** to establish a connection with the container. Connecting may take a few moments if Azure is still updating the container image.
6. After a connection is established with your container, run the `top` command to view the currently running processes. 
    
    ![](Create%20Azure%20Functions%20on%20Linux%20using%20a%20custom%20ima%20c580c26c18304c7da08c160d5582adfa/linux-custom-kudu-ssh-top.png)
    

## Clean up resources

If you want to continue working with Azure Function using the resources you created in this tutorial, you can leave all those resources in place. Because you created a Premium Plan for Azure Functions, you'll incur one or two USD per day in ongoing costs.

To avoid ongoing costs, delete the `AzureFunctionsContainer-rg` resource group to clean up all the resources in that group:

```
az group delete --name AzureFunctionsContainer-rg

```

## Next steps

- [Monitoring functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-monitoring)
- [Scale and hosting options](https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale)