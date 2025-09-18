# Google ADK + Vertex AI Live API. Going Beyond the ADK CLI by Building… | by Sascha Heyer | Google Cloud - Community | May, 2025 | Medium

Column: https://medium.com/google-cloud/google-adk-vertex-ai-live-api-125238982d5e
Processed: Yes
created on: May 16, 2025 6:44 AM

# Google ADK + Vertex AI Live API

## *Going Beyond the ADK CLI by Building Streaming Experiences with the Agent Development Kit and the Vertex AI Live API*

![](https://miro.medium.com/v2/resize:fill:32:32/1*0OH3M299jiP0PVYNOJq12A.png)

[Sascha Heyer](https://medium.com/@saschaheyer?source=post_page---byline--125238982d5e---------------------------------------)

7 min read

·

1 day ago

Alright, let’s talk ADK this time. In my previous [articles](https://github.com/SaschaHeyer/gen-ai-livestream/tree/main/multimodal-live-api#-the-article-series), we’ve talked exclusively about Google’s Multimodal Live API. We explored its power for low-latency, bidirectional interactions, even getting our AIs to chat back and forth with us in real-time.

Now, let’s bring that power into the [**Agent Development Kit (ADK)**](https://google.github.io/adk-docs/). The ADK is a fantastic toolkit for building sophisticated agents. Under the hood, it's also tapping into the same Multimodal Live API for its impressive live streaming features (voice and video). This is great because it means we learned a lot in the previous articles and can now take this and make use of it with the ADK.

![](https://miro.medium.com/v2/resize:fit:700/1*imM5Y4LbZaRyKb2CfkAZEA.png)

However, if you’ve gone beyond the ADK’s convenient CLI or its web interface, you might have noticed something. When you want to truly customize the experience like integrating live audio and video streams directly into your ADK agents the path can feel less documented. As of May 15th, 2025, finding a comprehensive, official example in the ADK samples repo that details a custom server-side setup for full audio/video streaming with deep integration… well, it’s a bit of a treasure hunt. (Perhaps I should contribute that article to the official repository.)

That’s precisely what this article is about. We discuss how you can directly integrate the Live API’s streaming capabilities when using the ADK.

This is for those moments when `adk web` is a great starting point, but you have reached the point where you want to put your agents into production.

# Why Go Direct with ADK and the Live API?

The ADK’s CLI and web UI are excellent for quick prototyping and testing. But what if you’re building:

- A custom web application with a unique user interface for voice and video interactions?
- A backend system that needs to programmatically manage and process live audio/video streams with an agent?

In these scenarios, you must work more closely with the ADK’s components that interface with the Live API. It requires a bit more effort, yes but this is what is required if you truly want to put your Agent in front of users or customers.

# Bridging the Documentation Gap

The code Ill be walking through is designed to create a robust server-side setup. This server handles bidirectional audio and video streams and integrates with an ADK agent.

The Python-based server uses WebSockets to communicate with a client, leveraging the ADK’s `Runner` and `LiveRequestQueue` to manage the conversation flow with the Live API.

If that is new for you, check out my previous articles in this [series](https://github.com/SaschaHeyer/gen-ai-livestream/tree/main/multimodal-live-api#-the-article-series).

Let us s dive into the key parts of the implementation.

# ADK Initialization and Configuration

At the heart of our server (`multimodal_server_adk.py`), we begin by initializing the core ADK components. This involves defining our agent, specifying the model it will use, and giving it instructions.

Here, `Agent`, `LiveRequestQueue`, `Runner`, `RunConfig`, and `StreamingMode` are fundamental ADK constructs.

First, we import the necessary ADK classes:

```
from google.adk.agents import Agent, LiveRequestQueue
from google.adk.runners import Runner
from google.adk.agents.run_config import RunConfig, StreamingMode
from google.genai import types
```

Next, within our `server` we define the agent itself. This is where we specify its behavior and the AI model it uses. So far this is standard ADK code, except for our Server class around it.

```
class MultimodalADKServer(BaseWebSocketServer):
    def __init__(self, host="0.0.0.0", port=8765):
        super().__init__(host, port)
        self.agent = Agent(
            name="customer_service_agent",
            model=MODEL,
            instruction=SYSTEM_INSTRUCTION,
            tools=[],
        )
        self.session_service = InMemorySessionService()
```

The real-time interaction is configured within the `process_audio` method.

Here we create a `LiveRequestQueue` which will be our channel for sending media to the agent.

We then define a `RunConfig` object. This object is critical as it dictates how the streaming session will operate. This is the same config we covered in earlier parts of the series.

```
async def process_audio(self, websocket, client_id):
        live_request_queue = LiveRequestQueue()

        run_config = RunConfig(
            streaming_mode=StreamingMode.BIDI,
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=VOICE_NAME
                    )
                )
            ),
            response_modalities=["AUDIO"],
            output_audio_transcription=types.AudioTranscriptionConfig(),
            input_audio_transcription=types.AudioTranscriptionConfig(),
        )
```

If there is one thing to remember, it is the `LiveRequestQueue` which is key for *sending* our media (audio, image).

# Sending Media with `LiveRequestQueue`

This is where the real-time action of sending your audio and video to the agent happens. The ADK provides the `LiveRequestQueue` object as the dedicated channel for this purpose.

Our server is designed to handle media coming from a client (like a web browser) over WebSockets. In the `process_audio` method of `MultimodalADKServer`, we set up an `asyncio.TaskGroup` to manage several concurrent operations:

```
audio_queue = asyncio.Queue()
video_queue = asyncio.Queue()

async with asyncio.TaskGroup() as tg:
  # Tasks for receiving, processing, and sending media are created here
```

Let’s look at how each piece contributes to sending data.

## **A. Receiving Media from the Client (WebSocket)**

First, we need a way to get the audio and video data from the client application (e.g., the browser). The `handle_websocket_messages` coroutine listens on the WebSocket connection. When the client sends a message containing audio or video, this task decodes it (it's sent as Base64 in our example) and puts the raw bytes onto local `asyncio.Queue`s (`audio_queue` or `video_queue`).

```
async def handle_websocket_messages():
    async for message in websocket:
        data = json.loads(message)
        if data.get("type") == "audio":
            audio_bytes = base64.b64decode(data.get("data", ""))
            await audio_queue.put(audio_bytes)
        elif data.get("type") == "video":
            video_bytes = base64.b64decode(data.get("data", ""))
            video_mode = data.get("mode", "webcam")
            await video_queue.put({"data": video_bytes, "mode": video_mode})

tg.create_task(handle_websocket_messages(), name="MessageHandler")
```

This task acts as the bridge between the external client and our server’s internal processing queues.

## **B. Sending Audio to the Agent via `LiveRequestQueue`**

Once audio data is in our local `audio_queue`, the `process_and_send_audio` task picks it up.

This is where `LiveRequestQueue` comes into play.

We use its `send_realtime()` method to dispatch the audio bytes to the Live API.

```
async def process_and_send_audio():
    while True:
        data = await audio_queue.get()
        live_request_queue.send_realtime(
            types.Blob(
                data=data,
                mime_type=f"audio/pcm;rate={SEND_SAMPLE_RATE}",
            )
        )
        audio_queue.task_done()

tg.create_task(process_and_send_audio(), name="AudioProcessor")
```

The `types.Blob` object wraps our audio data. The `live_request_queue.send_realtime()` method is specifically designed for streaming these media blobs with low latency.

## **C. Sending Video to the Agent via `LiveRequestQueue`**

Similarly, the `process_and_send_video` task handles video frames from the local `video_queue`.

It also uses `live_request_queue.send_realtime()` to send each video frame as a `types.Blob`.

```
async def process_and_send_video():
    while True:
        video_data_item = await video_queue.get()
        video_bytes = video_data_item.get("data")
        live_request_queue.send_realtime(
            types.Blob(
                data=video_bytes,
                mime_type="image/jpeg",
            )
        )
        video_queue.task_done()

tg.create_task(process_and_send_video(), name="VideoProcessor")
```

Here, the `mime_type` would be appropriate for the video frames, such as `image/jpeg` if you're sending JPEG-encoded frames. We are not sending an actually video but processing the video in single image frames.

This clear separation receiving from the client into local queues, then dedicated tasks using `LiveRequestQueue.send_realtime()` to forward to the agent is key to managing the flow of live media effectively.

# Receiving Responses from the Agent

While sending data is crucial, a live interaction is a two-way street.

The `receive_and_process_responses` task is responsible for handling what the ADK with its underlying Live API sends back.

This task listens for various events stream from `runner.run_live()` like the agents spoken audio, transcription or tool, interruptions, turn complections, calls among many other event data points.

It iterates over those events yielded by `runner.run_live()`.

```
async def receive_and_process_responses():
    async for event in runner.run_live(
        session=session,
        live_request_queue=live_request_queue,
        run_config=run_config,
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                if hasattr(part, "inline_data") and part.inline_data:
                    b64_audio = base64.b64encode(part.inline_data.data).decode("utf-8")
                    await websocket.send(json.dumps({"type": "audio", "data": b64_audio}))

                if hasattr(part, "text") and part.text:
                    if "partial=True" in str(event):
                        await websocket.send(json.dumps({"type": "text", "data": part.text}))

tg.create_task(receive_and_process_responses(), name="ResponseHandler")
```

# The Client Side

While our main focus in this article is the server-side ADK integration for streaming, it’s important to remember that a complete solution requires a client.

The provided codebase includes `multimodal.html`, `audio-client.js`, and `multimodal-client.js` which sets up a web interface.

This client handles capturing microphone audio and camera/screen video, and then sends this media over WebSockets to our Python server.

It also plays back the audio responses received from the server. The specifics of implementing such a client capturing media streams, handling user permissions, and WebSocket communication were covered in more detail in our previous articles, where we interfaced directly with the Multimodal Live API.

The principles remain the same here, with the client sending data to and receiving data from our custom ADK-based server.

# Get The Full Code 💻

You can find the complete, evolving project that continues our series, as well as a simpler starter version, in the following GitHub repositories:

**Full Project (Continuing Series)**This repository contains the complete implementation with all features discussed + what we discussed in previous articles, and will be updated as the series progresses.

## [gen-ai-livestream/multimodal-live-api/ui at main · SaschaHeyer/gen-ai-livestream](https://github.com/SaschaHeyer/gen-ai-livestream/tree/main/multimodal-live-api/ui?source=post_page-----125238982d5e---------------------------------------)

### [Contribute to SaschaHeyer/gen-ai-livestream development by creating an account on GitHub.](https://github.com/SaschaHeyer/gen-ai-livestream/tree/main/multimodal-live-api/ui?source=post_page-----125238982d5e---------------------------------------)

[github.com](https://github.com/SaschaHeyer/gen-ai-livestream/tree/main/multimodal-live-api/ui?source=post_page-----125238982d5e---------------------------------------)

If you are looking for this ⬇️ the full project is the correct code for you.

![](https://miro.medium.com/v2/resize:fit:700/1*IGb6OZiOC8Hl2K6YIcLR2A.png)

**Starter Code** If you're looking for a more bare-bones version to get started quickly, this repository provides a simplified setup.

## [gen-ai-livestream/agents/agent-development-kit/live-api at main · SaschaHeyer/gen-ai-livestream](https://github.com/SaschaHeyer/gen-ai-livestream/tree/main/agents/agent-development-kit/live-api?source=post_page-----125238982d5e---------------------------------------)

### [Contribute to SaschaHeyer/gen-ai-livestream development by creating an account on GitHub.](https://github.com/SaschaHeyer/gen-ai-livestream/tree/main/agents/agent-development-kit/live-api?source=post_page-----125238982d5e---------------------------------------)

[github.com](https://github.com/SaschaHeyer/gen-ai-livestream/tree/main/agents/agent-development-kit/live-api?source=post_page-----125238982d5e---------------------------------------)

If you are looking for this ⬇️ the starter code is the correct code for you.

Perhaps this example, or one like it, will find its way into the official ADK.

# *Got thoughts on this approach?*

Have you built something similar? Found a neat trick for working with the ADK and Live API for audio/video streaming? I’d love to hear about it in the comments.

And hey, if you found this useful, you know the drill claps, shares, and all that good stuff are appreciated.

Connect with me on [LinkedIn](https://medium.com/google-cloud/YOUR_LINKEDIN_PROFILE_URL) and subscribe to my [YouTube Channel](https://medium.com/google-cloud/YOUR_YOUTUBE_CHANNEL_URL) for more deep dives into AI and development.

![](https://miro.medium.com/v2/resize:fit:700/1*ND1ZCH6aTYgy59qWLgMgMw.png)