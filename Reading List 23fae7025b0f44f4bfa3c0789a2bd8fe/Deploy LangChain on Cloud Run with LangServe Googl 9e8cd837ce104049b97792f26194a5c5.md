# Deploy LangChain on Cloud Run with LangServe | Google Cloud Blog

Column: https://cloud.google.com/blog/products/ai-machine-learning/deploy-langchain-on-cloud-run-with-langserve
Processed: No
created on: November 29, 2023 6:54 PM

![DO_NOT_USE_IShqnxc.max-2500x2500.jpg](Deploy%20LangChain%20on%20Cloud%20Run%20with%20LangServe%20Googl%209e8cd837ce104049b97792f26194a5c5/DO_NOT_USE_IShqnxc.max-2500x2500.jpg)

[Register](https://cloud.withgoogle.com/next?utm_source=cgc-blog&utm_medium=blog&utm_campaign=FY24-Q2-global-ENDM33-physicalevent-er-next-2024-mc&utm_content=left-hand-rail-blog-cta&utm_term=-)

[LangChain](https://www.langchain.com/) is a popular framework that makes it easy to build apps that use large language models (LLMs). LangChain recently introduced LangServe, a way to deploy any LangChain project as a REST API. LangServe supports deploying to both Cloud Run and Replit.

I asked Nuno Campos, one of the founding engineers at LangChain, why they chose Cloud Run. He said:

*“We researched alternatives, and Cloud Run is the easiest and fastest way to get your app running in production."*

In this blog, I’ll show you how to get started with LangServe and deploy a template to Cloud Run that calls the [VertexAI PaLM 2 for chat model](https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/text-chat).

## **Generative AI apps explained**

Generative AI chatbots such as Google Bard are powered by large language models (LLMs). Generally speaking, you prompt an LLM with some text and it’ll complete the prompt. While you can describe an LLM as an advanced auto-complete, that’s an oversimplified way of thinking about it. LLMs can write code, rephrase text, generate recommendations, and solve simple logic problems.

You can also send prompts to an LLM from your code, which can be very useful once you start integrating with your own private data and APIs. Some popular use cases include:

- Asking questions over your own data (including manuals, support cases, product data)
- Interacting with APIs using natural language, letting the LLM make API calls for you
- Summarizing documents
- Data labeling or text extraction

Building these integrations often involve building pipelines (typically referred to as chains), starting with a prompt, and bringing your own data into the prompt. That’s where [LangChain](https://github.com/langchain-ai/langchain) comes in. Approaching 70k stars on GitHub, LangChain is by far the most popular framework for building LLM-powered apps.

## **Build chains with LangChain**

LangChain provides all the abstractions you need to start building an LLM app, and it comes with many [components](https://js.langchain.com/docs/integrations/components) out of the box, including LLMs, document loaders, text embedding models, vector stores, agents and tools. I’m glad to see many [Google products that have an integration with LangChain](https://python.langchain.com/docs/integrations/platforms/google). Some highlights include Vertex AI Vector Search (previously known as Matching Engine), and hundreds of open source LLM models through Vertex AI Model Garden.

Here’s how you can use LangChain to call the [VertexAI PaLM 2 for chat model](https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/text-chat) and ask it to tell jokes about Chuck Norris:

lang-py

<div _="@=696,dis=none"><div _="@=697,dis=none"></div></div>

```
from langchain.chat_models import ChatVertexAI
```

```
from langchain.prompts import ChatPromptTemplate
```

```
_prompt = ChatPromptTemplate.from_template(
```

```
    "Tell me a joke about Chuck Norris and {text}")
```

```
_model = ChatVertexAI()
```

```
chain = _prompt | _model
```

```
chain.invoke({"text": "Cannelloni"})
```

```
# Here's a joke about Chuck Norris and Cannelloni:
```

```
# Chuck Norris doesn't eat cannelloni. He eats the can."
```

## **Serve chains as an API with LangServe**

Once you have your prototype chain ready, you package it up and expose it as a REST API with [LangServe](https://github.com/langchain-ai/langserve) in two steps:

- Scaffold a LangServe app using the `langchain` CLI
- Add your chain with the `add_routes` call

LangServe also comes with a playground endpoint that lets you try and debug your chain. If you’re interested in learning more, you should definitely read the [launch blog of LangServe](https://blog.langchain.dev/introducing-langserve/).

## **LangChain templates**

I always like it when a project comes with well-designed recipes that show how to put everything together to build something real, and LangChain has many of them. Here’s a [long list of LangChain templates](https://python.langchain.com/docs/templates), including the Chuck Norris example I’ve just shown you.

## **Demo time**

Let’s start with the Google Cloud part. I’m assuming you already have a Google Cloud project with an active billing account. [Find the project ID](https://support.google.com/googleapi/answer/7014113?hl=en) of that project, and set it as the default:

<div _="@=866,dis=none"><div _="@=867,dis=none"></div></div>

```
gcloud config set project [PROJECT-ID]
```

You should also enable the [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com) for the project:

<div _="@=917,dis=none"><div _="@=918,dis=none"></div></div>

```
gcloud services enable aiplatform.googleapis.com
```

To call the Vertex AI PaLM API from localhost, configure [application default credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc):

<div _="@=968,dis=none"><div _="@=969,dis=none"></div></div>

```
gcloud auth application-default login
```

## **Getting started with LangChain**

First, [install the LangChain CLI](https://python.langchain.com/docs/get_started/installation#langchain-cli):

<div _="@=1022,dis=none"><div _="@=1023,dis=none"></div></div>

```
pip install langchain-cli
```

Now, scaffold a LangServe REST API and add the Chuck Norris template using the following command:

<div _="@=1070,dis=none"><div _="@=1071,dis=none"></div></div>

```
langchain app new my-demo --package vertexai-chuck-norris
```

This command creates a directory `my-demo`, and the `--package` flag installs the Chuck Norris template.

Find `app/server.py` and link in Chuck Norris using this snippet (find the comments in the file that say where):

<div _="@=1129,dis=none"><div _="@=1130,dis=none"></div></div>

```
from vertexai_chuck_norris.chain import chain as vertexai_chuck_norris_chain
```

```
add_routes(app, vertexai_chuck_norris_chain,
```

```
           path="/vertexai-chuck-norris")
```

To start the API on your localhost, change into the `my-demo` directory and start the app:

<div _="@=1206,dis=none"><div _="@=1207,dis=none"></div></div>

```
langchain serve
```

This should bring up a webserver on `http://localhost:8080`. If you go to `http://localhost:8080/vertexai-chuck-norris/playground`, you can generate more silly jokes about Chuck Norris.

## **Deploy to Cloud Run**

It’s time to go from localhost to production now. Run this to deploy the API and create a Cloud Run service.

<div _="@=1276,dis=none"><div _="@=1277,dis=none"></div></div>

```
gcloud run deploy
```

This command will ask you to confirm a few settings, and you might need to enable a few APIs. It’ll also ask you to allow unauthenticated invocations. You want that if you want to access your app through a browser and share the link with your friends.

Cloud Run creates an HTTPS endpoint for you, and automatically scales the number of container instances to handle all incoming requests.

## **From prototype to a real-world application**

Before wrapping up this article, I want to add a word of caution. Deploying your prototype chain is only the first step in getting your GenAI app ready for real-world usage in [a responsible way](https://cloud.google.com/responsible-ai). It’s recommended to apply safety filters to both input and output, and perform adversarial testing. Refer to the [safety guidance to learn more](https://developers.generativeai.google/guide/safety_guidance). Additionally, you should also consider the legal implications of using GenAI models and content. For a range of Google Cloud services, [Google Cloud assumes responsibility for potential legal risks of using our generative AI](https://cloud.google.com/blog/products/ai-machine-learning/protecting-customers-with-generative-ai-indemnification).

## **LangChain and Vertex AI extensions**

This blog shows you how to deploy your LangChains as a REST API with LangServe. If you’re already familiar with using Vertex AI, you might also be interested in signing up for the private preview of [Vertex AI Extensions](https://cloud.google.com/vertex-ai/docs/generative-ai/extensions/overview) that provides another way of integrating your LangChain chains.

## **Next steps**