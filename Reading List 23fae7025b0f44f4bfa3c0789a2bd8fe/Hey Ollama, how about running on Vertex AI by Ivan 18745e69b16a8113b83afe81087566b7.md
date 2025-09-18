# Hey Ollama, how about running on Vertex AI? | by Ivan Nardini | Google Cloud - Community | Jan, 2025 | Medium

Column: https://medium.com/google-cloud/hey-ollama-how-about-running-on-vertex-ai-03cded7bfd0b
Processed: Yes
created on: January 26, 2025 7:17 AM

# Hey Ollama, how about running on Vertex AI?

![](https://miro.medium.com/v2/resize:fill:44:44/1*Wa96gcJRAH1sTcSqnhBGVg.png)

![](https://miro.medium.com/v2/resize:fill:24:24/1*FUjLiCANvATKeaJEeg20Rw.png)

[Ivan Nardini](https://medium.com/@ilnardo92?source=post_page---byline--03cded7bfd0b--------------------------------)

·

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F86600de286f3&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fgoogle-cloud%2Fhey-ollama-how-about-running-on-vertex-ai-03cded7bfd0b&user=Ivan+Nardini&userId=86600de286f3&source=post_page-86600de286f3--byline--03cded7bfd0b---------------------post_header-----------)

Published in

[Google Cloud - Community](https://medium.com/google-cloud?source=post_page---byline--03cded7bfd0b--------------------------------)

·

9 min read

·

4 days ago

- -

[](https://miro.medium.com/v2/resize:fit:700/0*YnBB84_P4BSF1Vlf)

# TL;DR

*Are you looking to scale an Ollama model on Cloud? This post walks you through deploying a Gemma 2 SQL adapter using Ollama on Vertex AI, showing a possible transition from local experimentation to scalable cloud deployment.*

# Introduction

Ollama is a fantastic open-source tool for running LLMs locally. Its user-friendly interface provides an easy way to experiment with and customize LLMs, putting you in complete control. But when I started using Ollama, I immediately wondered: how can I scale this in the cloud without losing that local development experience?

Then I remembered that with Vertex AI, you can build and serve your model locally, exactly as it would run on Vertex AI Prediction. This lets you iterate quickly and maintain control while easily transitioning to the cloud when you’re ready to scale. Unfortunately, I couldn’t find any resources on how to connect Ollama with Vertex AI. So, I decided to share my own journey!

This article shows you how to deploy a Gemma 2 SQL adapter using Ollama on Vertex AI, covering everything from containerization and local testing to cloud deployment and prediction.

Let’s get started!

# Get Gemma 2 ready for deployment with Vertex AI and Ollama

To deploy Gemma 2 as an Ollama model on Vertex AI Prediction, you can create a custom container that includes both the Ollama server and the Gemma 2 model. In this scenario, you use the *gemma-2–2b-it-lora-sql* adapter model from Hugging Face Hub, a Gemma 2 adapter specifically designed to handle SQL user requests. Below you have the code snippet that efficiently downloads the *gemma-2–2b-it-lora-sql* model from Hugging Face Hub using *huggingface_hub* library and stores it in a local directory, ready for containerization and deployment on Vertex AI.

```
base_model_id = "google-cloud-partnership/gemma-2-2b-it-lora-sql"
model_dir = "./gemma-2-2b-it-lora-sql"

ignore_patterns = [".gitattributes", ".gitkeep", "*.md"]

snapshot_download(
    repo_id=base_model_id,
    token=get_token(),
    local_dir=model_dir,
    local_dir_use_symlinks=False,
    ignore_patterns=ignore_patterns,
)
```

To build your container image, you can use Cloud Build, a fully managed CI/CD platform on Google Cloud. First, you’ll need to set up an Artifact Registry repository to store our container image. Artifact Registry acts as your private and secure docker container image registry in the cloud. Below you have the code to set up your Artifact Registry repository, creating a docker space to store and manage your Ollama container images.

```
PROJECT_ID = 'ollama-on-vertexai'
LOCATION = 'us-central1'
REPOSITORY_NAME = 'ollama-gemma-on-vertexai'

gcloud artifacts repositories create $REPOSITORY_NAME \
      --repository-format=docker \
      --location=$LOCATION \
      --project=$PROJECT_ID
```

Then, you define the Dockerfile to outline the steps to build our container image. Here you have an example of Dockerfile you may have.

```
# Use multi-stage build for a smaller final image
FROM ollama/ollama

# Install Python and FastAPI
RUN apt-get update && \
    apt-get install -y python3 python3-pip curl && \
    pip3 install fastapi uvicorn httpx

# Set build-time arguments for better flexibility
ARG OLLAMA_PORT=8079
ARG SERVING_PORT=8080

# Set environment variables
ENV OLLAMA_HOST=0.0.0.0:{OLLAMA_PORT} \ OLLAMA_MODELS=/ollama_models \ OLLAMA_KEEP_ALIVE=-1 \ OLLAMA_DEBUG=true # Copy model files COPY ./ollama_models /ollama_models COPY gemma-2-2b-it-lora-sql.modelfile . # Expose ollama port EXPOSE
{OLLAMA_PORT}

# Create model in a proper way with health check
RUN ollama serve & \
    sleep 5 && ollama create gemma-2-2b-it-lora-sql-2b -f gemma-2-2b-it-lora-sql.modelfile

# Expose port
EXPOSE ${SERVING_PORT}

# Copy the proxy server code and entrypoint script
COPY main.py .
COPY entrypoint.sh .

# Run the proxy server
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
```

Along the process to build the serving container, you install essential libraries like Python and FastAPI, set up environment variables, copy Ollama modelfile (*gemma-2–2b-it-lora-sql.modelfile*) to build the model, expose the necessary ports, copy the FastAPI serve engine proxy with its entrypoint (*main.py, entrypoint.sh*) and finally, launch the serve engine.

The Ollama modelfile is a declarative way to create models with Ollama. In this scenario, we use it to specify the *gemma-2–2b-it-lora-sql* as a fine tuned LoRA adapter to apply to the Gemma 2 base model. Here you have the content of the *gemma-2–2b-it-lora-sql.modelfile.*

```
FROM gemma2:2b
ADAPTER ollama_models/gemma-2-2b-it-lora-sql
```

While Ollama provides a robust framework for managing and serving LLMs, Vertex AI Prediction requires an HTTP server which functions as a proxy in this case of Ollama engine that serves the model. You can implement the HTTP server in any way, using any programming language, as long as it meets the Vertex AI Prediction requirements.

In the *main.py* module below you have a simple example of how to implement the HTTP server to run Gemma 2 model adapter using Ollama on Vertex AI Prediction.

```
''
FastAPI proxy for Vertex AI Endpoint running Ollama.
'''

import os
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
import httpx
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
import asyncio

# Configuration
class PredictionRequest(BaseModel):
    ...
class PredictionResponse(BaseModel):
    ...
class Config:
    ...

# Helper function
async def ollama_generate(prompt: str, parameters: Dict['str', Any]) -> str:
    '''
    Make a prediction using the Ollama model.
    '''
    async with httpx.AsyncClient(timeout=Config.TIMEOUT) as client:
        try:
            response = await client.post(
                f"{Config.OLLAMA_URL}/api/generate",
                json={
                    "prompt": prompt,
                    "stream": CONFIG.STREAM
                    "options": parameters,
                    "model": Config.MODEL_NAME
                }
            )
            response.raise_for_status()
            return response.json()["response"]

        except httpx.HTTPError as e:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail=f"Error calling Ollama: {str(e)}"
            )
# Application
app = FastAPI(
    title="Ollama Vertex AI Proxy",
    description="A proxy service to run Ollama models on Vertex AI"
)

@app.get(
    Config.HEALTH_ROUTE,
    response_model=Dict[str, str],
    description="Health check endpoint",
)
async def health() -> Dict[str, str]:
    '''Check if the service is healthy.'''
    return {'status': 'healthy'}

@app.post(
    Config.PREDICT_ROUTE,
    response_model=PredictionResponse,
    description="Make predictions using the Ollama model",
)
async def predict(request: PredictionRequest) -> PredictionResponse:
    '''Process predictions using the Ollama model concurrently.'''

    if not request.instances:
        raise HTTPException(...)

    try:
        # Process all prompts concurrently
        tasks = []
        for instance in request.instances:
            prompt = instance.get('inputs', '')
            parameters = instance.get('parameters', {})
            tasks.append(call_ollama(prompt, parameters))

        # Wait for all requests to complete
        predictions = await asyncio.gather(*tasks)
        return PredictionResponse(predictions=predictions)

    except Exception as e:
        raise HTTPException(...)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=Config.PORT
    )
```

This code sets up a FastAPI application to act as a streamlined proxy for the Ollama model. It defines two endpoints:

- */health* for checking the service’s status
- */predict* for generating predictions.

The */predict* endpoint leverages the *ollama_generate* function, which uses the *httpx* library for making asynchronous HTTP requests to the Ollama server, ensuring efficient and non-blocking communication. Notice how this code only proxies the *generate* API of Ollama. While this helps keep the code simple, you can easily extend this proxy to interact with other Ollama APIs. This allows you to create a more comprehensive interface for managing and interacting with your LLMs.

At this point, you have the Ollama model and the FastAPI proxy ready to go. Since you’re running both of these within the same container, you still need a way to manage their startup sequence. This *entrypoint* script takes care of that, ensuring everything starts up in the correct order:

```
#!/bin/bash

# Enable error handling
set -e

# Function to log messages with timestamps
log() {
    echo "[
1"
}

# Function to check if Ollama is ready
check_ollama() {
    for i in {1..30}; do
        if curl -s http://localhost:8079 >/dev/null; then
            log "✅ Ollama is ready!"
            return 0
        fi
        log "⏳ Waiting for Ollama to start... ($i/30)"
        sleep 1
    done
    log "❌ Ollama failed to start within 30 seconds"
    return 1
}

# Start Ollama in the background
log "🚀 Starting Ollama..."
ollama serve & sleep 5

# Wait for Ollama to be ready
check_ollama

# Start the FastAPI serving application
log "🚀 Starting FastAPI serving application..."
exec python3 /main.py
```

It first launches Ollama in the background, then checks its health to make sure it’s ready to go. Once Ollama gets the green check, the script fires up our FastAPI application, which takes over as the main interface for interacting with our Ollama model.

With the *entrypoint*, you can now build your serving image using Cloud Build as shown below.

```
SERVING_CONTAINER_IMAGE_URI = f"{LOCATION}-docker.pkg.dev/{PROJECT_ID}/{REPOSITORY_NAME}/ollama-gemma-2-serve"
BUILD_DIR = "./build"

! gcloud builds submit --tag $SERVING_CONTAINER_IMAGE_URI --project $PROJECT_ID --machine-type e2-highcpu-32 $BUILD_DIR
```

And here you have the resulting serving image in the Artifact Registry on Google Cloud.

Now, you might be wondering: can I run this serving container on my local machine? That’s where the Vertex AI *LocalModel* and *LocalEndpoint* classes come in handy.

# Local LLM Testing with Vertex AI

Available through the Vertex AI SDK for Python, Vertex AI *LocalModel* and *LocalEndpoint* classes let you build and serve your LLM locally, providing the deployment experience that mirrors an endpoint on Vertex AI Prediction.

To deploy your model locally, you use the *LocalModel* class and point it to your container image you just built. Here’s how you do it:

```
from google.cloud.aiplatform.prediction import LocalModel

local_ollama_gemma_model = LocalModel(
    serving_container_image_uri=SERVING_CONTAINER_IMAGE_URI,
    serving_container_ports=[8080],
)
```

Then, you deploy the model to a local endpoint, ready for serving. The *gpu_device_ids* parameter allows you to specify which GPUs to use, if available.

```
local_ollama_gemma_endpoint = local_ollama_gemma_model.deploy_to_local_endpoint(
    gpu_device_ids=get_cuda_device_names()
)

local_ollama_gemma_endpoint.serve()
```

To keep an eye on your deployment, you can use docker container ls -a to check the container’s status. For a more detailed view, use docker logs — follow *<CONTAINER_ID>* (replace *<CONTAINER_ID>* with the actual container ID) to stream the logs and see exactly what’s happening during deployment. This helps you catch any issues early on and ensures a smooth deployment process.

After your model gets deployed, you can test it out by sending a prediction request to the local endpoint. Simply convert your request data into a JSON string and send it over. You’ll receive a JSON response containing the predictions as shown below.

```
import json

prediction_request = {
    "instances": [{"inputs": "Tell me a funny joke!", "parameters": {"temperature": 1}}]
}

vertex_prediction_request = json.dumps(prediction_request)
vertex_prediction_response = local_ollama_gemma_endpoint.predict(
    request=vertex_prediction_request, headers={"Content-Type": "application/json"}
)
print(vertex_prediction_response.json()["predictions"])

#```sql SELECT * FROM tables;```
# This SQL statement selects all records from the table.
```

If your local deployment is working as expected, you’re ready to move to Vertex AI.

# Deploy Gemma 2 using Ollama on Vertex AI Prediction

Start by importing your model into Vertex AI Model Registry, a centralized repository for managing your ML models throughout their lifecycle. The *Model.upload* method in the Vertex AI SDK library provides a straightforward way to accomplish this.

```
model = Model.upload(
    display_name="google--gemma-2-2b-it-lora-sql-ollama",
    serving_container_image_uri=SERVING_CONTAINER_IMAGE_URI,
    serving_container_ports=[8080],
)
model.wait()
```

The *serving_container_image_uri* parameter specifies the location of your Ollama container image in Artifact Registry, while *serving_container_ports* defines the port where your Vertex AI endpoint will be exposed (the default is 8080).

After registering the model, you can deploy it to a Vertex AI endpoint using *Model.deploy* method. This serves the model on a scalable endpoint for generating predictions.

```
endpoint = Endpoint.create(
    display_name="google--gemma-2-2b-it-lora-sql-ollama-endpoint"
)

deployed_model = model.deploy(
    endpoint=endpoint,
    machine_type="g2-standard-4",
    accelerator_type="NVIDIA_L4",
    accelerator_count=1,
)
```

With the model deployed, you’re ready to generate predictions! Use the *Endpoint.predict* method to send requests to your deployed model as shown below.

```
output = deployed_model.predict(
    instances=[
        {
            "inputs": "How to run a select all query",
            "parameters": {
                "temperature": 1.0,
            },
        },
    ]
)
predictions = output.predictions
print(predictions[0])

# ```sql\nSELECT * FROM sales_data;```\n\nThis query selects all records from the 'sales_data' table. It uses the '*' wildcard character
```

# Conclusion

Hey Ollama, look, we get it! This blog post demonstrated how to deploy a Gemma 2 SQL adapter using Ollama on Vertex AI, covering everything from containerization and local testing to cloud deployment and prediction. By combining Ollama’s user-friendly interface with Vertex AI, developers can manage and scale their LLM applications. And the approach described in this blog allows for a coherent workflow, bridging the gap between local development and production-ready deployments. Now it’s your turn — what will you build?

# What’s next

Explore these resources to learn more about Ollama and Vertex AI Prediction

## Documentation

- [Ollama documentation](https://github.com/ollama/ollama/tree/main/docs)
- [Custom container requirements for prediction](https://cloud.google.com/vertex-ai/docs/predictions/custom-container-requirements)
- [Package prediction](https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.prediction)

## GitHub examples

- [Running a Gemma 2-based agentic RAG with Ollama on Vertex AI and LangGraph](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/open-models/serving/vertex_ai_ollama_gemma2_rag_agent.ipynb)

# Thanks for reading

I hope you enjoyed the article. If so, 𝗙𝗼𝗹𝗹𝗼𝘄 𝗺𝗲, 👏 this article or leave comments. Also let’s connect on [LinkedIn](https://www.linkedin.com/in/ivan-nardini/) or [X](https://twitter.com/IlNardo92) to share feedback and questions 🤗 about Vertex AI you would like to find an answer.