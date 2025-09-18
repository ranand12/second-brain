# g-emarco/advanced-rag

Column: https://github.com/g-emarco/advanced-rag
Processed: No
created on: December 13, 2023 6:51 AM

# Advanced RAG

![](g-emarco%20advanced-rag%200ddb3a2688d84496b0b5f40aa4d4b5e6/ai21-adanved-rag.png)

## Tech Stack

**Client:** Streamlit

**Server Side:** LangChain 🦜🔗

**Vectorstore:** PGVector

**Embeddings:** GCP VertexAI

**LLMS:** PaLM 2, AI21 Contextual Answers

**Runtime:** Cloud Run

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`AI21_API_KEY`, `CONNECTION_STRING`

## Run Locally

Clone the project

```
  git clone https://github.com/g-emarco/advanced-rag.git
```

Go to the project directory

```
  cd advanced-rag
```

Install dependencies

```
  pipenv install
```

Start the Streamlit server

```
  streamlit run app.py
```

NOTE: When running locally make sure `GOOGLE_APPLICATION_CREDENTIALS` is set to a service account with permissions to use VertexAI

## Deployment to cloud run

CI/CD via Cloud build is availale in `cloudbuild.yaml`

Please replace $PROJECT_ID with your actual Google Cloud project ID.

To deploy manually:

1. Make sure you enable GCP APIs:

```
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable secretmanager.googleapis.com
gcloud services enable artifactregistry.googleapis.com
gcloud services enable vertexai.googleapis.com

```

1. Create a service account `rag-app-sa` with the following roles:

```
gcloud iam service-accounts create rag-app-sa \
    --display-name="SA For Application"

gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:rag-app-sa@PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/run.invoker"

gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:rag-app-sa@PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/serviceusage.serviceUsageConsumer"

gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:rag-app-sa@PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/ml.admin"

gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:rag-app-sa@PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/vertexai.admin"

```

1. Create the secrets:

`AI21_API_KEY`

and for each secret grant the SA `rag-app-sa@$PROJECT_ID.iam.gserviceaccount.com` Secret Manager Secret Accessor role to th secrets

1. Build Image

```
docker build . -t us-east1-docker.pkg.dev/$PROJECT_ID/app/documentation-assistant:latest
```

1. Push to Artifact Registry

```
docker push us-east1-docker.pkg.dev/$PROJECT_ID/app/documentation-assistant:latest
```

1. Deploy to cloud run

```
    --image=us-east1-docker.pkg.dev/PROJECT_ID/app/documentation-assistant:latest \
    --region=us-east1 \
    --service-account=rag-app-sa@$PROJECT_ID.iam.gserviceaccount.com \
    --allow-unauthenticated \
    --set-secrets="GOOGLE_API_KEY=projects/PROJECT_ID/secrets/AI21_API_KEY/versions/latest

```

## 🚀 About Me

Eden Marco, LLM Lead @ Google Cloud, Tel Aviv🇮🇱

[](g-emarco%20advanced-rag%200ddb3a2688d84496b0b5f40aa4d4b5e6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c696e6b6564696e2d3041363643323f7374796c653d666f722d7468652d6261646765266c6f676f3d6c696e6b6564696e266c6f676f436f6c6f723d7768697465)

[](g-emarco%20advanced-rag%200ddb3a2688d84496b0b5f40aa4d4b5e6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f747769747465722d3144413146323f7374796c653d666f722d7468652d6261646765266c6f676f3d74776974746572266c6f676f436f6c6f723d7768697465)