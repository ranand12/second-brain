# From Zero to Hero: Building LLM Chains and Agents with Google DeepMind’s OneTwo OpenSource Toolkit. | by Olejniczak Lukasz | Jul, 2024 | AI Advances

Column: https://ai.gopubby.com/from-zero-to-hero-building-llm-chains-and-agents-with-google-deepminds-onetwo-opensource-toolkit-7d7b5cb6c8b7
Processed: Yes
created on: August 13, 2024 8:04 PM

In April 2024 Google DeepMind open-sourced project named **OneTwo. Google Search explains that it is a python library designed to simplify interactions with language and multimodal foundation models:**

![](https://miro.medium.com/v2/resize:fit:700/1*tgbSWblVQWYJNT0VgijM-w.png)

You might wonder, which interactions need simplification? After all the easiest way to interact with multimodal foundational models is through applications like **Gemini App** ([gemini.google.com](http://gemini.google.com/)). Just start asking questions, work with documents, book flights, … But for developers, integrating language models into their products opens up a world of possibilities.

Imagine building features that require multiple steps, each involving a different request to the model or even external systems. To handle these complex sequences, you’ll need an orchestration tool. OneTwo is one option designed specifically for this purpose.

At first glance, this library might seem similar to packages like Langchain or LlamaIndex. However, as you explore the examples in this blog, you’ll appreciate its lightweight design and discover its unique capabilities that set it apart.

In this blog I will cover the following topics:

- Explain step by step how to use OneTwo library to chain language models for serial and/or parallel execution
- Explain how to build prompt templates with intermediate and intermediate state variables
- Explain how to build agents with tools and customize ReAct template
- Show how to deploy our OneTwo ReAct Agent as Cloud Run Service!!

Intrigued? Let’s dive in and build some OneTwo chains with **Gemini** on **Vertex AI**! We’ll be using **Vertex AI Colab Enterprise** as our workspace. Open a new notebook, and let’s get started!

![](https://miro.medium.com/v2/resize:fit:700/1*qqCVyvbBFPhlpdvYwiuu0Q.png)

First things first — install **OneTwo** library:

```
!pip install git+https://github.com/google-deepmind/onetwo
```

OneTwo is designed to give you incredible flexibility when building flows by decoupling flow definitions from language models represented by so-called backends. Therefore backends are swappable components that determine where your AI application “gets its answers” from. Think of it like choosing the type of fuel for your AI car. Just as different fuels offer varying performance and efficiency, OneTwo lets you choose from diverse backends like Gemini API in Google AI Studio, Vertex AI API, OpenAI API, and Local Gemma. You can even add more through the OneTwo API! Each backend brings unique strengths and characteristics to your AI application, giving you the power to tailor it to your specific needs.

[](https://miro.medium.com/v2/resize:fit:700/0*yUr12xy0wNNeKM3N)

In this blog, I will be using **Vertex AI** backend.

![](https://miro.medium.com/v2/resize:fit:700/1*AplAqb_a5SC83DS1cpODvA.png)

![](https://miro.medium.com/v2/resize:fit:700/1*8cWNS5uqgz_9qJi87Rtv1w.png)

We’ll start simple with a one-step flow to get an answer to our question.

However, lets first clarify what does Vertex AI bring to the table for our OneTwo chain adventure? Vertex AI is your one-stop shop for everything ML, from prototyping and training to automating, serving, and monitoring models. It offers a wide range of language and multimodal foundation models. For our example, we’ll configure our Vertex AI backend for text generation using the **gemini-1.5-flash-001** model.

![](https://miro.medium.com/v2/resize:fit:700/1*ln9xv-y5NiRjwRkniAQr1g.png)

There are many more parameters we can set here, like Vertex AI Project and location. But the most interesting ones are:

- **max_qps**: which helps to specify maximum number of queries per second for the backend (if None, no rate limiting is applied)
- **batch_size:** which helps to specify a number of requests that are grouped together when sending them to GenAI API. When GenAI API does not explicitly support batching, OneTwo sends multiple requests from separate threads. This parameter works for models specified for generate_text, chat and generate_embedding.

OneTwo also boasts a unique capability: the ability to cache the results of calls to language models. This allows you to swiftly replay a flow or experiment, even if it only partially executed, without incurring costs for previously completed calls. Imagine you have a complex flow and want to add another step. With OneTwo, rerunning the entire flow simply means retrieving the cached results and executing only the new step. This caching feature is enabled by default, saving you both time and money.

```
backend = vertexai_api.VertexAIAPI(generate_model_name='gemini-1.5-flash-001')
```

One important technical detail to remember: we must register the backend before we can use it:

```
backend.register()
```

Alright, let’s run a very simple flow consisting of just a single step:

```
from onetwo import ot
from onetwo.builtins import llm

# Ask the model to generate answer.
e = llm.generate_text(
    'What are the three not so well known cities in Spain?',
    max_tokens=1024,
)

print(ot.run(e))
```

![](https://miro.medium.com/v2/resize:fit:700/1*4_x00gHmY9NKeUaCCXu4yg.png)

Because we didn’t disable caching, re-executing the same cell instantly retrieves the same answer from the cache!

Now, let’s spice things up a bit and build a flow with two steps, where the second step waits for the response from the first.

```
@ot.make_executable
async def f() -> str:
  result1 = await llm.generate_text(
      'Q: What is the southernmost city in France? A:',
      max_tokens=500,
  )
  print('Intermediate result:', result1)
  result2 = await llm.generate_text(
      f'Q: Who is the mayor of {result1}? A:',
      max_tokens=500,
  )
  return result2

result = ot.run(f())
print(result)
```

All we need to do is write a Python function that includes these two steps and decorate it with `@ot.make_executable`. This allows us to use it within `ot.run()`:

![](https://miro.medium.com/v2/resize:fit:700/1*bGDE8EW19WjES8UdWuaDtQ.png)

As you can see, OneTwo seamlessly chained this sequence of steps, using the output from the first step as input for the second.

Now, what if there’s no dependency between steps, like in the following example?

```
e1 = llm.generate_text(
    'Q: What is the southernmost city in France? A:', max_tokens=500
)
e2 = llm.generate_text(
    'Q: What is the southernmost city in Spain? A:', max_tokens=500
)
```

We can leverage another unique capability of OneTwo: Asynchronous Execution. This feature utilizes multi-threading, allowing us to execute calls in parallel!

We can instruct OneTwo to execute the two calls concurrently by adding `e = ot.parallel(e1, e2)`:

```
@ot.make_executable
async def f() -> list:
  e1 = llm.generate_text(
      'Q: What is the southernmost city in France? A:', max_tokens=500
  )
  e2 = llm.generate_text(
      'Q: What is the southernmost city in Spain? A:', max_tokens=500
  )
  e = ot.parallel(e1, e2)
  return e
```

![](https://miro.medium.com/v2/resize:fit:700/1*0_1hROhcIQZm8ZlKubCD1A.png)

Easy, right?

Now, let’s experiment a little with prompt templates. OneTwo offers two options for defining them. One is to use Jinja2 syntax, where we can create a template using OneTwo’s built-in `composables.j()`:

```
from onetwo.builtins import composables

template = composables.j("""\
What is the southernmost city in Poland? {{ generate_text(max_tokens=500) }}
Who is its mayor? {{ generate_text(max_tokens=500) }}
""")
result = ot.run(template)
print(result)
```

![](https://miro.medium.com/v2/resize:fit:700/1*VAK8-lRJzxr2C15jsKfrIQ.png)

What else can we do? We can also add variables to templates. In the following example, we’ll add a variable named “country”:

```
prompt = composables.j(
    'Q: What is the capital of {{ country }}?\n'
    'A:{{ store("city", generate_text(max_tokens=100 }}\n'
    'Q: Who is the mayor of {{ __vars__.city }}?\n'
    'A:{{ store("mayor", generate_text(max_tokens=10)) }}'
)
res = ot.run(prompt(country='France'))
print(res)
print(prompt['city'], prompt['mayor'])
```

Now, you might be wondering, what are `{{ store() }}` and `{{ __vars__.city }}`? These represent another powerful feature of OneTwo: short-term memory for storing intermediate variables.

```
{{ store("variable_name", built-in function, e.g. generate_text) }}
```

We can reference this stored temporal variable later in the prompt template using:

```
{{ __vars__.variable_name }}
```

This is an amazing feature, isn’t it?

Another option for defining prompt templates is to concatenate `composables.generate_text()` and `composables.store()` into the prompt string using the '+' operator.

```
e = (
    'What is the southernmost city in Poland? ' + composables.generate_text(max_tokens=20) +
    '\nWho is its mayor? ' + composables.generate_text(max_tokens=20)
)
result = ot.run(e)
print(result)
```

In this pattern, we can also use and chain operations on the short-term memory handled by `store`:

```
e = (
    composables.f('Q: What is the capital of {question}?\nA:') +
    composables.store('city', composables.generate_text(max_tokens=100)) +
    composables.f('\nQ: Who is the mayor of {city}?\nA:') +
    composables.store('mayor', composables.generate_text(max_tokens=100))
)
res = ot.run(e(question='Poland'))
print(res)
print(e['city'], e['mayor'])
```

But can we somehow extract and output the values stored during flow executions? Absolutely!

```
print(e['city'], e['mayor'])
```

Alright, that covered the basics. Now, how about tools? Not so fast! In the OneTwo framework, tools are designed to define the capabilities of **AGENTS.**

OneTwo offers two ready-to-use components for multi-step tool usage: ReActAgent and PythonPlanningAgent. In this discussion, we’ll focus on ReActAgent. To utilize this component, we need the following import:

```
from onetwo.agents import react
```

Next, we’ll create a new instance of our agent:

```
react_agent = react.ReActAgent()
```

And now we’re ready to ask questions!

```
question = 'What is the total population of Poland?'
answer = ot.run(react_agent(inputs=question))
answer
```

to learn the following:

Agents in OneTwo are specifically designed for use with tools. I highly encourage you to study the prompt template for the [ReActAgent](https://github.com/google-deepmind/onetwo/blob/main/onetwo/agents/react.py) component to gain a deeper understanding of how it operates.

![](https://miro.medium.com/v2/resize:fit:700/1*h2lzhuYSmDTVP2-Mw2Ja8g.png)

To proceed, we need a Tool. Let’s create one from a Python function.

This function will call the Frankfurter API ([https://api.frankfurter.app/](https://api.frankfurter.app/)) to obtain exchange rate data for specified currencies and a date:

```
def get_exchange_rate(
    currency_from: str = "USD",
    currency_to: str = "EUR",
    currency_date: str = "latest",
):
    """Retrieves the exchange rate between two currencies on a specified date.

    Uses the Frankfurter API (https://api.frankfurter.app/) to obtain exchange rate data.

    Args:
        currency_from: The base currency (3-letter currency code). Defaults to "USD" (US Dollar).
        currency_to: The target currency (3-letter currency code). Defaults to "EUR" (Euro).
        currency_date: The date for which to retrieve the exchange rate. Defaults to "latest" for the most recent exchange rate data. Can be specified in YYYY-MM-DD format for historical rates.

    Returns:
        dict: A dictionary containing the exchange rate information.
             Example: {"amount": 1.0, "base": "USD", "date": "2023-11-24", "rates": {"EUR": 0.95534}}
    """
    import requests
    response = requests.get(
        f"https://api.frankfurter.app/{currency_date}",
        params={"from": currency_from, "to": currency_to},
    )
    return response.json()
```

If we plan to use a Python function as a Tool, we need the following declaration:

```
from onetwo.stdlib.tool_use import llm_tool_use

exchange_rate_tool = llm_tool_use.Tool(
    name='get_exchange_rate',
    function=get_exchange_rate,
    ##example=EXAMPLES,
)
```

We’ll also need another Tool to finalize the planning and deliver a response to the user:

```
finish_tool = llm_tool_use.Tool(
    name='Finish',
    function=lambda x: x,
    description='Function for returning the final answer.',
)
```

Now, if you revisit the ReAct prompt template, you’ll notice a block starting at line 111 called “ReAct few-shots.” This section is crucial because it provides examples of how the agent can solve problems using tools. The underlying language model should be able to generalize and adapt to our tools, but generally, providing good examples here leads to a more effective agent.

Given the importance of this element, let me show you how to declare your own example:

```
from onetwo.agents.react import ReActStep, ReActState

REACT_FEWSHOTS_EXCHANGE = [
    ReActState(
        inputs="What's the exchange rate from US dollars to British currency today??",
        updates=[
            ReActStep(
                thought=(
                    'The user wants to know the exchange rate between USD and GBP today'
                ),
                action=llm_tool_use.FunctionCall(
                    function_name='get_exchange_rate',
                    args=('USD','GBP','latest'),
                    kwargs={},
                ),
                observation='{"amount": 1.0, "base": "USD", "date": "2023-11-24", "rates": {"GBP": 0.95534}}',
                fmt=llm_tool_use.ArgumentFormat.JSON,
            ),
            ReActStep(
                is_finished=True,
                thought='The API response contains the exchange rate for today. The user should be informed about the current exchange rate. Extract the rate for GBP from the rates dictionary',
                action=llm_tool_use.FunctionCall(
                    function_name='Finish', args=('The exchange rate from USD to GBP today (2024-07-01) is 1 USD = 0.95534 GBP',), kwargs={}
                ),
                observation='The exchange rate from USD to GBP today (2024-07-01) is 1 USD = 0.95534 GBP',
                fmt=llm_tool_use.ArgumentFormat.PYTHON,
            ),
        ],
    ),

]
```

Our few-shot example consists of two steps:

1. **Mapping the user question to the get_exchange_rate tool:** In this step, we interpret the user’s query and determine the relevant parameters for the `get_exchange_rate` function. This includes extracting the currency values and date from the question. The response from this tool is then recorded as the observation.
2. **Finalizing and responding to the user:** Here, we signal that the tool execution sequence is complete and ready to present the answer. We call the `Finish` tool, instructing the model how to formulate a response. Since the exchange rate isn't explicitly stated, the response is crafted by interpreting the JSON data from the previous step.

Now, let’s dive deeper into the individual components of each step in the ReAct strategy.

- **Thought:** The “thought” represents the agent’s internal reasoning process. It’s the logic that determines the next action based on the current situation and available data.

```
thought=(
   'The user wants to know the exchange rate between USD and GBP today'
),
```

- **Action:** This is the specific task or operation the agent will carry out in this step, if applicable. It could involve calling a tool, manipulating data, or even deciding to gather more information.

```
action=llm_tool_use.FunctionCall(
                    function_name='get_exchange_rate',
                    args=('USD','GBP','latest'),
                    kwargs={},
)
```

- **Observation:** This component captures the results of any executed actions. It’s essentially the feedback the agent receives from the environment, which can be the output of a tool, changes in data, or even a lack of change. This observation then informs the agent’s next thought and action.

```
observation='{"amount": 1.0, "base": "USD", "date": "2023-11-24", "rates": {"GBP": 0.95534}}',
```

- **is_finished:** This internal state indicates whether the current step is intended to be the final one in the process. If `is_finished` is True, it means that the observation generated in this step can be treated as the final answer and the agent's task is complete.

```
is_finished=False,
```

- **fmt:** This specifies the format in which the action (and the resulting observation) are to be presented to the language model. It determines how the information is structured and displayed, ensuring that the LLM can understand and process it effectively.

```
fmt=llm_tool_use.ArgumentFormat.JSON,
```

More examples to study the ReAct strategy can be found in the original paper from Google entitled: “[ReAct: Synergizing Reasoning and Acting in Language Models.](https://arxiv.org/pdf/2210.03629)”

Source: [https://arxiv.org/pdf/2210.03629](https://arxiv.org/pdf/2210.03629)

![](https://miro.medium.com/v2/resize:fit:530/1*TQuSubUUHwtXZhV86Jzksw.png)

With that understanding, we’re ready to declare our agent:

```
from onetwo.agents import react
from onetwo.stdlib.tool_use import llm_tool_use
from onetwo.stdlib.tool_use import python_tool_use

react_agent = react.ReActAgent(
    exemplars=REACT_FEWSHOTS_EXCHANGE,
    environment_config=python_tool_use.PythonToolUseEnvironmentConfig(
        tools=[exchange_rate_tool, finish_tool],
    ),
    ##max_steps=20,
    ##stop_prefix=''
)
```

Excellent! Now our agent’s definition includes both the necessary tools and the instructional examples.

Let’s pose our question: “What’s the exchange rate from US dollars to Polish currency today?”

```
question = "What's the exchange rate from US dollars to Polish currency today?"
```

```
from onetwo import ot
answer = ot.run(react_agent(inputs=question))
answer
```

![](https://miro.medium.com/v2/resize:fit:700/1*urIx_xJjabhfxHDiratM0Q.png)

As you can see, the agent successfully utilized its model knowledge to identify the currency of Poland (Polish zloty), execute the `get_exchange_rate` function with the correct currencies, and present the answer with the corresponding exchange rate, all while adhering to the communication style from our example.

But what if something goes wrong? How can we troubleshoot this reasoning and action process? This is where traces come in handy.

Enabling traces is quite simple. Just add `enable_tracing=True` when running the agent:

```
answer, trace = ot.run(react_agent(inputs=question), enable_tracing=True)
answer
```

And here’s how you can display the collected traces:

```
from onetwo.core import results
print(results.format_result(trace, color=True))
```

![](https://miro.medium.com/v2/resize:fit:700/1*Fu35Phr21HYRxOi6ap9H2A.png)

You can even display the traces in a visually appealing HTML format:

```
import IPython
IPython.display.HTML(results.HTMLRenderer().render(trace))
```

![](https://miro.medium.com/v2/resize:fit:700/1*nBb7yHEFAsGQNNg_Ppkp7Q.png)

Okay, for our final question: how can we deploy such an agent to Cloud Run? In my next blog post I will show you how to do it using **VertexAI Reasoning Engine [custom templates](https://cloud.google.com/vertex-ai/generative-ai/docs/reasoning-engine/customize).** Here I will deploy it the hard way, but then you will appreciate the value of **Reasoning Engine**.

If this is your first time deploying code as a Cloud Run service, it might seem like the most challenging part of this blog. Unfortunately, there’s no simple way to directly deploy your notebook as a Cloud Run service. However, I’ll provide detailed steps to guide you through the process smoothly.

Essentially, we’ll need to copy large portions of our code from the notebook and organize it into Python files. (WARNING: Use the `%%writefile` cell magic only if you're creating these files within Vertex AI Colab Notebook cells, not in an IDE like PyCharm or VSCode):

![](https://miro.medium.com/v2/resize:fit:450/1*o1aZda_yZ4A5W2DSMJ6F8Q.png)

1. **requirements.txt** file which includes all the dependencies needed to run our agent and tools

```
%%writefile requirements.txt

Flask
gunicorn
Werkzeug
blinker==1.4
sentencepiece
git+https://github.com/google-deepmind/onetwo
google-cloud-aiplatform==1.55.0
```

2. **ctools.py** file which includes definitions of our tools

```
%%writefile ctools.py

from onetwo.stdlib.tool_use import llm_tool_use
import requests

def get_exchange_rate(
    currency_from: str = "USD",
    currency_to: str = "EUR",
    currency_date: str = "latest",
):
    """Retrieves the exchange rate between two currencies on a specified date.

    Uses the Frankfurter API (https://api.frankfurter.app/) to obtain exchange rate data.

    Args:
        currency_from: The base currency (3-letter currency code). Defaults to "USD" (US Dollar).
        currency_to: The target currency (3-letter currency code). Defaults to "EUR" (Euro).
        currency_date: The date for which to retrieve the exchange rate. Defaults to "latest" for the most recent exchange rate data. Can be specified in YYYY-MM-DD format for historical rates.

    Returns:
        dict: A dictionary containing the exchange rate information.
             Example: {"amount": 1.0, "base": "USD", "date": "2023-11-24", "rates": {"EUR": 0.95534}}
    """

    response = requests.get(
        f"https://api.frankfurter.app/{currency_date}",
        params={"from": currency_from, "to": currency_to},
    )
    return response.json()

finish_tool = llm_tool_use.Tool(
    name='Finish',
    function=lambda x: x,
    description='Function for returning the final answer.',
)

exchange_rate_tool = llm_tool_use.Tool(
    name='get_exchange_rate',
    function=get_exchange_rate,
    ##example=EXAMPLES,
)
```

3. **agent.py** file which includes reasoning and action examples and agent definition:

```
%%writefile cagent.py

from onetwo.agents import react
from onetwo.agents.react import ReActStep, ReActState
from onetwo.stdlib.tool_use import llm_tool_use
from onetwo.stdlib.tool_use import python_tool_use
from ctools import exchange_rate_tool, finish_tool

REACT_FEWSHOTS_EXCHANGE = [
    ReActState(
        inputs="What's the exchange rate from US dollars to British currency today??",
        updates=[
            ReActStep(
                thought=(
                    'The user wants to know the exchange rate between USD and GBP today'
                ),
                action=llm_tool_use.FunctionCall(
                    function_name='get_exchange_rate',
                    args=('USD','GBP','latest'),
                    kwargs={},
                ),
                observation='{"amount": 1.0, "base": "USD", "date": "2023-11-24", "rates": {"GBP": 0.95534}}',
                fmt=llm_tool_use.ArgumentFormat.JSON,
            ),
            ReActStep(
                is_finished=True,
                thought='The API response contains the exchange rate for today. The user should be informed about the current exchange rate. Extract the rate for GBP from the rates dictionary',
                action=llm_tool_use.FunctionCall(
                    function_name='Finish', args=('The exchange rate from USD to GBP today (2024-07-01) is 1 USD = 0.95534 GBP',), kwargs={}
                ),
                observation='The exchange rate from USD to GBP today (2024-07-01) is 1 USD = 0.95534 GBP',
                fmt=llm_tool_use.ArgumentFormat.PYTHON,
            ),
        ],
    ),

]

react_agent = react.ReActAgent(
    exemplars=REACT_FEWSHOTS_EXCHANGE,
    environment_config=python_tool_use.PythonToolUseEnvironmentConfig(
        tools=[exchange_rate_tool, finish_tool],
    ),
    ##max_steps=20,
    ##stop_prefix=''
)
```

4. main.py file which is going to be a main entry point to our service where our questions are routed to our agent:

```
%%writefile onetwoagent/main.py

import os
from onetwo import ot
from flask import Flask, request, jsonify
from cagent import react_agent
from onetwo.backends import vertexai_api

app = Flask(__name__)

@app.route("/", methods=["POST"])
def get_answer():
    data = request.get_json()

    if not data or "question" not in data:
        return jsonify({"error": "Please provide a 'question' key in the JSON body."}), 400

    backend = vertexai_api.VertexAIAPI(generate_model_name='gemini-1.5-flash-001')
    backend.register()
    question = data["question"]
    # Run the agent on the question and return the answer.
    answer = ot.run(react_agent(inputs=question))
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
```

5. **Dockerfile.** Cloud Run’s primary way of deploying applications is through container images. A Dockerfile is the blueprint for creating these images. It defines the runtime environment, dependencies, startup scripts …

```
%%writefile onetwoagent/Dockerfile

FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install required system dependencies
RUN apt-get update
RUN apt-get install -y \
    pkg-config \
    cmake \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy project files into the container
COPY main.py cagent.py ctools.py requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default port (8080, or change if needed)
EXPOSE 8080

# Set the environment variable for the port (adjust if needed)
ENV PORT 8080

# Start the Flask application with the correct port
CMD ["python", "main.py"]
```

Once we have these files ready, we’re just two steps away from deploying our agent as a serverless Cloud Run Service. Both of these steps will involve running commands in a terminal. If you’re not familiar with how to access a terminal within your environment, here’s a quick guide:

![](https://miro.medium.com/v2/resize:fit:594/1*6AtSKSBTZTT5QIJ-ZpeXDg.png)

- Step 1: build image from Dockerfile:

```
gcloud builds submit --tag gcr.io/<your-project-id>/onetwoagentimage .
```

This command will initiate a **Cloud Build** job that should build your image and register it in the **Cloud Artifacts Repository**:

![](https://miro.medium.com/v2/resize:fit:700/1*i1RE5WwIGbHB9OyL9vO2Og.png)

- create **Cloud Run** service for our agent from docker image!

```
gcloud run deploy onetwoagent --image gcr.io/<your-project-id>/onetwoagentimage
```

This next command will take care of everything needed to create your Cloud Run service. Be aware that when you run it, you’ll be asked whether you want to allow unauthenticated access to your service:

![](https://miro.medium.com/v2/resize:fit:700/1*Z1XwdCbs3wZUZMnWEwjrPg.png)

As you can see, I chose “YES” in this example because it’s an experimental setup. However, for production environments, **it’s crucial to ALWAYS enforce authentication to ensure the security of your service.**

![](https://miro.medium.com/v2/resize:fit:700/1*j-xM_IZf844MEugv5dYoXA.png)

When you see a similar screen, it signifies that your agent has been successfully deployed as a Cloud Run service and is ready to receive requests! Congratulations!

Now, let’s use this simple Python code to send an HTTP request to our service endpoint with the question: “What’s the exchange rate from US dollars to Polish currency today?”

```
import requests
url = "<your cloud run service URL>"
question = "What's the exchange rate from US dollars to Polish currency today?"  # Replace with your actual question
headers = {
    "Content-Type": "application/json"
}
data = {"question": question}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print("Answer:", result["answer"])  # Assuming the response format
else:
    print(f"Request failed with status code: {response.status_code}")
```

And here is the response from our agent service:

![](https://miro.medium.com/v2/resize:fit:700/1*l4981iO_EhrzBlW72U5dYw.png)

I’d like to add a few comments about this deployment. Firstly, Cloud Run isn’t just a compute resource for our Agent. You’ll likely want to monitor your service’s popularity and performance, tracking metrics like request count and latency. These are crucial insights for your DevOps or SRE engineers.

The good news is that Cloud Run automatically collects these core metrics and displays them on your service dashboard:

![](https://miro.medium.com/v2/resize:fit:700/0*8WcDWEt67l1jkEeu.png)

Let’s take a closer look at the “Container instance count” chart. Cloud Run’s serverless nature means you don’t have to worry about managing and scaling the infrastructure needed to handle requests.

In theory, Cloud Run can scale infinitely to accommodate any traffic, which is great news if your agent becomes wildly popular.

However, with scalability comes the need to manage costs and set limits. One way to do this is by defining the maximum number of container instances. But how many user requests can a single instance handle? This is configurable, with a maximum of 1000 concurrent requests per instance. By default, each instance can handle up to 80 requests simultaneously.

The diagram below illustrates how the maximum concurrent requests per instance setting directly impacts the number of instances required to handle a given load:

![](https://miro.medium.com/v2/resize:fit:700/0*5Ikwbp_pB2ZWInfJ.png)

With concurrency set to 1, each incoming request will be handled by a brand new container instance. However, with a concurrency of 80, each instance has 80 slots available to manage requests simultaneously. If the incoming traffic exceeds 80 requests, Cloud Run will automatically provision additional container instances to meet the demand, each with its own 80 slots.

As you can see, adjusting this setting allows you to fine-tune the balance between cost and performance. You can limit the maximum number of instances to control costs or increase the concurrent requests per instance to handle higher traffic with fewer instances.

While our new Cloud Run service currently receives 100% of the traffic, you can actually define multiple revisions within the service. Think of revisions as different versions of your agent. You can then control how much traffic is directed to each revision, making this a valuable feature for A/B testing or canary deployments of new iterations of your agent.

![](https://miro.medium.com/v2/resize:fit:700/0*UD99EESPAjvMcoHb.png)

If you would like to learn more about Cloud Run I highly recommend starting from the book: **Building Serverless Applications with Google Cloud Run: A Real-World Guide to Building Production-Ready Services** by [Wietse Venema](https://www.oreilly.com/library/view/building-serverless-applications/9781492057086/).

The key takeaway at this point is that our service is now live and ready to handle traffic, thanks to Cloud Run’s automatic scaling capabilities.

Deploying OneTwo agents using this DIY approach is not the only option. Another one is **Vertex AI’s Reasoning Engine** which provides a managed environment for deploying agents, streamlining the process significantly. With **Reasoning Engine**, deploying a new agent can be as simple as executing a create operation and providing the necessary dependencies for the agent and its tools:

![](https://miro.medium.com/v2/resize:fit:700/1*moTYClNz0r-WOPb8lj6N-g.png)

The combination of **OneTwo** and **Reasoning Engine** offers a compelling solution for efficient agent deployment, but we’ll delve into that exciting topic in a future article. **Stay tuned!**

**Summary:**

In this blog post, I’ve provided a step-by-step walkthrough of Google DeepMind’s OneTwo, a powerful Python library designed to simplify interactions with language and multimodal foundation models. We’ve explored numerous examples showcasing its key advantages:

- **Flexibility:** Developers can swap backends, choosing from various platforms like Google AI Studio API, Vertex AI API, Open AI API, and Local Gemma.
- **Caching:** OneTwo enables caching of model call results, speeding up re-execution of workflows and experiments.
- **Asynchronous Execution:** OneTwo can execute multiple calls in parallel, improving efficiency for independent tasks.
- **Prompt Templates:** Users can utilize Jinja2 syntax or concatenate composables to define templates with intermediate variables.
- **ReActAgent and PythonPlanningAgent:** These components enable multi-step tool use, enhancing the agent’s capabilities.
- **Deployment to Cloud Run:** User can deploy OneTwo agents as serverless Cloud Run services, allowing for easy scalability and monitoring.

***Please clap for this article if you enjoyed reading it. For more about google cloud, data science, data engineering, and AI/ML follow me on [LinkedIn](https://www.linkedin.com/in/lukasz-olejniczak-phd-1a75a613/).***

> This article is authored by Lukasz Olejniczak — AI Specialist at Google Cloud. The views expressed are those of the authors and don’t necessarily reflect those of Google.
>