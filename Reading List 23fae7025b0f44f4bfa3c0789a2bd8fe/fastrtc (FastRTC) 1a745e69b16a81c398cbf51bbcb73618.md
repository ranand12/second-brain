# fastrtc (FastRTC)

Column: https://huggingface.co/fastrtc
Processed: Yes
created on: February 27, 2025 5:22 AM

![](https://huggingface.co/datasets/freddyaboulton/bucket/resolve/main/fastrtc_logo.png)

FastRTC Logo

### The Real-Time Communication Library for Python.

Turn any python function into a real-time audio and video stream over WebRTC or WebSockets.

## Installation

```
pip install fastrtc

```

to use built-in pause detection (see [ReplyOnPause](https://fastrtc.org/)), and text to speech (see [Text To Speech](https://fastrtc.org/userguide/audio/#text-to-speech)), install the `vad` and `tts` extras:

```
pip install fastrtc[vad, tts]

```

## Key Features

- 🗣️ Automatic Voice Detection and Turn Taking built-in, only worry about the logic for responding to the user.
- 💻 Automatic UI - Use the `.ui.launch()` method to launch the webRTC-enabled built-in Gradio UI.
- 🔌 Automatic WebRTC Support - Use the `.mount(app)` method to mount the stream on a FastAPI app and get a webRTC endpoint for your own frontend!
- ⚡️ Websocket Support - Use the `.mount(app)` method to mount the stream on a FastAPI app and get a websocket endpoint for your own frontend!
- 📞 Automatic Telephone Support - Use the `fastphone()` method of the stream to launch the application and get a free temporary phone number!
- 🤖 Completely customizable backend - A `Stream` can easily be mounted on a FastAPI app so you can easily extend it to fit your production application. See the [Talk To Claude](https://huggingface.co/spaces/fastrtc/talk-to-claude) demo for an example on how to serve a custom JS frontend.

## Docs

[https://fastrtc.org](https://fastrtc.org/)