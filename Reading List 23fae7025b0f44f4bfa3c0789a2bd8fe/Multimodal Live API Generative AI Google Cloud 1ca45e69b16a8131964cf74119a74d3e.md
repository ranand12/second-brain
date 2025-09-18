# Multimodal Live API  |  Generative AI  |  Google Cloud

Column: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/multimodal-live#capabilities
Processed: Yes
created on: April 3, 2025 7:31 PM

To try a tutorial that lets you use your voice and camera to talk to Gemini through the Multimodal Live API, see the .

The Multimodal Live API enables low-latency, two-way interactions that use text, audio, and video input, with audio and text output. This facilitates natural, human-like voice conversations with the ability to interrupt the model at any time. The model's video understanding capability expands communication modalities, enabling you to share camera input or screencasts and ask questions about them.

## Capabilities

Multimodal Live API includes the following key capabilities:

- **Multimodality**: The model can see, hear, and speak.
- **Low-latency realtime interaction**: The model can provide fast responses.
- **Session memory**: The model retains memory of all interactions within a single session, recalling previously heard or seen information.
- **Support for function calling, code execution, and Search as a Tool**: You can integrate the model with external services and data sources.

Multimodal Live API is designed for server-to-server communication.

For web and mobile apps, we recommend using the integration from our partners at [Daily](https://www.daily.co/products/gemini/multimodal-live-api/).

## Get started

To try the Multimodal Live API, go to the [Vertex AI Studio](https://console.cloud.google.com/vertex-ai/studio/chat?model=gemini-2.0-flash-exp), and then click **Try Multimodal Live**.

Multimodal Live API is a stateful API that uses [WebSockets](https://en.wikipedia.org/wiki/WebSocket).

This section shows an example of how to use Multimodal Live API for text-to-text generation, using Python 3.9+.

## Integration guide

This section describes how integration works with Multimodal Live API.

### Sessions

A WebSocket connection establishes a session between the client and the Gemini server.

After a client initiates a new connection the session can exchange messages with the server to:

- Send text, audio, or video to the Gemini server.
- Receive audio, text, or function call requests from the Gemini server.

The session configuration is sent in the first message after connection. A session configuration includes the model, generation parameters, system instructions, and tools.

See the following example configuration:

```

{
  "model": string,
  "generationConfig": {
    "candidateCount": integer,
    "maxOutputTokens": integer,
    "temperature": number,
    "topP": number,
    "topK": integer,
    "presencePenalty": number,
    "frequencyPenalty": number,
    "responseModalities": [string],
    "speechConfig": object
  },

  "systemInstruction": string,
  "tools": [object]
}

```

For more information, see [BidiGenerateContentSetup](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/multimodal-live#bidigeneratecontentsetup).

### Send messages

Messages are JSON-formatted objects exchanged over the WebSocket connection.

To send a message the client must send a JSON object over an open WebSocket connection. The JSON object must have *exactly one* of the fields from the following object set:

```

{
  "setup": BidiGenerateContentSetup,
  "clientContent": BidiGenerateContentClientContent,
  "realtimeInput": BidiGenerateContentRealtimeInput,
  "toolResponse": BidiGenerateContentToolResponse
}

```

### Supported client messages

See the supported client messages in the following table:

| Message | Description |
| --- | --- |
| `BidiGenerateContentSetup` | Session configuration to be sent in the first message |
| `BidiGenerateContentClientContent` | Incremental content update of the current conversation delivered from the client |
| `BidiGenerateContentRealtimeInput` | Real time audio or video input |
| `BidiGenerateContentToolResponse` | Response to a `ToolCallMessage` received from the server |

### Receive messages

To receive messages from Gemini, listen for the WebSocket 'message' event, and then parse the result according to the definition of the supported server messages.

See the following:

```
ws.addEventListener("message", async (evt) => {
  if (evt.data instanceof Blob) {
    // Process the received data (audio, video, etc.)
  } else {
    // Process JSON response
  }
});
```

Server messages will have *exactly one* of the fields from the following object set:

```

{
  "setupComplete": BidiGenerateContentSetupComplete,
  "serverContent": BidiGenerateContentServerContent,
  "toolCall": BidiGenerateContentToolCall,
  "toolCallCancellation": BidiGenerateContentToolCallCancellation
}

```

### Supported server messages

See the supported server messages in the following table:

| Message | Description |
| --- | --- |
| `BidiGenerateContentSetupComplete` | A `BidiGenerateContentSetup` message from the client, sent when setup is complete |
| `BidiGenerateContentServerContent` | Content generated by the model in response to a client message |
| `BidiGenerateContentToolCall` | Request for the client to run the function calls and return the responses with the matching IDs |
| `BidiGenerateContentToolCallCancellation` | Sent when a function call is canceled due to the user interrupting model output |

### Incremental content updates

Use incremental updates to send text input, establish session context, or restore session context. For short contexts you can send turn-by-turn interactions to represent the exact sequence of events. For longer contexts it's recommended to provide a single message summary to free up the context window for the follow up interactions.

See the following example context message:

```
{
  "clientContent": {
    "turns": [
      {
          "parts":[
          {
            "text": ""
          }
        ],
        "role":"user"
      },
      {
          "parts":[
          {
            "text": ""
          }
        ],
        "role":"model"
      }
    ],
    "turnComplete": true
  }
}
```

Note that while content parts can be of a `functionResponse` type, `BidiGenerateContentClientContent` shouldn't be used to provide a response to the function calls issued by the model. `BidiGenerateContentToolResponse` should be used instead. `BidiGenerateContentClientContent` should only be used to establish previous context or provide text input to the conversation.

### Streaming audio and video

To see an example of how to use the Multimodal Live API in a streaming audio and video format, run the "Getting started with the Multimodal Live API" Jupyter notebook in one of the following environments: 
[Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/multimodal-live-api/intro_multimodal_live_api_genai_sdk.ipynb) | [Open in Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fmultimodal-live-api%2Fintro_multimodal_live_api_genai_sdk.ipynb) | [Open in Vertex AI Workbench user-managed notebooks](https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fmultimodal-live-api%2Fintro_multimodal_live_api_genai_sdk.ipynb) | [View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/multimodal-live-api/intro_multimodal_live_api_genai_sdk.ipynb)

### Code execution

To see an example of code execution, run the "Intro to Generating and Executing Python Code with Gemini 2.0" Jupyter notebook in one of the following environments: 
[Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/code-execution/intro_code_execution.ipynb) | [Open in Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fcode-execution%2Fintro_code_execution.ipynb) | [Open in Vertex AI Workbench user-managed notebooks](https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fcode-execution%2Fintro_code_execution.ipynb) | [View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/code-execution/intro_code_execution.ipynb)

To learn more about code execution, see [Code execution](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/code-execution).

### Function calling

To see an example of function calling, run the "Intro to Function Calling with the Gemini API" Jupyter notebook in one of the following environments: 
[Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/intro_function_calling.ipynb) | [Open in Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Ffunction-calling%2Fintro_function_calling.ipynb) | [Open in Vertex AI Workbench user-managed notebooks](https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Ffunction-calling%2Fintro_function_calling.ipynb) | [View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/intro_function_calling.ipynb)

All functions must be declared at the start of the session by sending tool definitions as part of the `BidiGenerateContentSetup` message.

You define functions by using JSON, specifically with a [select subset](https://ai.google.dev/api/caching#schema) of the [OpenAPI schema format](https://spec.openapis.org/oas/v3.0.3#schemawr). A single function declaration can include the following parameters:

- **name** (string): The unique identifier for the function within the API call.
- **description** (string): A comprehensive explanation of the function's purpose and capabilities.
- **parameters** (object): Defines the input data required by the function.
    - **type** (string): Specifies the overall data type, such as object.
    - **properties** (object): Lists individual parameters, each with:
        - **type** (string): The data type of the parameter, such as string, integer, boolean.
        - **description** (string): A clear explanation of the parameter's purpose and expected format.
    - **required** (array): An array of strings listing the parameter names that are mandatory for the function to operate.

For code examples of a function declaration using curl commands, see [Intro to function calling with the Gemini API](https://ai.google.dev/gemini-api/docs/function-calling#function-calling-curl-samples). For examples of how to create function declarations using the Gemini API SDKs, see the [Function calling tutorial](https://ai.google.dev/gemini-api/docs/function-calling/tutorial).

From a single prompt, the model can generate multiple function calls and the code necessary to chain their outputs. This code executes in a sandbox environment, generating subsequent `BidiGenerateContentToolCall` messages. The execution pauses until the results of each function call are available, which ensures sequential processing.

The client should respond with `BidiGenerateContentToolResponse`.

To learn more, see [Introduction to function calling](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling).

### Audio formats

Multimodal Live API supports the following audio formats:

- Input audio format: Raw 16 bit PCM audio at 16kHz little-endian
- Output audio format: Raw 16 bit PCM audio at 24kHz little-endian

### System instructions

You can provide system instructions to better control the model's output and specify the tone and sentiment of audio responses.

System instructions are added to the prompt before the interaction begins and remain in effect for the entire session.

System instructions can only be set at the beginning of a session, immediately following the initial connection. To provide further input to the model during the session, use incremental content updates.

### Interruptions

Users can interrupt the model's output at any time. When Voice activity detection (VAD) detects an interruption, the ongoing generation is canceled and discarded. Only the information already sent to the client is retained in the session history. The server then sends a `BidiGenerateContentServerContent` message to report the interruption.

In addition, the Gemini server discards any pending function calls and sends a `BidiGenerateContentServerContent` message with the IDs of the canceled calls.

### Voices

Multimodal Live API supports the following voices:

- Puck
- Charon
- Kore
- Fenrir
- Aoede

To specify a voice, set the `voiceName` within the `speechConfig` object, as part of your [session configuration](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/multimodal-live#sessions).

See the following JSON representation of a `speechConfig` object:

```
{
  "voiceConfig": {
    "prebuiltVoiceConfig": {
      "voiceName": "VOICE_NAME"
    }
  }
}
```

## Limitations

Consider the following limitations of Multimodal Live API and Gemini 2.0 when you plan your project.

### Client authentication

Multimodal Live API only provides server to server authentication and isn't recommended for direct client use. Client input should be routed through an intermediate application server for secure authentication with the Multimodal Live API.

### Conversation history

While the model keeps track of in-session interactions, conversation history isn't stored. When a session ends, the corresponding context is erased.

In order to restore a previous session or provide the model with historic context of user interactions, the application should maintain its own conversation log and use a `BidiGenerateContentClientContent` message to send this information at the start of a new session.

### Maximum session duration

Session duration is limited to up to 15 minutes for audio or up to 2 minutes of audio and video. When the session duration exceeds the limit, the connection is terminated.

The model is also limited by the context size. Sending large chunks of content alongside the video and audio streams may result in earlier session termination.

### Voice activity detection (VAD)

The model automatically performs voice activity detection (VAD) on a continuous audio input stream. VAD is always enabled, and its parameters aren't configurable.

### Additional limitations

Manual endpointing isn't supported.

Audio inputs and audio outputs negatively impact the model's ability to use function calling.

### Token count

Token count isn't supported.

### Rate limits

The following rate limits apply:

- 3 concurrent sessions per API key
- 4M tokens per minute

## Messages and events

### BidiGenerateContentClientContent

Incremental update of the current conversation delivered from the client. All the content here is unconditionally appended to the conversation history and used as part of the prompt to the model to generate content.

A message here will interrupt any current model generation.

| Fields |  |
| --- | --- |
| `turns[]` | [`Content`](https://cloud.google.com/vertex-ai/generative-ai/docs/reference/rpc/google.cloud.aiplatform.v1beta1#google.cloud.aiplatform.v1beta1.Content) 
Optional. The content appended to the current conversation with the model.
For single-turn queries, this is a single instance. For multi-turn queries, this is a repeated field that contains conversation history and latest request. |
| `turn_complete` | `bool` 
Optional. If true, indicates that the server content generation should start with the currently accumulated prompt. Otherwise, the server will await additional messages before starting generation. |

### BidiGenerateContentRealtimeInput

User input that is sent in real time.

This is different from `ClientContentUpdate` in a few ways:

- Can be sent continuously without interruption to model generation.
- If there is a need to mix data interleaved across the `ClientContentUpdate` and the `RealtimeUpdate`, server attempts to optimize for best response, but there are no guarantees.
- End of turn is not explicitly specified, but is rather derived from user activity (for example, end of speech).
- Even before the end of turn, the data is processed incrementally to optimize for a fast start of the response from the model.
- Is always assumed to be the user's input (cannot be used to populate conversation history).

| Fields |  |
| --- | --- |
| `media_chunks[]` | [`Blob`](https://cloud.google.com/vertex-ai/generative-ai/docs/reference/rpc/google.cloud.aiplatform.v1beta1#google.cloud.aiplatform.v1beta1.Blob) 
Optional. Inlined bytes data for media input. |

### BidiGenerateContentServerContent

Incremental server update generated by the model in response to client messages.

Content is generated as quickly as possible, and not in realtime. Clients may choose to buffer and play it out in realtime.

| Fields |  |
| --- | --- |
| `turn_complete` | `bool` 
Output only. If true, indicates that the model is done generating. Generation will only start in response to additional client messages. Can be set alongside `content`, indicating that the `content` is the last in the turn. |
| `interrupted` | `bool` 
Output only. If true, indicates that a client message has interrupted current model generation. If the client is playing out the content in realtime, this is a good signal to stop and empty the current queue. |
| `grounding_metadata` | [`GroundingMetadata`](https://cloud.google.com/vertex-ai/generative-ai/docs/reference/rpc/google.cloud.aiplatform.v1beta1#google.cloud.aiplatform.v1beta1.GroundingMetadata) 
Output only. Metadata specifies sources used to ground generated content. |
| `model_turn` | [`Content`](https://cloud.google.com/vertex-ai/generative-ai/docs/reference/rpc/google.cloud.aiplatform.v1beta1#google.cloud.aiplatform.v1beta1.Content) 
Output only. The content that the model has generated as part of the current conversation with the user. |

### BidiGenerateContentSetup

Message to be sent in the first and only first client message. Contains configuration that will apply for the duration of the streaming session.

Clients should wait for a `BidiGenerateContentSetupComplete` message before sending any additional messages.

| Fields |  |
| --- | --- |
| `model` | `string` 
Required. The fully qualified name of the publisher model or tuned model endpoint to use.
Publisher model format: `projects/{project}/locations/{location}/publishers/\*/models/\*` |
| `generation_config` | [`GenerationConfig`](https://cloud.google.com/vertex-ai/generative-ai/docs/reference/rpc/google.cloud.aiplatform.v1beta1#google.cloud.aiplatform.v1beta1.GenerationConfig) 
Optional. Generation config.
The following fields aren't supported:  
• `responseLogprobs` 
• `responseMimeType` 
• `logprobs` 
• `responseSchema` 
• `stopSequence` 
• `routingConfig` 
• `audioTimestamp`  |
| `system_instruction` | [`Content`](https://cloud.google.com/vertex-ai/generative-ai/docs/reference/rpc/google.cloud.aiplatform.v1beta1#google.cloud.aiplatform.v1beta1.Content) 
Optional. The user provided system instructions for the model. Note: only text should be used in parts. Content in each part will be in a separate paragraph. |
| `tools[]` | [`Tool`](https://cloud.google.com/vertex-ai/generative-ai/docs/reference/rpc/google.cloud.aiplatform.v1beta1#google.cloud.aiplatform.v1beta1.Tool) 
Optional. A list of `Tools` the model may use to generate the next response.
A `Tool` is a piece of code that enables the system to interact with external systems to perform an action, or set of actions, outside of knowledge and scope of the model. |

### BidiGenerateContentSetupComplete

This type has no fields.

Sent in response to a `BidiGenerateContentSetup` message from the client.

### BidiGenerateContentToolCall

Request for the client to execute the `functionCalls` and return the responses with the matching `id`s.

| Fields |  |
| --- | --- |
| `function_calls[]` | [`FunctionCall`](https://cloud.google.com/vertex-ai/generative-ai/docs/reference/rpc/google.cloud.aiplatform.v1beta1#google.cloud.aiplatform.v1beta1.FunctionCall) 
Output only. The function call to be executed. |

### BidiGenerateContentToolCallCancellation

Notification for the client that a previously issued `ToolCallMessage` with the specified `id`s should have been not executed and should be cancelled. If there were side-effects to those tool calls, clients may attempt to undo the tool calls. This message occurs only in cases where the clients interrupt server turns.

| Fields |  |
| --- | --- |
| `ids[]` | `string` 
Output only. The ids of the tool calls to be cancelled. |

### BidiGenerateContentToolResponse

Client generated response to a `ToolCall` received from the server. Individual `FunctionResponse` objects are matched to the respective `FunctionCall` objects by the `id` field.

Note that in the unary and server-streaming GenerateContent APIs function calling happens by exchanging the `Content` parts, while in the bidi GenerateContent APIs function calling happens over these dedicated set of messages.

| Fields |  |
| --- | --- |
| `function_responses[]` | [`FunctionResponse`](https://cloud.google.com/vertex-ai/generative-ai/docs/reference/rpc/google.cloud.aiplatform.v1beta1#google.cloud.aiplatform.v1beta1.FunctionResponse) 
Optional. The response to the function calls. |

## What's next

- Learn more about [function calling](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling).
- See the [Function calling reference](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/function-calling) for examples.