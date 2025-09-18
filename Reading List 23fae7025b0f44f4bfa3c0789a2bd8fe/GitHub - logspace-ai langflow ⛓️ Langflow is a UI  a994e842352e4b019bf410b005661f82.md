# GitHub - logspace-ai/langflow: ⛓️ Langflow is a UI for LangChain, designed with react-flow to provide an effortless way to experiment and prototype flows.

Column: https://github.com/logspace-ai/langflow
Processed: No
created on: September 9, 2023 4:23 PM

# ⛓️ Langflow

~ An effortless way to experiment and prototype [LangChain](https://github.com/hwchase17/langchain) pipelines ~

[](GitHub%20-%20logspace-ai%20langflow%20%E2%9B%93%EF%B8%8F%20Langflow%20is%20a%20UI%20%20a994e842352e4b019bf410b005661f82/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6e7472696275746f72732f6c6f6773706163652d61692f6c616e67666c6f77)

[](GitHub%20-%20logspace-ai%20langflow%20%E2%9B%93%EF%B8%8F%20Langflow%20is%20a%20UI%20%20a994e842352e4b019bf410b005661f82/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6173742d636f6d6d69742f6c6f6773706163652d61692f6c616e67666c6f77)

[](GitHub%20-%20logspace-ai%20langflow%20%E2%9B%93%EF%B8%8F%20Langflow%20is%20a%20UI%20%20a994e842352e4b019bf410b005661f82/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f7265706f2d73697a652f6c6f6773706163652d61692f6c616e67666c6f77)

[](GitHub%20-%20logspace-ai%20langflow%20%E2%9B%93%EF%B8%8F%20Langflow%20is%20a%20UI%20%20a994e842352e4b019bf410b005661f82/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f6c6f6773706163652d61692f6c616e67666c6f77)

[](GitHub%20-%20logspace-ai%20langflow%20%E2%9B%93%EF%B8%8F%20Langflow%20is%20a%20UI%20%20a994e842352e4b019bf410b005661f82/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732d70722f6c6f6773706163652d61692f6c616e67666c6f77)

[](GitHub%20-%20logspace-ai%20langflow%20%E2%9B%93%EF%B8%8F%20Langflow%20is%20a%20UI%20%20a994e842352e4b019bf410b005661f82/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6c6f6773706163652d61692f6c616e67666c6f77)

[](GitHub%20-%20logspace-ai%20langflow%20%E2%9B%93%EF%B8%8F%20Langflow%20is%20a%20UI%20%20a994e842352e4b019bf410b005661f82/68747470733a2f2f646362616467652e76657263656c2e6170702f6170692f7365727665722f45716b737945324558393f636f6d706163743d74727565267374796c653d666c6174)

[](GitHub%20-%20logspace-ai%20langflow%20%E2%9B%93%EF%B8%8F%20Langflow%20is%20a%20UI%20%20a994e842352e4b019bf410b005661f82/68747470733a2f2f68756767696e67666163652e636f2f64617461736574732f68756767696e67666163652f6261646765732f7261772f6d61696e2f6f70656e2d696e2d68662d7370616365732d736d2e737667)

![](GitHub%20-%20logspace-ai%20langflow%20%E2%9B%93%EF%B8%8F%20Langflow%20is%20a%20UI%20%20a994e842352e4b019bf410b005661f82/langflow-demo.gif)

# Table of Contents

- [⛓️ Langflow](https://github.com/logspace-ai/langflow#%EF%B8%8F-langflow)
- [Table of Contents](https://github.com/logspace-ai/langflow#table-of-contents)
- [📦 Installation](https://github.com/logspace-ai/langflow#-installation)
    - [Locally](https://github.com/logspace-ai/langflow#locally)
    - [HuggingFace Spaces](https://github.com/logspace-ai/langflow#huggingface-spaces)
- [🖥️ Command Line Interface (CLI)](https://github.com/logspace-ai/langflow#%EF%B8%8F-command-line-interface-cli)
    - [Usage](https://github.com/logspace-ai/langflow#usage)
        - [Environment Variables](https://github.com/logspace-ai/langflow#environment-variables)
- [Deployment](https://github.com/logspace-ai/langflow#deployment)
    - [Deploy Langflow on Google Cloud Platform](https://github.com/logspace-ai/langflow#deploy-langflow-on-google-cloud-platform)
    - [Deploy Langflow on Jina AI Cloud](https://github.com/logspace-ai/langflow#deploy-langflow-on-jina-ai-cloud)
        - [API Usage](https://github.com/logspace-ai/langflow#api-usage)
    - [Deploy on Railway](https://github.com/logspace-ai/langflow#deploy-on-railway)
    - [Deploy on Render](https://github.com/logspace-ai/langflow#deploy-on-render)
- [🎨 Creating Flows](https://github.com/logspace-ai/langflow#-creating-flows)
- [👋 Contributing](https://github.com/logspace-ai/langflow#-contributing)
- [📄 License](https://github.com/logspace-ai/langflow#-license)

# 📦 Installation

### **Locally**

You can install Langflow from pip:

```
# This installs the package without dependencies for local models
pip install langflow
```

To use local models (e.g llama-cpp-python) run:

```
pip install langflow[local]
```

This will install the following dependencies:

- [CTransformers](https://github.com/marella/ctransformers)
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
- [sentence-transformers](https://github.com/UKPLab/sentence-transformers)

You can still use models from projects like LocalAI

Next, run:

```
python -m langflow
```

or

```
langflow # or langflow --help
```

### HuggingFace Spaces

You can also check it out on [HuggingFace Spaces](https://huggingface.co/spaces/Logspace/Langflow) and run it in your browser! You can even clone it and have your own copy of Langflow to play with.

# 🖥️ Command Line Interface (CLI)

Langflow provides a command-line interface (CLI) for easy management and configuration.

## Usage

You can run the Langflow using the following command:

```
langflow [OPTIONS]
```

Each option is detailed below:

- `-help`: Displays all available options.
- `-host`: Defines the host to bind the server to. Can be set using the `LANGFLOW_HOST` environment variable. The default is `127.0.0.1`.
- `-workers`: Sets the number of worker processes. Can be set using the `LANGFLOW_WORKERS` environment variable. The default is `1`.
- `-timeout`: Sets the worker timeout in seconds. The default is `60`.
- `-port`: Sets the port to listen on. Can be set using the `LANGFLOW_PORT` environment variable. The default is `7860`.
- `-config`: Defines the path to the configuration file. The default is `config.yaml`.
- `-env-file`: Specifies the path to the .env file containing environment variables. The default is `.env`.
- `-log-level`: Defines the logging level. Can be set using the `LANGFLOW_LOG_LEVEL` environment variable. The default is `critical`.
- `-components-path`: Specifies the path to the directory containing custom components. Can be set using the `LANGFLOW_COMPONENTS_PATH` environment variable. The default is `langflow/components`.
- `-log-file`: Specifies the path to the log file. Can be set using the `LANGFLOW_LOG_FILE` environment variable. The default is `logs/langflow.log`.
- `-cache`: Selects the type of cache to use. Options are `InMemoryCache` and `SQLiteCache`. Can be set using the `LANGFLOW_LANGCHAIN_CACHE` environment variable. The default is `SQLiteCache`.
- `-jcloud/--no-jcloud`: Toggles the option to deploy on Jina AI Cloud. The default is `no-jcloud`.
- `-dev/--no-dev`: Toggles the development mode. The default is `no-dev`.
- `-path`: Specifies the path to the frontend directory containing build files. This option is for development purposes only. Can be set using the `LANGFLOW_FRONTEND_PATH` environment variable.
- `-open-browser/--no-open-browser`: Toggles the option to open the browser after starting the server. Can be set using the `LANGFLOW_OPEN_BROWSER` environment variable. The default is `open-browser`.
- `-remove-api-keys/--no-remove-api-keys`: Toggles the option to remove API keys from the projects saved in the database. Can be set using the `LANGFLOW_REMOVE_API_KEYS` environment variable. The default is `no-remove-api-keys`.
- `-install-completion [bash|zsh|fish|powershell|pwsh]`: Installs completion for the specified shell.
- `-show-completion [bash|zsh|fish|powershell|pwsh]`: Shows completion for the specified shell, allowing you to copy it or customize the installation.

### Environment Variables

You can configure many of the CLI options using environment variables. These can be exported in your operating system or added to a `.env` file and loaded using the `--env-file` option.

A sample `.env` file named `.env.example` is included with the project. Copy this file to a new file named `.env` and replace the example values with your actual settings. If you're setting values in both your OS and the `.env` file, the `.env` settings will take precedence.

# Deployment

## Deploy Langflow on Google Cloud Platform

Follow our step-by-step guide to deploy Langflow on Google Cloud Platform (GCP) using Google Cloud Shell. The guide is available in the [**Langflow in Google Cloud Platform**](https://github.com/logspace-ai/langflow/blob/dev/GCP_DEPLOYMENT.md) document.

Alternatively, click the **"Open in Cloud Shell"** button below to launch Google Cloud Shell, clone the Langflow repository, and start an **interactive tutorial** that will guide you through the process of setting up the necessary resources and deploying Langflow on your GCP project.

[](GitHub%20-%20logspace-ai%20langflow%20%E2%9B%93%EF%B8%8F%20Langflow%20is%20a%20UI%20%20a994e842352e4b019bf410b005661f82/68747470733a2f2f677374617469632e636f6d2f636c6f75647373682f696d616765732f6f70656e2d62746e2e737667)

## Deploy Langflow on [Jina AI Cloud](https://github.com/jina-ai/langchain-serve)

Langflow integrates with langchain-serve to provide a one-command deployment to Jina AI Cloud.

Start by installing `langchain-serve` with

```
pip install langflow[deploy]
# or
pip install -U langchain-serve
```

Then, run:

```
langflow --jcloud
```

```
🎉 Langflow server successfully deployed on Jina AI Cloud 🎉
🔗 Click on the link to open the server (please allow ~1-2 minutes for the server to startup): https://<your-app>.wolf.jina.ai/
📖 Read more about managing the server: https://github.com/jina-ai/langchain-serve

```

Details

Show complete (example) output

```
  🚀 Deploying Langflow server on Jina AI Cloud
  ╭───────────────────────── 🎉 Flow is available! ──────────────────────────╮
  │                                                                          │
  │   ID                    langflow-e3dd8820ec                              │
  │   Gateway (Websocket)   wss://langflow-e3dd8820ec.wolf.jina.ai           │
  │   Dashboard             https://dashboard.wolf.jina.ai/flow/e3dd8820ec   │
  │                                                                          │
  ╰──────────────────────────────────────────────────────────────────────────╯
  ╭──────────────┬──────────────────────────────────────────────────────────────────────────────╮
  │ App ID       │                     langflow-e3dd8820ec                                      │
  ├──────────────┼──────────────────────────────────────────────────────────────────────────────┤
  │ Phase        │                            Serving                                           │
  ├──────────────┼──────────────────────────────────────────────────────────────────────────────┤
  │ Endpoint     │          wss://langflow-e3dd8820ec.wolf.jina.ai                              │
  ├──────────────┼──────────────────────────────────────────────────────────────────────────────┤
  │ App logs     │                  dashboards.wolf.jina.ai                                     │
  ├──────────────┼──────────────────────────────────────────────────────────────────────────────┤
  │ Swagger UI   │          https://langflow-e3dd8820ec.wolf.jina.ai/docs                       │
  ├──────────────┼──────────────────────────────────────────────────────────────────────────────┤
  │ OpenAPI JSON │        https://langflow-e3dd8820ec.wolf.jina.ai/openapi.json                 │
  ╰──────────────┴──────────────────────────────────────────────────────────────────────────────╯

  🎉 Langflow server successfully deployed on Jina AI Cloud 🎉
  🔗 Click on the link to open the server (please allow ~1-2 minutes for the server to startup): https://langflow-e3dd8820ec.wolf.jina.ai/
  📖 Read more about managing the server: https://github.com/jina-ai/langchain-serve

```

### API Usage

You can use Langflow directly on your browser, or use the API endpoints on Jina AI Cloud to interact with the server.

Details

Show API usage (with python)

```
import requests

BASE_API_URL = "https://langflow-e3dd8820ec.wolf.jina.ai/api/v1/predict"
FLOW_ID = "864c4f98-2e59-468b-8e13-79cd8da07468"
# You can tweak the flow by adding a tweaks dictionary
# e.g {"OpenAI-XXXXX": {"model_name": "gpt-4"}}
TWEAKS = {
"ChatOpenAI-g4jEr": {},
"ConversationChain-UidfJ": {}
}

def run_flow(message: str, flow_id: str, tweaks: dict = None) -> dict:
  """
  Run a flow with a given message and optional tweaks.

  :param message: The message to send to the flow
  :param flow_id: The ID of the flow to run
  :param tweaks: Optional tweaks to customize the flow
  :return: The JSON response from the flow
  """
  api_url = f"{BASE_API_URL}/{flow_id}"

  payload = {"message": message}

  if tweaks:
      payload["tweaks"] = tweaks

  response = requests.post(api_url, json=payload)
  return response.json()

# Setup any tweaks you want to apply to the flow
print(run_flow("Your message", flow_id=FLOW_ID, tweaks=TWEAKS))
```

```
{
  "result": "Great choice! Bangalore in the 1920s was a vibrant city with a rich cultural and political scene. Here are some suggestions for things to see and do:\n\n1. Visit the Bangalore Palace - built in 1887, this stunning palace is a perfect example of Tudor-style architecture. It was home to the Maharaja of Mysore and is now open to the public.\n\n2. Attend a performance at the Ravindra Kalakshetra - this cultural center was built in the 1920s and is still a popular venue for music and dance performances.\n\n3. Explore the neighborhoods of Basavanagudi and Malleswaram - both of these areas have retained much of their old-world charm and are great places to walk around and soak up the atmosphere.\n\n4. Check out the Bangalore Club - founded in 1868, this exclusive social club was a favorite haunt of the British expat community in the 1920s.\n\n5. Attend a meeting of the Indian National Congress - founded in 1885, the INC was a major force in the Indian independence movement and held many meetings and rallies in Bangalore in the 1920s.\n\nHope you enjoy your trip to 1920s Bangalore!"
}
```

> 
> 
> 
> Read more about resource customization, cost, and management of Langflow apps on Jina AI Cloud in the [**langchain-serve**](https://github.com/jina-ai/langchain-serve) repository.
> 

## Deploy on Railway

[](GitHub%20-%20logspace-ai%20langflow%20%E2%9B%93%EF%B8%8F%20Langflow%20is%20a%20UI%20%20a994e842352e4b019bf410b005661f82/68747470733a2f2f7261696c7761792e6170702f627574746f6e2e737667)

## Deploy on Render

[](GitHub%20-%20logspace-ai%20langflow%20%E2%9B%93%EF%B8%8F%20Langflow%20is%20a%20UI%20%20a994e842352e4b019bf410b005661f82/68747470733a2f2f72656e6465722e636f6d2f696d616765732f6465706c6f792d746f2d72656e6465722d627574746f6e2e737667)

# 🎨 Creating Flows

Creating flows with Langflow is easy. Simply drag sidebar components onto the canvas and connect them together to create your pipeline. Langflow provides a range of [LangChain components](https://langchain.readthedocs.io/en/latest/reference.html) to choose from, including LLMs, prompt serializers, agents, and chains.

Explore by editing prompt parameters, link chains and agents, track an agent's thought process, and export your flow.

Once you're done, you can export your flow as a JSON file to use with LangChain. To do so, click the "Export" button in the top right corner of the canvas, then in Python, you can load the flow with:

```
from langflow import load_flow_from_json

flow = load_flow_from_json("path/to/flow.json")
# Now you can use it like any chain
flow("Hey, have you heard of Langflow?")
```

# 👋 Contributing

We welcome contributions from developers of all levels to our open-source project on GitHub. If you'd like to contribute, please check our [contributing guidelines](https://github.com/logspace-ai/langflow/blob/dev/CONTRIBUTING.md) and help make Langflow more accessible.

Join our [Discord](https://discord.com/invite/EqksyE2EX9) server to ask questions, make suggestions and showcase your projects! 🦾

[](GitHub%20-%20logspace-ai%20langflow%20%E2%9B%93%EF%B8%8F%20Langflow%20is%20a%20UI%20%20a994e842352e4b019bf410b005661f82/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d6c6f6773706163652d61692f6c616e67666c6f7726747970653d54696d656c696e65)

# 📄 License

Langflow is released under the MIT License. See the LICENSE file for details.