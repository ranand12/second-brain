# Workload identity on AKS with Python: boring – Cloudtrooper

Column: https://blog.cloudtrooper.net/2022/11/19/workload-identity-on-aks-with-python-boring/
Processed: No
created on: November 25, 2022 12:10 AM
topics: azure, tech-stuff

![image-13.png](Workload%20identity%20on%20AKS%20with%20Python%20boring%20%E2%80%93%20Clou%2079d7a948c0364be0af6dbd89626ab964/image-13.png)

I finally decided to carve out an afternoon to test workload identity on AKS. I had done some preliminary reading, and my conclusion was that there had to be some voodoo magic and quantum entanglement at play there to make it work, so I braced myself for failure.

The goal of the exercise was clear: first, configuring workload identity in an AKS cluster, and second, changing the code of the YADA (Yet Another Demo App) API ([https://github.com/Microsoft/YADA](https://github.com/Microsoft/YADA)) to make it work.

TL;DR: for the first step you can find plenty of docs and blog posts out there. The second step proved to be the best: no code changes required!

## Configuring workload identity

You have a couple of alternatives here, all of which should yield the same positive result. You can check the official AKS ([https://learn.microsoft.com/azure/aks/learn/tutorial-kubernetes-workload-identity](https://learn.microsoft.com/azure/aks/learn/tutorial-kubernetes-workload-identity)), you can follow the workload identity docs ([https://azure.github.io/azure-workload-identity/docs/installation.html](https://azure.github.io/azure-workload-identity/docs/installation.html)), or you can use your favorite search engine to find a blog of your liking.

Another option is using a predefined ARM, bicep or Terraform template. Huge kudos to my admired colleague [Felip Miguel Puig](https://github.com/felipmiguel) for his Terraform template to .NET and Java apps on AKS with workload identity: [https://github.com/felipmiguel/spring-petclinic-microservices/tree/feature/aks-passwordless](https://github.com/felipmiguel/spring-petclinic-microservices/tree/feature/aks-passwordless).

I followed the AKS docs instead of using the workload identity github.io (the latter deploys the required mutating admission webhook via helm). In any case, here you have the commands I used (you can find my whole script to deploy AKS with different options in [https://github.com/erjosito/azcli/blob/master/aks.azcli](https://github.com/erjosito/azcli/blob/master/aks.azcli)):

```
# Variables
workload_id_name=workloadidtest       # Name of the User-Assigned Managed Identity
federated_id_name=federatedid         # Name for the identity federation
sa_name=myserviceaccount
sa_namespace=default

# Enable workload identity and create identity
enableAksFeature EnableWorkloadIdentityPreview
echo "Enabling workload identity in cluster..."
az aks update -n $aks_name -g $rg --enable-oidc-issuer --enable-workload-identity true -o none
aks_oidc_issuer="$(az aks show -n $aks_name -g $rg --query "oidcIssuerProfile.issuerUrl" -o tsv)"
echo "Creating managed identity..."
az identity create -n $workload_id_name -g $rg -o none
workload_id_id="$(az identity show -n $workload_id_name -g $rg --query 'clientId' -o tsv)"
sleep 30  # Sometimes it takes some time to properly create the identity
az keyvault set-policy -n $akv_name --secret-permissions get --spn "${workload_id_id}" -o none

# Create service account
echo "Creating service account in AKS cluster..."
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: ServiceAccount
metadata:
  annotations:
azure.workload.identity/client-id: ${workload_id_id}
  labels:
azure.workload.identity/use: "true"
  name: $sa_name
  namespace: $sa_workspace
EOF

# Federate identities
echo "Federating managed identity and service account..."
az identity federated-credential create -n $federated_id_name --identity-name $workload_id_name -g $rg \
    --issuer ${aks_oidc_issuer} --subject "system:serviceaccount:${sa_namespace}:${sa_name}" -o none

```

If you are not using the AKS `--enable-workload-identity` setting, or you are not using AKS altogether, you can find in [https://azure.github.io/azure-workload-identity/docs/installation/mutating-admission-webhook.html](https://azure.github.io/azure-workload-identity/docs/installation/mutating-admission-webhook.html) how to deploy the mutating admission webhook with a helm chart. If you are using the AKS and enable workload identity in your cluster, you shouldn’t need to install any helm chart.

## Deploying the pod

Alright, now deploying the app. Looking at the example in the workload identity docs in github.io, you can see that only one additional setting in your YAML is required:

- You actually don’t need a label `azure.workload.identity/use` set to true, as the docs for the helm chart approach seem to suggest ([https://azure.github.io/azure-workload-identity/docs/quick-start.html#7-deploy-workload](https://azure.github.io/azure-workload-identity/docs/quick-start.html#7-deploy-workload))
- The spec property serviceAccountName set to the name of the service account that you federated to a user-defined managed identity to the installation.

So this is the YAML I deployed:

```
apiVersion: v1
kind: Pod
metadata:
  name: yadaapi
  labels:
    app: yadaapi
spec:
serviceAccountName: ${sa_name}
  containers:
    - image: erjosito/yadaapi:1.0
      name: yadaapi
      env:
      - name: SQL_SERVER_FQDN
        value: ${sql_server_fqdn}
      - name: SQL_SERVER_USERNAME
        value: ${sql_username}
      - name: AKV_NAME
        value: ${akv_name}
      - name: AKV_SECRET_NAME
        value: ${akv_secret_name}
  nodeSelector:
    kubernetes.io/os: linux

```

You wouldn’t need the environment variables for a basic test, but I deployed the YADA pod with those variables to test access to a backend database too.

You can verify at this point that the mutating admission controller injected additional variables into the pod with this command (assuming you have `kubectl` and `jq` in your system, which you definitely should):

```
kubectl get pod yadaapi -o json | jq -r '.spec.containers[0].env'
```

## Testing the app

Here is where I mentally prepared for another StackOverflow frenzy. The YADA API app (documentation [https://github.com/microsoft/YADA/blob/main/api/README.md](https://github.com/microsoft/YADA/blob/main/api/README.md)) offers an endpoint to extract a secret from an Azure Key Vault, so that is what I picked from my first test:

```
akv_name=name-of-your-azure-keyvault
akv_secret_name=name-of-a-secret-in-your-azure-keyvault
curl "http://${svc_ip}/api/akvsecret?akvname=${akv_name}&akvsecret=${akv_secret_name}
```

And it worked! No StackOverflow frenzy today! But why? Well, because of the magic of the Microsoft identity SDK. The app (a very simple Flask app, find the code in [https://github.com/microsoft/YADA/blob/main/api/sql_api.py](https://github.com/microsoft/YADA/blob/main/api/sql_api.py))is using the method `AzureDefaultCredential` from the Python module `azure.identity`.

```
from azure.identity import DefaultAzureCredential
```

Using this couldn’t be simpler:

```
azure_credential = DefaultAzureCredential()
akv_client = SecretClient(vault_url=akv_uri, credential=azure_credential)
akv_secret = akv_client.get_secret(akv_secret_name)
```

The original purpose of this code was authenticating using the legacy pod identity mechanism, which in turn leverages the Instance Meta Data Service to get a token. And as it turns out, when the right environment variables exist (injected by the mutating admission controller) exactly the same code works for workload identity!

## Adding up

In my opinion, “boring” is one of the best adjectives you can apply to a new technology: it does what it promises, it is easy to use, and it gives you no surprises. Welcome to workload identity in AKS.

### *Related*