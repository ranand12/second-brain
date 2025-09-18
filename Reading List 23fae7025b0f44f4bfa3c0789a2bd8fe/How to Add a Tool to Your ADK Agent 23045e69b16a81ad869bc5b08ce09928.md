# How to Add a Tool to Your ADK Agent

Column: https://wietsevenema.eu/blog/2025/adding-a-tool-to-your-adk-agent/
Processed: Yes
created on: July 14, 2025 1:49 PM

In the [previous post](https://wietsevenema.eu/blog/2025/a-fast-way-to-get-started-with-adk/), you created your first AI agent with the Agent Development Kit (ADK). Now, you can give your agent new abilities by adding tools.

## Adding a URL Fetcher

Let's create a Python function that can fetch the content of a URL and add it to your agent's toolbox.

1. Install the `httpx` library. From your `agent-project` directory, run the following command:
2. Open the `demo-agent/agent.py` file.
3. Add the `import httpx` line at the top of the file.
4. Create the `fetch_url` function. This function takes a string `url` as input and returns the text content of the response.
    
    ```
    def fetch_url(url: str) -> str:
        """Fetches the content of a URL."""
        with httpx.Client(follow_redirects=True) as client:
            response = client.get(url)
            response.raise_for_status()
            return response.text
    
    ```
    

Your `agent.py` should now look like this:

```
from google.adk.agents import Agent
import httpx

def fetch_url(url: str) -> str:
    """Fetches the content of a URL."""
    with httpx.Client(follow_redirects=True) as client:
        response = client.get(url)
        response.raise_for_status()
        return response.text

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[fetch_url]
)

```

## Testing Your Tool

Test your tool using the ADK web UI.

1. From your `agent-project` directory, (re)start the web UI: The restart is required because it doesn't reload changed files automatically
2. In the chat interface, ask the agent to summarize the content of a URL. For example: *"What's on wietsevenema.eu?"*

The agent calls your `fetch_url` function, receives the HTML content, and then summarizes it to answer your question. The web UI's conversation panel displays the function call and the final summarized response.

![](https://wietsevenema.eu/blog/2025/adding-a-tool-to-your-adk-agent/example.png)

## Why Tools Matter

Large Language Models (LLMs) used in isolation have some key limitations. Their knowledge is frozen at the time they were trained, and they cannot interact directly with the outside world. A key development that enables a more dynamic approach is *tool calling*.

## How Tools Work

1. With each prompt, the application provides the LLM with a list of available tools and their descriptions.
2. The LLM uses these descriptions to decide which tool (if any) can help fulfill the prompt.
3. Instead of running the tool itself, the LLM generates a structured output that specifies which tool it wants to use and what information to pass to it.
4. The application code receives this output, executes the actual tool, and then calls the LLM a second time, providing the tool's result as part of the new prompt.
5. The LLM then uses the tool's output to generate its final response to you.

## The Importance of a Good Description

The docstring you write for your function (in this example, `"""Fetches the content of a URL."""`) is the primary way the LLM understands what the tool does. A clear, concise, and accurate description is crucial.

*Why it's important:*

- **Discovery:** The LLM uses the description to determine if the tool is relevant to the user's request. A vague description might cause the model to overlook your tool when it's needed, or use it incorrectly.
- **Parameter Mapping:** The description, along with the function's parameter names and types, helps the model understand what arguments to pass. For your `fetch_url` function, the model knows it needs to provide a string for the `url` parameter because ADK tells it about it.

*Common failure modes:*

- **Vague or Ambiguous Descriptions:** If the description is unclear, the model might not know when to use the tool. For instance, `"Returns items in display order"` doesn't specify *what items* are returned and what *display order* exactly means.
- **Mismatch between Description and Functionality:** If the description says the tool does one thing but the code does another, the model will be confused and likely produce incorrect or unexpected results.
- **Confusing Parameter Names:** If you use non-descriptive variable names, the model may struggle to provide the correct inputs, leading to errors.

You've learned how to add a tool to your ADK agent. By providing a Python function with a clear description, you can build agents that can fetch data, interact with APIs, and perform a wide range of tasks.