# LangChain, Gemini & MongoDB Chatbot Guide

Column: https://cckeh.hashnode.dev/building-chatbots-with-memory-capabilities-a-comprehensive-tutorial-with-langchain-langgraph-gemini-ai-and-mongodb
Processed: Yes
created on: January 20, 2025 11:21 AM

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1733757407279/6da6b41e-83fc-461f-9e31-dff97820bf6b.png?w=1600&h=840&fit=crop&crop=entropy&auto=compress,format&format=webp)

## Table of contents

- [Introduction](https://cckeh.hashnode.dev/building-chatbots-with-memory-capabilities-a-comprehensive-tutorial-with-langchain-langgraph-gemini-ai-and-mongodb#heading-introduction)
- [Key Components of Our Chatbot](https://cckeh.hashnode.dev/building-chatbots-with-memory-capabilities-a-comprehensive-tutorial-with-langchain-langgraph-gemini-ai-and-mongodb#heading-key-components-of-our-chatbot)
- [Code Walkthrough](https://cckeh.hashnode.dev/building-chatbots-with-memory-capabilities-a-comprehensive-tutorial-with-langchain-langgraph-gemini-ai-and-mongodb#heading-code-walkthrough)
    - [Step 1: Import Required Libraries](https://cckeh.hashnode.dev/building-chatbots-with-memory-capabilities-a-comprehensive-tutorial-with-langchain-langgraph-gemini-ai-and-mongodb#heading-step-1-import-required-libraries)
    - [Step 2: Define the State Schema](https://cckeh.hashnode.dev/building-chatbots-with-memory-capabilities-a-comprehensive-tutorial-with-langchain-langgraph-gemini-ai-and-mongodb#heading-step-2-define-the-state-schema)
    - [Step 3: Configure the AI Model](https://cckeh.hashnode.dev/building-chatbots-with-memory-capabilities-a-comprehensive-tutorial-with-langchain-langgraph-gemini-ai-and-mongodb#heading-step-3-configure-the-ai-model)
    - [Step 4: Define Prompt Templates](https://cckeh.hashnode.dev/building-chatbots-with-memory-capabilities-a-comprehensive-tutorial-with-langchain-langgraph-gemini-ai-and-mongodb#heading-step-4-define-prompt-templates)
    - [Step 5: Implement the Workflow](https://cckeh.hashnode.dev/building-chatbots-with-memory-capabilities-a-comprehensive-tutorial-with-langchain-langgraph-gemini-ai-and-mongodb#heading-step-5-implement-the-workflow)
    - [Step 6: Setup Trimmer](https://cckeh.hashnode.dev/building-chatbots-with-memory-capabilities-a-comprehensive-tutorial-with-langchain-langgraph-gemini-ai-and-mongodb#heading-step-6-setup-trimmer)
    - [Step 7: Call the AI Model](https://cckeh.hashnode.dev/building-chatbots-with-memory-capabilities-a-comprehensive-tutorial-with-langchain-langgraph-gemini-ai-and-mongodb#heading-step-7-call-the-ai-model)
    - [Step 8: Invoke Function](https://cckeh.hashnode.dev/building-chatbots-with-memory-capabilities-a-comprehensive-tutorial-with-langchain-langgraph-gemini-ai-and-mongodb#heading-step-8-invoke-function)
    - [Step 9: Main Execution](https://cckeh.hashnode.dev/building-chatbots-with-memory-capabilities-a-comprehensive-tutorial-with-langchain-langgraph-gemini-ai-and-mongodb#heading-step-9-main-execution)
- [How It Works](https://cckeh.hashnode.dev/building-chatbots-with-memory-capabilities-a-comprehensive-tutorial-with-langchain-langgraph-gemini-ai-and-mongodb#heading-how-it-works)
    - [Output](https://cckeh.hashnode.dev/building-chatbots-with-memory-capabilities-a-comprehensive-tutorial-with-langchain-langgraph-gemini-ai-and-mongodb#heading-output)
- [Conclusion](https://cckeh.hashnode.dev/building-chatbots-with-memory-capabilities-a-comprehensive-tutorial-with-langchain-langgraph-gemini-ai-and-mongodb#heading-conclusion)

## Introduction

Chatbots are revolutionizing our interactions with technology. In this blog, we’ll guide you through building a chatbot using **LangChain**, **Gemini AI**, **LangGraph**, and **MongoDB**. This system will have memory capabilities, allowing it to retain conversation history. This beginner-friendly walkthrough will cover key concepts and provide a detailed code explanation.

## **Key Components of Our Chatbot**

1. **LangChain**: A framework for making building AI-powered applications with language models easy. This includes the easy integration of prompts, memory, and custom workflows.
2. **LangGraph**: It is a tool that extends LangChain to stateful workflows by making use of graph-based models. This offers systematic management of conversation states.
3. **Memory in Chatbots**: Memory lets chatbots recall previous interactions to offer a coherent and contextual conversational experience.
4. **MongoDB**: A NoSQL database to store the chat history persistently so that the chatbot has long-term memory even beyond a session.

## **Code Walkthrough**

Below is the complete code for our chatbot. Let's break it down step-by-step.

Code is available on my [GitHub](https://github.com/CC-KEH/GenAI-Tutorials/blob/main/langchain_chatbot_with_memory.py).

### **Step 1: Import Required Libraries**

The first part of the code imports the necessary libraries:

```
import os
import getpass
from typing import Sequence
from typing_extensions import Annotated, TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    trim_messages,
    BaseMessage,
)
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, StateGraph
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_mongodb.chat_message_histories import MongoDBChatMessageHistory
from langgraph.graph.message import add_messages

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

```

These libraries manage:

- **Message handling** (LangChain Core).
- **Memory management** (LangGraph and MongoDB).
- **Model interactions** (LangChain Google Generative AI).

### **Step 2: Define the State Schema**

A state schema is like a blueprint that defines how we organize and store information in our chatbot. It helps the chatbot keep track of important details, such as the messages exchanged and other constraints.

In our example, the state schema contains two major parts:

- **Messages:** This is a list holding all messages that have been sent and received during the conversation. One can think of each message as a piece of the chat history.
- **Language:** This is a simple text field that stores the user's preferred language for communication. This is to ensure that the chatbot answers back in the correct language.

```
class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    language: str

```

### **Step 3: Configure the AI Model**

The `Model` class initializes the chatbot's core functionality:

```
class Model:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            # If you wish to send api key here, then google_api_key="xxxx"
        )

```

- **Gemini 1.5 Flash**: This is a light-weight, multi-modal foundation model by Google, built for high volume, high frequency tasks. Issues with Gemini Pro arise while handling chat history.
- **Temperature**: Controls the randomness of responses.

### **Step 4: Define Prompt Templates**

The chatbot uses a prompt template to define its behavior:

```
self.prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability in {language}.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

```

This will be helpful in case when we only want our chatbot to answer the user's query if they are relevant to the purpose of the chatbot.

### **Step 5: Implement the Workflow**

LangGraph’s `StateGraph` enables systematic state management:

```
self.workflow = StateGraph(state_schema=State)
self.workflow.add_edge(START, "model")
self.workflow.add_node("model", self.call_model)
self.memory = MemorySaver()
self.app = self.workflow.compile(checkpointer=self.memory)

```

1. `self.workflow = StateGraph(state_schema=State)` 
    - This line creates a new workflow called `workflow` using a `StateGraph`. A `StateGraph` is a structure that helps in managing the flow of data and actions in a program. **The** `state_schema=State` **part means that the workflow will use a specific format or structure for the data it will handle, defined by** `State`**.**
2. `self.workflow.add_edge(START, "model")` 
    - Here, an "edge" which is similar to a connection or a path is added to the workflow. This edge connects the start point which has been marked by `START` to a node called `"model"`. Thus, when this workflow begins, it goes to the `"model"` part.
3. `self.workflow.add_node("model", self.call_model`) 
    - This line introduces a new "node" (which is a specific task or function) into the workflow. The node is named `"model"` and is linked to a function called `self.call_model`. This means that when the workflow reaches the `"model"` node, it will execute the `call_model` function.
4. `self.memory = MemorySaver()` 
    - This line establishes a memory storage system called `memory` with the `MemorySaver`. The `MemorySaver` is a tool which allows the workflow to keep track of its state so it can remember information between steps or runs.
5. `self.app = self.workflow.compile(checkpointer=self.memory)` 
    - Finally, this line compiles the workflow into a runnable application called `app`. The `checkpointer=self.memory` part means that the workflow will use the `MemorySaver` to keep track of its state while it runs. This allows the application to save and restore its progress if needed.

### **Step 6: Setup Trimmer**

```
self.trimmer = trim_messages(
            max_tokens=65,
            strategy="last",
            token_counter=self.model,
            include_system=True,
            allow_partial=False,
            start_on="human",
        )

```

Here we initialize `self.trimmer` to handle message histories, with up to 65 tokens while keeping the most recent messages, including system messages, and ensuring the history starts with a human message. It uses the model for token counting and does not allow partial (incomplete) messages .

### **Step 7: Call the AI Model**

The `call_model` function processes inputs, generates responses, and updates memory:

```
def call_model(self, state: State):
    if not state["messages"] or len(state["messages"]) == 1:
        state["messages"] = self.chat_message_history.messages + state["messages"]
    print(state["messages"])
    trimmed_messages = self.trimmer.invoke(state["messages"])
    prompt = self.prompt_template.invoke(
        {"messages": trimmed_messages, "language": state["language"]}
    )
    response = self.model.invoke(prompt)

    self.chat_message_history.add_user_message(prompt.messages[-1].content)
    self.chat_message_history.add_ai_message(response.content)

    return {"messages": [response]}

```

This function:

1. Retrieve old messages from memory, retrieve old messages from memory or MongoDB in case a new session has started.
2. Trim the messages to fit token limits, trim the messages so that they don't go over token limits for optimal performance.
3. Send the prompt to Gemini AI and update MongoDB.

### **Step 8: Invoke Function**

```
def invoke(self, query, config, chat_message_history):
    self.chat_message_history = chat_message_history
    input_messages = [HumanMessage(query)]
    response = self.app.invoke(
            {"messages": input_messages, "language": "en"}, config
    )
    return response["messages"][-1].content

```

This function:

- Sends a user query `query` to the model or service using the `invoke` method of our `app`.
- This further involves wrapping the query within an instance of the `HumanMessage` object and sending it with other input messages.
- The `chat_message_history` parameter is an object which ensures chat histories are persistently stored in a MongoDB database and can be retrieved later, enabling continuity across sessions.
- Finally, it returns the content of the last response message.

### **Step 9: Main Execution**

The main block handles multiple users and demonstrates memory persistence:

```
if __name__ == "__main__":
    model = Model()
    no_of_users = input("Enter the number of users: ")

    # Create memory with initial queries
    for i in range(int(no_of_users)):
        query = input(f"Enter your query 1 for user{i+1}: ")
        config = {"configurable": {"thread_id": "user" + str(i)}}
        chat_message_history = MongoDBChatMessageHistory(
            session_id="user" + str(i),
            connection_string="mongodb://localhost:27017",
            database_name="my_db",
            collection_name="chat_histories",
        )
        print(model.invoke(query, config, chat_message_history))

    # Check memory with new queries
    for i in range(int(no_of_users)):
        query = input(f"Enter your query 2 for user{i+1}: ")
        config = {"configurable": {"thread_id": "user" + str(i)}}
        chat_message_history = MongoDBChatMessageHistory(
            session_id="user" + str(i),
            connection_string="mongodb://localhost:27017",
            database_name="my_db",
            collection_name="chat_histories",
        )
        print(model.invoke(query, config, chat_message_history))

```

## **How It Works**

1. **User Input**: The chatbot captures queries from multiple users.
2. **Chat History**: Retrieves and updates conversation logs in MongoDB.
3. **AI Interaction**: Processes queries using Gemini AI.
4. **Memory**: Ensures continuity across sessions.

### **Output**

Interaction with Chatbot

Chat History in MongoDB

## **Conclusion**

This chatbot shows the might of LangChain, LangGraph, Gemini AI, and MongoDB when integrated with memory. This makes it deliver context-aware and personalized conversations. I hope you find this guide helpful. If so, please like and follow. ❤️

## Subscribe to our newsletter

Read articles from **My Blogs** directly inside your inbox. Subscribe to the newsletter, and don't miss out.

### Did you find this article valuable?

Support **My Blogs** by becoming a sponsor. Any amount is appreciated!

[Learn more about Hashnode Sponsors](https://hashnode.com/sponsors)