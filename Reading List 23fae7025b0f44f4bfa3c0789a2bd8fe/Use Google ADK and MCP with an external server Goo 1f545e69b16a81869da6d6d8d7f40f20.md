# Use Google ADK and MCP with an external server | Google Cloud Blog

Column: https://cloud.google.com/blog/topics/developers-practitioners/use-google-adk-and-mcp-with-an-external-server
Processed: Yes
created on: May 16, 2025 12:15 PM

![11_-_Developers__Practitioners_a4Y5EGr.max-2600x2600.jpg](Use%20Google%20ADK%20and%20MCP%20with%20an%20external%20server%20Goo%201f545e69b16a81869da6d6d8d7f40f20/11_-_Developers__Practitioners_a4Y5EGr.max-2600x2600.jpg)

### Try Gemini 2.5

Our most intelligent model is now available on Vertex AI

[Try now](https://console.cloud.google.com/vertex-ai/studio/freeform)

For AI-powered agents to perform useful, real-world tasks, they need to reliably access tools and up-to-the-minute information that lives outside the base model. Anthropic’s Model Context Protocol (MCP) is designed to address this, providing a standardized way for agents to retrieve that crucial, external context needed to inform their responses and actions.

This is vital for developers who need to build and deploy sophisticated agents that can leverage enterprise data or public tools. But integrating agents built with Google's Agent Development Kit (ADK) to communicate effectively with an MCP server, especially one hosted externally, might present some integration challenges.

Today, we’ll guide you through developing ADK agents that connect to external MCP servers, initially using Server-Sent Events (SSE). We’ll take an example of an ADK agent leveraging MCP to access Wikipedia articles, which is a common use case to retrieve external specialised data. We will also introduce Streamable HTTP, the next-generation transport protocol designed to succeed SSE for MCP communications.

### **A quick refresher**

Before we start, let's make sure we all understand the following terms:

- 
    
    **SSE** enables servers to push data to clients over a persistent HTTP connection. In a typical setup for MCP, this involved using two distinct endpoints: one for the client to send requests to the server (usually via HTTP POST) and a separate endpoint where the client would establish an SSE connection (HTTP GET) to receive streaming responses and server-initiated messages.
    
- 
    
    **MCP** is an open standard designed to standardize how Large Language Models (LLMs) interact with external data sources, APIs and resources as agent tools, MCP aims to replace the current landscape of fragmented, custom integrations with a universal, standardized framework.
    
- 
    
    **Streamable HTTP** utilizes a single HTTP endpoint for both sending requests from the client to the server, and receiving responses and notifications from the server to the client.
    

**$300 in free credit to try Google Cloud developer tools**
Build and test your proof of concept with $300 in free credit for new customers. Plus, all customers get free monthly usage of 20+ products, including AI APIs.[Start building for free](http://console.cloud.google.com/freetrial?redirectPath=/welcome)

### **Step 1: Create an MCP server**

You need the following python packages installed in your virtual environment before proceeding. We will be using the [uv tool](https://docs.astral.sh/uv/) in this blog.

lang-py

Loading...

Here’s an explanation of the Python code `server.py`:

- 
    
    It creates an instance of an MCP server using `FastMCP`
    
- 
    
    It defines a tool called `extract_wikipedia_article` decorated with `@mcp.tool`
    
- 
    
    It configures an SSE transport mechanism `SseServerTransport` to enable real-time communication, typically for the MCP server interactions.
    
- 
    
    It creates a web application instance using the [Starlette framework](https://www.starlette.io/) and defines two routes, `message` and `sse`.
    
- 
    
    You can read more about SSE transport protocol [here](https://modelcontextprotocol.io/specification/2024-11-05/basic/transports#http-with-sse).
    

lang-py

Loading...

To start the server, you can run the command `uv run [server.py](http://server.py/)`.

Bonus tip, to debug the server using [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector), execute the command `uv run mcp dev server.py`.

### **Step 2: Attach the MCP server while creating ADK agents**

The following explains the Python code in the file `agent.py`:

- 
    
    Uses `MCPToolset.from_server` with `SseServerParams` to establish a SSE connection to a URI endpoint. For this demo we will use `http://localhost:8001/sse`, but in production this would be a remote server.
    
- 
    
    Create an ADK Agent and call `get_tools_async` to get the tools from the MCP server.
    

lang-py

Loading...

### **Step 3: Test your agent**

We will use the ADK developer tool to test the agent.

Create the following directory structure:

lang-py

Loading...

The content for `__init__.py` and `.env` are as follows:

lang-py

Loading...

lang-py

Loading...

Start the UI with the following command:

lang-py

Loading...

This will open up the ADK developer tool interface as shown below:

### **Streamable HTTP**

It is worth noting that in March 2025, MCP released a new transport protocol called [Streamable HTTP](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http). The Streamable HTTP transport allows a server to function as an independent process managing multiple client connections via HTTP POST and GET requests. Servers can optionally implement Server-Sent Events (SSE) for streaming multiple messages, enabling support for basic MCP servers as well as more advanced servers with streaming and server-initiated communication.

The following code demonstrates how to implement a Streamable HTTP server, where the tool `extract_wikipedia_article` will return a dummy string to simplify the code.

lang-py

Loading...

You can start the Streamable HTTP MCP server using by running the following:

lang-py

Loading...

To debug with [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector), select `Streamable HTTP` and fill in the MCP Server URL [`http://localhost:3000/mcp`](http://localhost:3000/mcp).

### **Authentication**

For production deployments of MCP servers, robust authentication is a critical security consideration. As this field is under active development at the time of writing, we recommend referring to the [MCP specification on Authentication](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization) for more information.

For an enterprise grade API governance system which, similar to MCP, can generate agent tools:

- 
    
    Apigee centralizes and manages any APIs, with full control, versioning, and governance
    
- 
    
    API Hub organizes metadata for any API and documentation
    
- 
    
    Application Integrations support many existing API connections with user access control support
    
- 
    
    ADK supports these [Google Cloud Managed Tools](https://google.github.io/adk-docs/tools/google-cloud-tools/) with about the same number of lines of code
    

### Get started

To get started today, read the [documentation](https://google.github.io/adk-docs/) for ADK. You can create your own Agent with access to available MCP servers in the open community with ADK.