# LangChain Chat with Custom Tools, Functions and Memory | by gil fernandes | Medium

Column: https://medium.com/@gil.fernandes/langchain-chat-with-custom-tools-functions-and-memory-e34daa331aa7
Processed: No
created on: April 4, 2024 10:13 PM

# LangChain Chat with Custom Tools, Functions and Memory

![](https://miro.medium.com/v2/resize:fill:88:88/0*A8uRGeFcAOrLT17b.jpg)

[gil fernandes](https://medium.com/@gil.fernandes?source=post_page-----e34daa331aa7--------------------------------)

·

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F8585469bc295&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40gil.fernandes%2Flangchain-chat-with-custom-tools-functions-and-memory-e34daa331aa7&user=gil+fernandes&userId=8585469bc295&source=post_page-8585469bc295----e34daa331aa7---------------------post_header-----------)

7 min read

·

Jul 11, 2023

Photo by [Barn Images](https://unsplash.com/@barnimages?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

[](https://miro.medium.com/v2/resize:fit:700/0*hEqiQYXIj4yeJR3g)

In this story we are going to explore how you can create a simple web based chat application that communicates with a private REST API, uses [OpenAI functions](https://openai.com/blog/function-calling-and-other-api-updates) and [conversational memory](https://python.langchain.com/docs/modules/memory/).

We will be using again the [LangChain framework](https://python.langchain.com/) which provides a great infrastructure for interacting with [Large Language Models](https://machinelearningmastery.com/what-are-large-language-models/) (LLM).

The Agent we are going to describe in this post is going to use these tools:

- [Wikipedia](https://www.wikipedia.org/) with LangChain’s [WikipediaAPIWrapper](https://python.langchain.com/docs/modules/agents/tools/integrations/wikipedia)
- [DuckDuckGo Search](https://duckduckgo.com/) with LangChain’s [DuckDuckGoSearchAPIWrapper](https://python.langchain.com/docs/modules/agents/tools/integrations/ddg)
- Pubmed with [PubMedAPIWrapper](https://github.com/hwchase17/langchain/blob/master/langchain/tools/pubmed/tool.py)
- LLM Math Chain with [LLMMathChain](https://github.com/hwchase17/langchain/blob/master/langchain/chains/llm_math/base.py)
- Events API with a custom implementation which we describe later.

The agent will have two user interfaces:

- A [Streamlit](https://streamlit.io/) based tweb client
- A command line interface

# **OpenAI functions**

One of the main problems when dealing with responses from a LLM like [ChatGPT](https://openai.com/blog/chatgpt) is that the responses are not completely predictable. When you try to parse the responses there might be slight variations in the output which make parsing by programmatic tools error prone. Since LangChain agents send user input to an LLM and expect it to route the output to a specific tool (or function), the agents need to be able to parse predictable output.

To address this problem OpenAI introduced on June 13th of 2023 “Function Calling” which allows developers to describe the JSON output describing which functions (in LangChain speak: tools) to call based on a specific input.

The approach initially used by LangChain agents — like e.g. the ZERO_SHOT_REACT_DESCRIPTION agent — uses prompt engineering to route messages to the right tools. This approach is potentially less accurate and slower than the approach using OpenAI functions.

As of the time of writing this blog the models which support this feature are:

- gpt-4–0613
- gpt-3.5-turbo-0613 (this includes gpt-3.5-turbo-16k-0613, which we used for your playground chat agent)

Here are some examples given by OpenAI on how function calling works:

> Convert queries such as “Email Anya to see if she wants to get coffee next Friday” to a function call like send_email(to: string, body: string), or “What’s the weather like in Boston?” to get_current_weather(location: string, unit: 'celsius' | 'fahrenheit')
> 

Internally the instructions about the function and its parameters are injected into the system message.

The API endpoint is:

POST [https://api.openai.com/v1/chat/completions](https://api.openai.com/v1/chat/completions)

And you can find the low level API details here:

## [OpenAI Platform](https://platform.openai.com/docs/api-reference/chat?source=post_page-----e34daa331aa7--------------------------------)

### [Explore developer resources, tutorials, API docs, and dynamic examples to get the most out of OpenAI's platform.](https://platform.openai.com/docs/api-reference/chat?source=post_page-----e34daa331aa7--------------------------------)

[platform.openai.com](https://platform.openai.com/docs/api-reference/chat?source=post_page-----e34daa331aa7--------------------------------)

# The Agent Loop

As far as the author of the blog could see the agent loop is the same as for most agents. The [basic agents code](https://github.com/hwchase17/langchain/blob/master/langchain/agents/agent.py) is similar to the ZERO_SHOT_REACT_DESCRIPTION agent. So the agent loop still could be depicted with this diagramme:

The agent loop

![](https://miro.medium.com/v2/resize:fit:1000/1*1uPNZZN3KhoRtbVWbNJooA.png)

# Custom and LangChain Tools

A LangChain agent uses tools (corresponds to OpenAPI functions). LangChain (v0.0.220) comes out of the box with a plethora of tools which allow you to connect to all kinds of paid and free services or interactions, like e.g:

- arxiv (free)
- azure_cognitive_services
- bing_search
- brave_search
- ddg_search
- file_management
- gmail
- google_places
- google_search
- google_serper
- graphql
- human interaction
- jira
- json
- metaphor_search
- office365
- openapi
- openweathermap
- playwright
- powerbi
- pubmed
- python
- requests
- scenexplain
- searx_search
- shell
- sleep
- spark_sql
- sql_database
- steamship_image_generation
- vectorstore
- wikipedia (free)
- wolfram_alpha
- youtube
- zapier

We will show in this blog how you can create a custom tool to access a custom REST API.

# Conversational Memory

This type of memory comes in handy when you want to remember items from previous inputs. For example: if you ask “Who is Albert Einstein?” and then subsequently “Who were his mentors?”, then conversational memory will help the agent to remember that “his” refers to “Albert Einstein”.

Here is [LangChain’s documentation on Memory](https://python.langchain.com/docs/modules/memory/).

# An Agent with Functions, Custom Tool and Memory

Our agent can be found in a Git repository:

## [GitHub - gilfernandes/chat_functions: Simple playground chat app that interacts with OpenAI's…](https://github.com/gilfernandes/chat_functions.git?source=post_page-----e34daa331aa7--------------------------------)

### [Simple playground chat app that interacts with OpenAI's functions with memory and custom tools. - GitHub …](https://github.com/gilfernandes/chat_functions.git?source=post_page-----e34daa331aa7--------------------------------)

[github.com](https://github.com/gilfernandes/chat_functions.git?source=post_page-----e34daa331aa7--------------------------------)

In order to get it to run, please install [Conda](https://docs.conda.io/en/latest/) first.

Then create the following environment and install the following libraries:

```
conda activate langchain_streamlit
pip install langchain
pip install prompt_toolkit
pip install wikipedia
pip install arxiv
pip install python-dotenv
pip install streamlit
pip install openai
pip install duckduckgo-search
```

Then create an *.env* file with this content:

```
OPENAI_API_KEY=<key>
```

Then you can run the command line version of the agent using:

```
python .\agent_cli.py
```

And the Streamlit version can be run with this command on port 8080:

```
streamlit run ./agent_streamlit.py --server.port 8080
```

Here are some screenshots of the tool:

Using a custom agent

![](https://miro.medium.com/v2/resize:fit:1000/1*YPX5Mv04aIquOQto_kwxgA.png)

The UI shows which tool (OpenAI function) is being used and which input was sent to it.

Using Arxiv Tool

![](https://miro.medium.com/v2/resize:fit:1000/1*WIWqQYtHr8E4ISytsVPv4w.png)

Using the calculator

![](https://miro.medium.com/v2/resize:fit:1000/1*sZETPsf0ZpFeItCxuZGMQg.png)

Using Wikipedia

![](https://miro.medium.com/v2/resize:fit:1000/1*x1GxFuwfgULvWM1tNv0w4Q.png)

# Code Details

The code has the following main parts:

## Agent Setup

In the following piece of code you have to setup the agent with its tools memory:

```
def setup_agent() -> AgentExecutor:
    """
    Sets up the tools for a function based chain.
    We have here the following tools:
    - wikipedia
    - duduckgo
    - calculator
    - arxiv
    - events (a custom tool)
    - pubmed
    """
    cfg = Config()
    duckduck_search = DuckDuckGoSearchAPIWrapper()
    wikipedia = WikipediaAPIWrapper()
    pubmed = PubMedAPIWrapper()
    events = tools_wrappers.EventsAPIWrapper()
    events.doc_content_chars_max=5000
    llm_math_chain = LLMMathChain.from_llm(llm=cfg.llm, verbose=False)
    arxiv = ArxivAPIWrapper()
    tools = [
        Tool(
            name = "Search",
            func=duckduck_search.run,
            description="useful for when you need to answer questions about current events. You should ask targeted questions"
        ),
        Tool(
            name="Calculator",
            func=llm_math_chain.run,
            description="useful for when you need to answer questions about math"
        ),
        Tool(
            name="Wikipedia",
            func=wikipedia.run,
            description="useful when you need an answer about encyclopedic general knowledge"
        ),
        Tool(
            name="Arxiv",
            func=arxiv.run,
            description="useful when you need an answer about encyclopedic general knowledge"
        ),
        # This is the custom tool. Note that the OpenAPI Function parameters are inferred via analysis of the `events.run`` method
        StructuredTool.from_function(
            func=events.run,
            name="Events",
            description="useful when you need an answer about meditation related events in the united kingdom"
        ),
        StructuredTool.from_function(
            func=pubmed.run,
            name='PubMed',
            description='Useful tool for querying medical publications'
        )
    ]
    agent_kwargs, memory = setup_memory()

    return initialize_agent(
        tools,
        cfg.llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=False,
        agent_kwargs=agent_kwargs,
        memory=memory
    )
```

In this function the memory is setup:

```
def setup_memory() -> Tuple[Dict, ConversationBufferMemory]:
    """
    Sets up memory for the open ai functions agent.
    :return a tuple with the agent keyword pairs and the conversation memory.
    """
    agent_kwargs = {
        "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
    }
    memory = ConversationBufferMemory(memory_key="memory", return_messages=True)

    return agent_kwargs, memory
```

And this is the mode the agent is:

```
class Config():
    """
    Contains the configuration of the LLM.
    """
    model = 'gpt-3.5-turbo-16k-0613'
    llm = ChatOpenAI(temperature=0, model=model)
```

This is the custom tool that calls a simple REST API:

```
import requests
import urllib.parse

from typing import Dict, Optional
from pydantic import BaseModel, Extra

class EventsAPIWrapper(BaseModel):
    """Wrapper around a custom API used to fetch public event information.

    There is no need to install any package to get this to work.
    """

    offset: int = 0
    limit: int = 10
    filter_by_country: str = "United Kingdom"
    doc_content_chars_max: int = 4000

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    def run(self, query: str) -> str:
        """Run Events search and get page summaries."""
        encoded_query =  urllib.parse.quote_plus(query)
        encoded_filter_by_country =  urllib.parse.quote_plus(self.filter_by_country)
        response = requests.get(f"https://events.brahmakumaris.org/events-rest/event-search-v2?search={encoded_query}" +
                     f"&limit=10&offset={self.offset}&filterByCountry={encoded_filter_by_country}&includeDescription=true")
        if response.status_code >= 200 and response.status_code < 300:
            json = response.json()
            summaries = [self._formatted_event_summary(e) for e in json['events']]
            return "\n\n".join(summaries)[: self.doc_content_chars_max]
        else:
            return f"Failed to call events API with status code {response.status_code}"

    @staticmethod
    def _formatted_event_summary(event: Dict) -> Optional[str]:
        return (f"Event: {event['name']}\n" +
                f"Start: {event['startDate']} {event['startTime']}\n" +
                f"End: {event['endDate']} {event['endTime']}\n" +
                f"Venue: {event['venueAddress']} {event['postalCode']} {event['locality']} {event['countryName']}\n" +
                f"Event Description: {event['description']}\n" +
                f"Event URL: https://brahmakumaris.uk/event/?id={event['id']}\n"
        )
```

## Agent CLI Loop

The agent CLI loop is uses a simple while loop:

```
from prompt_toolkit import HTML, prompt, PromptSession
from prompt_toolkit.history import FileHistory

from langchain.input import get_colored_text
from dotenv import load_dotenv
from langchain.agents import AgentExecutor

import langchain
from callbacks import AgentCallbackHandler

load_dotenv()
from chain_setup import setup_agent

langchain.debug = True

if __name__ == "__main__":

    agent_executor: AgentExecutor = setup_agent()

    session = PromptSession(history=FileHistory(".agent-history-file"))
    while True:
        question = session.prompt(
            HTML("<b>Type <u>Your question</u></b>  ('q' to exit): ")
        )
        if question.lower() == 'q':
            break
        if len(question) == 0:
            continue
        try:
            print(get_colored_text("Response: >>> ", "green"))
            print(get_colored_text(agent_executor.run(question, callbacks=[AgentCallbackHandler()]), "green"))
        except Exception as e:
            print(get_colored_text(f"Failed to process {question}", "red"))
            print(get_colored_text(f"Error {e}", "red"))
```

## Streamlit API Application

This is the Streamlit application which renders the UI displayed above:

```
import streamlit as st
from dotenv import load_dotenv

from langchain.agents import AgentExecutor

import callbacks

load_dotenv()

from chain_setup import setup_agent

QUESTION_HISTORY: str = 'question_history'

def init_stream_lit():
    title = "Chat Functions Introduction"
    st.set_page_config(page_title=title, layout="wide")
    agent_executor: AgentExecutor = prepare_agent()
    st.header(title)
    if QUESTION_HISTORY not in st.session_state:
        st.session_state[QUESTION_HISTORY] = []
    intro_text()
    simple_chat_tab, historical_tab = st.tabs(["Simple Chat", "Session History"])
    with simple_chat_tab:
        user_question = st.text_input("Your question")
        with st.spinner('Please wait ...'):
            try:
                response = agent_executor.run(user_question, callbacks=[callbacks.StreamlitCallbackHandler(st)])
                st.write(f"{response}")
                st.session_state[QUESTION_HISTORY].append((user_question, response))
            except Exception as e:
                st.error(f"Error occurred: {e}")
    with historical_tab:
        for q in st.session_state[QUESTION_HISTORY]:
            question = q[0]
            if len(question) > 0:
                st.write(f"Q: {question}")
                st.write(f"A: {q[1]}")

def intro_text():
    with st.expander("Click to see application info:"):
        st.write(f"""Ask questions about:
- [Wikipedia](https://www.wikipedia.org/) Content
- Scientific publications ([pubmed](https://pubmed.ncbi.nlm.nih.gov) and [arxiv](https://arxiv.org))
- Mathematical calculations
- Search engine content ([DuckDuckGo](https://duckduckgo.com/))
- Meditation related events (Custom Tool)
    """)

@st.cache_resource()
def prepare_agent() -> AgentExecutor:
    return setup_agent()

if __name__ == "__main__":
    init_stream_lit()
```

# Summary

[OpenAI functions](https://openai.com/blog/function-calling-and-other-api-updates) can now be easily used with LangChain. And this seems to be a much better method (faster and more accurate) to create agents compared to prompt based approaches.

[OpenAI functions](https://openai.com/blog/function-calling-and-other-api-updates) can also be easily integrated with memory and custom tools too. There is no excuse to not use [OpenAI functions](https://openai.com/blog/function-calling-and-other-api-updates) for the type of agent described in this blog.