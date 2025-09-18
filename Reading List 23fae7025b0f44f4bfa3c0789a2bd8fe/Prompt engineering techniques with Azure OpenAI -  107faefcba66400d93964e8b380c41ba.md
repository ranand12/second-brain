# Prompt engineering techniques with Azure OpenAI - Azure OpenAI Service | Microsoft Learn

Column: https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/advanced-prompt-engineering?pivots=programming-language-chat-completions
Processed: No
created on: April 25, 2023 5:45 PM

![logo-ms-social.png](Prompt%20engineering%20techniques%20with%20Azure%20OpenAI%20-%20%20107faefcba66400d93964e8b380c41ba/logo-ms-social.png)

This guide will walk you through some advanced techniques in prompt design and prompt engineering. If you're new to prompt engineering, we recommend starting with our [introduction to prompt engineering guide](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/prompt-engineering).

While the principles of prompt engineering can be generalized across many different model types, certain models expect a specialized prompt structure. For Azure OpenAI GPT models, there are currently two distinct APIs where prompt engineering comes into play:

- Chat Completion API.
- Completion API.

Each API requires input data to be formatted differently, which in turn impacts overall prompt design. The **Chat Completion API** supports the ChatGPT (preview) and GPT-4 (preview) models. These models are designed to take input formatted in a [specific chat-like transcript](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/chatgpt) stored inside an array of dictionaries.

The **Completion API** supports the older GPT-3 models and has much more flexible input requirements in that it takes a string of text with no specific format rules. Technically the ChatGPT (preview) models can be used with either APIs, but we strongly recommend using the Chat Completion API for these models. To learn more, please consult our [in-depth guide on using these APIs](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/chatgpt).

The techniques in this guide will teach you strategies for increasing the accuracy and grounding of responses you generate with a Large Language Model (LLM). It is, however, important to remember that even when using prompt engineering effectively you still need to validate the responses the models generate. Just because a carefully crafted prompt worked well for a particular scenario doesn't necessarily mean it will generalize more broadly to certain use cases. Understanding the [limitations of LLMs](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/transparency-note?context=%2Fazure%2Fcognitive-services%2Fopenai%2Fcontext%2Fcontext#limitations), is just as important as understanding how to leverage their strengths.