# LangChain Tutorial in Python - Crash Course - Python Engineer

Column: https://www.python-engineer.com/posts/langchain-crash-course/
Processed: No
created on: September 7, 2023 5:50 PM

![langchain-crash-course.png](LangChain%20Tutorial%20in%20Python%20-%20Crash%20Course%20-%20Pyth%20c81e658641dc4fc78126c5fc5df4e636/langchain-crash-course.png)

**In this LangChain Crash Course you will learn how to build applications powered by large language models.**

LangChain is a framework for developing applications powered by language models. In this LangChain Crash Course you will learn how to build applications powered by large language models. We go over all important features of this framework.

- [GitHub repo](https://github.com/hwchase17/langchain)
- [Official Docs](https://python.langchain.com/en/latest/index.html)

## Overview:

- Installation
- LLMs
- Prompt Templates
- Chains
- Agents and Tools
- Memory
- Document Loaders
- Indexes

Try out all the code in this [Google Colab](https://colab.research.google.com/drive/1VOwJpcZqOXag-ZXi-52ibOx6L5Pw-YJi?usp=sharing).

## Installation

```
pip install langchain

```

## LLMs

LangChain provides a generic interface for many different LLMs. Most of them work via their API but you can also run local models.

See all [LLM providers](https://python.langchain.com/en/latest/modules/models/llms/integrations.html).

```
pip install openai

```

```
import os
os.environ["OPENAI_API_KEY"] ="YOUR_OPENAI_TOKEN"

```

## Prompt Templates

LangChain faciliates prompt management and optimization.

Normally, when you use an LLM in an application, you are not sending user input directly to the LLM. Instead, you need to take the user input and construct a prompt, and only then send that to the LLM.

A better prompt is this:

This can be achieved with `PromptTemplates`:

## Chains

Combine LLMs and Prompts in multi-step workflows.

## Agents and Tools

Agents involve an LLM making decisions about which cctions to take, taking that cction, seeing an observation, and repeating that until done.

When used correctly agents can be extremely powerful. In order to load agents, you should understand the following concepts:

- Tool: A function that performs a specific duty. This can be things like: Google Search, Database lookup, Python REPL, other chains. See available [Tools](https://python.langchain.com/en/latest/modules/agents/tools.html).
- LLM: The language model powering the agent.
- Agent: The agent to use. See also [Agent Types](https://python.langchain.com/en/latest/modules/agents/agents/agent_types.html).

## Memory

Add state to Chains and Agents.

Memory is the concept of persisting state between calls of a chain/agent. LangChain provides a standard interface for memory, a collection of memory implementations, and examples of chains/agents that use memory.

## Document Loaders

Combining language models with your own text data is a powerful way to differentiate them. The first step in doing this is to load the data into *documents* (i.e., some pieces of text). This module is aimed at making this easy.

See all [available Document Loaders](https://python.langchain.com/en/latest/modules/indexes/document_loaders.html).

## Indexes

Indexes refer to ways to structure documents so that LLMs can best interact with them. This module contains utility functions for working with documents

- Embeddings: An embedding is a numerical representation of a piece of information, for example, text, documents, images, audio, etc.
- Text Splitters: When you want to deal with long pieces of text, it is necessary to split up that text into chunks.
- Vectorstores: Vector databases store and index vector embeddings from NLP models to understand the meaning and context of strings of text, sentences, and whole documents for more accurate and relevant search results. See [available vectorstores](vectorstore: https://python.langchain.com/en/latest/modules/indexes/vectorstores.html).

## End-to-end example

Check out the [https://github.com/hwchase17/chat-langchain](https://github.com/hwchase17/chat-langchain) repo.

* These are affiliate link. By clicking on it you will not have any additional costs. Instead, you will support my project. Thank you! 🙏