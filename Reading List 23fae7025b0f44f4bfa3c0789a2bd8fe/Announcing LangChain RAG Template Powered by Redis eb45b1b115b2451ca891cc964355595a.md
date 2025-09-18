# Announcing LangChain RAG Template Powered by Redis | Redis

Column: https://redis.com/blog/announcing-langchain-rag-template-powered-by-redis/
Processed: No
created on: December 19, 2023 10:50 PM

**The recent launch of [LangChain Templates](https://blog.langchain.dev/langchain-templates/) introduces a transformative approach for developers to create and deploy generative AI APIs. LangChain Templates, including the new Redis Retrieval Augmented Generation (RAG) template, provide deployable reference architectures that blend efficiency with adaptability.**

AI developers today face a deluge of technology choices between model providers, databases, and development frameworks such as [LangChain](https://github.com/langchain-ai/langchain). Additionally, getting to production requires significant investment beyond Jupyter notebooks and fancy Streamlit demos.

To reduce the friction in deploying APIs, LangChain offers a [hub of deployable architectures](https://templates.langchain.com/). These templates encompass tool-specific chains, Large Language Model (LLM)-specific chains, and technique-specific chains, ensuring comprehensive developer options. Central to their deployment is [LangServe](https://github.com/langchain-ai/langserve), which uses [FastAPI](https://fastapi.tiangolo.com/) to transform LLM-based [Chains](https://python.langchain.com/docs/modules/chains/) or [Agents](https://python.langchain.com/docs/modules/agents/) into operational REST APIs, enhancing accessibility and production-readiness.

Redis partnered with LangChain to produce the [Redis RAG template](https://github.com/langchain-ai/langchain/tree/master/templates/rag-redis), a package optimized for creating factually consistent, LLM-powered chat applications. By using Redis as the [vector database](https://redis.com/solutions/use-cases/vector-database), this template ensures rapid context retrieval and grounded prompt construction, crucial for responsive and precise AI responses.

## Getting Started with the Redis RAG Template

The Redis RAG template serves a REST API for developers to chat with public financial PDF documents such as Nike’s 10k filings. The application uses:

- [FastAPI](https://fastapi.tiangolo.com/) and [Uvicorn](https://www.uvicorn.org/) to serve client requests via HTTP
- [UnstructuredFileLoader](https://python.langchain.com/docs/integrations/document_loaders/unstructured_file) to parse the PDF documents into raw text
- [RecursiveCharacterTextSplitter](https://python.langchain.com/docs/modules/data_connection/document_transformers/text_splitters/recursive_text_splitter) to split the text into smaller chunks
- ‘all-MiniLM-L6-v2’ sentence transformer from [HuggingFace](https://huggingface.co/) to embed text chunks into vectors
- [Redis](https://redis.com/solutions/use-cases/vector-database) as the vector database for realtime context retrieval
- [OpenAI](https://platform.openai.com/) ‘gpt-3.5-turbo-16k’ LLM to generate answers to user queries

![](Announcing%20LangChain%20RAG%20Template%20Powered%20by%20Redis%20eb45b1b115b2451ca891cc964355595a/LangChain_RAG_Redis.drawio.png)

To run the RAG application with the template, you will need two things:

1. a running Redis instance ([Redis Cloud](https://redis.com/try-free) or local [Redis Stack](https://redis.io/docs/install/install-stack/))
2. an [OpenAI API](https://platform.openai.com/) key

As always, refer to the official [project README](https://github.com/langchain-ai/langchain/tree/master/templates#readme) for the latest details. Here’s a step-by-step guide to build with the template locally:

1. **Environment Setup**: Set your OpenAI API key and Redis environment variables:

```
export OPENAI_API_KEY>
 export REDIS_HOST>
 export REDIS_PORT>
 export REDIS_USER>
 export REDIS_PASSWORD>
```

Alternatively, you can set the REDIS_URL environment variable instead of the individual components.

2. **Create and activate a Python3.9 virtual environment** (best practice). We will use [venv](https://docs.python.org/3/library/venv.html):

```
python3.9 -m venv lc-template
source lc-template/bin/activate

```

3. **Install the LangChain CLI** and Pydantic:

```
pip install -U langchain-cli pydantic==1.10.13
```

3. **Create a new LangChain project**:

```
langchain app new test-rag --package rag-redis>
```

Running the LangChain CLI command shown above will create a new directory named test-rag.

**When prompted to install the template, select the yes option,** y**.** This step will download the rag-redis template contents under the ./test-rag/packages directory and attempt to install Python requirements.

4. Enter the new project directory:

```
cd test-rag

```

Looking at the directory tree, we should see the following structure:

![](Announcing%20LangChain%20RAG%20Template%20Powered%20by%20Redis%20eb45b1b115b2451ca891cc964355595a/LangChain-RAG-image_Page_3_Image_0001.png)

directory tree

5. To use the rag-redis package, **add the following snippet** to your app/server.py file:

```
from rag_redis.chainimport chainas rag_redis_chain
add_routes(app, rag_redis_chain, path="/rag-redis")
```

6. **Ingest source data** for demo app:

```
cd packages/rag-redis
python ingest.py
```

This may take a few minutes. The ingest.py script executes a pipeline, as visualized below, that loads the source PDF docs, converts text into smaller chunks, creates text embeddings using a [HuggingFace](https://huggingface.co/) sentence transformer model, and loads data into Redis.

7. **Serve the FastAPI** app with LangServe:

```
cd ../ && cd ../
langchain serve
```

8. **Access the API** on port 8000. After spinning up, you should see the following output:

![](Announcing%20LangChain%20RAG%20Template%20Powered%20by%20Redis%20eb45b1b115b2451ca891cc964355595a/LangChain-RAG-image_Page_4_Image_0001.png)

Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to see documentation.

Visit [http://127.0.0.1:8000/rag-redis/playground](http://127.0.0.1:8000/rag-redis/playground) to use the testing playground, seen below:

![](Announcing%20LangChain%20RAG%20Template%20Powered%20by%20Redis%20eb45b1b115b2451ca891cc964355595a/LangChain-RAG-image_Page_5_Image_0001.png)

LangServ Playground

Use the playground to test your API by asking a question. The LangChain application responds with an answer that combines rich context from the Nike company PDF, retrieved from Redis, with the generative abilities of the OpenAI LLM.

## Advancing AI Innovation with LangChain and Redis

Our ongoing partnership with LangChain reflects a commitment to continual innovation in AI. This collaboration fosters the development of tools such as the LangChain RAG template and supports initiatives such as the [OpenGPTs project](https://redis.com/blog/powering-langchain-opengpts-with-redis-cloud/). The partnership also fuels our work in maintaining the [Redis <> LangChain integrations](https://python.langchain.com/docs/integrations/providers/redis), as well Redis’ own AI-native client, [redisvl](https://github.com/RedisVentures/redisvl).

Redis is dedicated to equipping AI developers with the latest resources for creating performant and production-ready applications.

## Your Next Steps

The LangChain RAG template, powered by Redis’ vector database, simplifies the creation of AI applications. Build with this template and leverage these tools to create AI solutions that drive progress in the field.