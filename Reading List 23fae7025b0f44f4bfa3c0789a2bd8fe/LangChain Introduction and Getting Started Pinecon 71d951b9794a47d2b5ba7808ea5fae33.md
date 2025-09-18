# LangChain: Introduction and Getting Started | Pinecone

Column: https://www.pinecone.io/learn/series/langchain/langchain-intro/
Processed: No
created on: March 31, 2024 7:52 PM

**L**arge **L**anguage **M**odels (LLMs) entered the world stage with the release of OpenAI’s GPT-3 in 2020 [1]. Since then, they’ve enjoyed a steady growth in popularity.

That is until late 2022. Interest in LLMs and the broader discipline of generative AI has skyrocketed. The reasons for this are likely the continuous upward momentum of significant advances in LLMs.

We saw the dramatic news about Google’s *“sentient”* LaMDA chatbot. The first high-performance and *open-source* LLM called BLOOM was released. OpenAI released their next-generation text embedding model and the next generation of *“GPT-3.5”* models.

After all these giant leaps forward in the LLM space, OpenAI released *ChatGPT* — thrusting LLMs into the spotlight.

[LangChain](https://github.com/hwchase17/langchain) appeared around the same time. Its creator, Harrison Chase, made the first commit in late October 2022. Leaving a short couple of months of development before getting caught in the LLM wave.

Despite being early days for the library, it is already packed full of incredible features for building amazing tools around the core of LLMs. In this article, we’ll introduce the library and start with the most straightforward component offered by LangChain — LLMs.

[](https://www.notion.so'https://i.ytimg.com/vi/nE2skSRWTTs/hqdefault.jpg')

## LangChain

At its core, LangChain is a framework built around LLMs. We can use it for chatbots, [**G**enerative](https://www.pinecone.io/learn/openai-gen-qa/) [**Q**uestion-**A**nswering (GQA)](https://www.pinecone.io/learn/openai-gen-qa/), summarization, and much more.

The core idea of the library is that we can *“chain”* together different components to create more advanced use cases around LLMs. Chains may consist of multiple components from several modules:

- **Prompt templates**: Prompt templates are templates for different types of prompts. Like “chatbot” style templates, ELI5 question-answering, etc
- **LLMs**: Large language models like GPT-3, BLOOM, etc
- **Agents**: Agents use LLMs to decide what actions should be taken. Tools like web search or calculators can be used, and all are packaged into a logical loop of operations.
- **Memory**: Short-term memory, long-term memory.

We will dive into each of these in much more detail in upcoming chapters of the LangChain handbook.

For now, we’ll start with the basics behind **prompt templates** and **LLMs**. We’ll also explore two LLM options available from the library, using models from *Hugging Face Hub* or *OpenAI*.

Start using Pinecone for free

Pinecone is the developer-favorite [vector database](https://www.pinecone.io/learn/vector-database/) that's fast and easy to use at any scale.

## Our First Prompt Templates

Prompts being input to LLMs are often structured in different ways so that we can get different results. For Q&A, we could take a user’s question and reformat it for different Q&A styles, like conventional Q&A, a bullet list of answers, or even a summary of problems relevant to the given question.

### Creating Prompts in LangChain

Let’s put together a simple question-answering prompt template. We first need to install the langchain library.

!pip install langchain

*Follow along with the code via* [*the walkthrough](https://github.com/pinecone-io/examples/blob/master/learn/generation/langchain/handbook/00-langchain-intro.ipynb)!*

From here, we import the PromptTemplate class and initialize a template like so:

```
from langchain import PromptTemplate

template = """Question: {question}

Answer: """
prompt = PromptTemplate(
        template=template,
    input_variables=['question']
)

# user question
question = "Which NFL team won the Super Bowl in the 2010 season?"
```

When using these prompt template with the given question we will get:

Question: Which NFL team won the Super Bowl in the 2010 season? Answer:

For now, that’s all we need. We’ll use the same prompt template across both Hugging Face Hub and OpenAI LLM generations.

## Hugging Face Hub LLM

The Hugging Face Hub endpoint in LangChain connects to the Hugging Face Hub and runs the models via their free inference endpoints. We need a [Hugging Face account and API key](https://huggingface.co/settings/tokens) to use these endpoints.

Once you have an API key, we add it to the HUGGINGFACEHUB_API_TOKEN environment variable. We can do this with Python like so:

```
import os

os.environ['HUGGINGFACEHUB_API_TOKEN'] = 'HF_API_KEY'
```

Next, we must install the huggingface_hub library via Pip.

!pip install huggingface_hub

Now we can generate text using a Hub model. We’ll use [google/flan-t5-x1](https://huggingface.co/google/flan-t5-xl).

*The default Hugging Face Hub inference APIs do not use specialized hardware and, therefore, can be slow. They are also not suitable for running larger models like* *bigscience/bloom-560m* *or* *google/flan-t5-xxl* *(note* *xxl* *vs.* *xl).*

For this question, we get the correct answer of "green bay packers".

### Asking Multiple Questions

If we’d like to ask multiple questions, we can try two approaches:

1. Iterate through all questions using the generate method, answering them one at a time.
2. Place all questions into a single prompt for the LLM; this will only work for more advanced LLMs.

Starting with option (1), let’s see how to use the generate method:

Here we get bad results except for the first question. This is simply a limitation of the LLM being used.

If the model cannot answer individual questions accurately, grouping all queries into a single prompt is unlikely to work. However, for the sake of experimentation, let’s try it.

As expected, the results are not helpful. We’ll see later that more powerful LLMs can do this.

## OpenAI LLMs

The OpenAI endpoints in LangChain connect to OpenAI directly or via Azure. We need an [OpenAI account and API key](https://beta.openai.com/account/api-keys) to use these endpoints.

Once you have an API key, we add it to the OPENAI_API_TOKEN environment variable. We can do this with Python like so:

Next, we must install the openai library via Pip.

!pip install openai

Now we can generate text using OpenAI’s GPT-3 generation (or *completion*) models. We’ll use [text-davinci-003](https://huggingface.co/google/flan-t5-xl).

*Alternatively, if you’re using OpenAI via Azure, you can do:*

We’ll use the same simple question-answer prompt template as before with the Hugging Face example. The only change is that we now pass our OpenAI LLM davinci:

As expected, we’re getting the correct answer. We can do the same for multiple questions using generate:

Most of our results are correct or have a degree of truth. The model undoubtedly functions better than the google/flan-t5-xl model. As before, let’s try feeding all questions into the model at once.

As we keep rerunning the query, the model will occasionally make errors, but at other times manage to get all answers correct.

That’s it for our introduction to LangChain — a library that allows us to build more advanced apps around LLMs like OpenAI’s GPT-3 models or the open-source alternatives available via Hugging Face.

As mentioned, LangChain can do much more than we’ve demonstrated here. We’ll be covering these other features in upcoming articles.

## References

[1] [GPT-3 Archived Repo](https://github.com/openai/gpt-3) (2020), OpenAI GitHub

[](https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Fb0bf4949bbd13bd1e62057bfc931fe30aad35d83-1700x2192.png&w=3840&q=100)

The handbook to the LangChain library for building applications around generative AI and large language models (LLMs). (series cover image)