# Building a Real-Time Video Chat with Gemini 2.0, Gradio, and WebRTC 👀👂

Column: https://huggingface.co/blog/freddyaboulton/realtime-video-chat-with-gradio-webrtc
Processed: Yes
created on: February 27, 2025 5:44 AM

In December 2024 Google [released](https://medium.com/r/?url=https%3A%2F%2Fblog.google%2Fproducts%2Fgemini%2Fgoogle-gemini-ai-collection-2024%2F) Gemini 2.0 - a complete overhaul of their flagship AI model. One of the coolest new features is the ability to have natural, human-like video chat conversations with Gemini via the [multimodal live API](https://ai.google.dev/api/multimodal-live). In this tutorial, we'll build a web application that lets you have real-time video chats with Gemini using Python.

Our application will enable:

- Real-time video chat with Gemini using your webcam
- Real-time Audio streaming for natural conversations
- Optional image upload capabilities
- A clean, user-friendly interface

 Your browser does not support the video tag.

## Prerequisites

- Basic Python knowledge
- A Google Cloud account with a Gemini API key. Go [here](https://support.google.com/googleapi/answer/6158862?hl=en)
- The following python packages:

Our application will be built with [Gradio](https://www.gradio.app/), a framework for building AI-powered web applications entirely in Python. Gradio will handle all the UI elements for us so we can just focus on the core logic of the application. The `gradio-webrtc` package is an extension of Gradio that enables low-latency audio/video streams via WebRTC, a real-time communication protocol.

The `google-generativeai` package is Google's official package for interacting with Gemini.

## Implementing the Audio Video Handler

The core of our application is the `GeminiHandler` class which will set up the audio/video stream to the Gemini server. Let's break down the implementation into parts.

### Class Constructor and Copy Method

The class constructor will create all the variables we need to handle the video session. Namely, queues for storing the audio and video output as well as a session variable for storing the connection to the gemini server.

The copy method ensures that each user has their own unique stream handler.

### Audio Processing

The audio processing is handled by the `emit` and `receive` methods. The `receive` method is called whenever a new audio frame is received from the user and `emit` returns Gemini's next audio frame.

In the `emit` method we'll connect to the Gemini API by calling the `connect` method in the background (that's what `asyncio.create_task` means). The Gemini python library uses a context manager to open and close a connection. We use an [`asyncio.Event`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event) to keep this context manager open until the user clicks the stop button or closes the page. At that point, the shutdown method is called and the `asyncio.Event` is set.

### Video Processing

The video processing will be handled by the `video_receive` and `video_emit` methods. For our application, we will simply show the webcam stream back to the user but every 1 second we will send the latest webcam frame, as well the optional uploaded image, to the Gemini server.

![](https://cdn-uploads.huggingface.co/production/uploads/626a9bfa03e2e2796f24ca11/ZsZcajGb4LXLAGicq2Y07.png)

## The UI

Finally, let's create the Gradio interface with proper styling and components.

Below the HTML header we place two rows - one for inputting the gemini API key and the other for starting the video chat. When the page is first opened, only the first row will be visible. Once an API key is inputted, the second row will be visible and the first row will not be.

The `webrtc.stream` method sets up our video chat. As inputs to this event, we'll pass in the api key and the optional `image_input` component. We set `time_limit=90` so that a video chat is limited to 90 seconds. The free tier of the Gemini API only allows two concurrent connections so we set a `concurrency_limit=2` to ensure only two users are connected at a time.

# Conclusion

This implementation creates a full-featured voice chat interface for Gemini AI, supporting both audio and image inputs. The use of WebRTC enables real-time, low-latency communication, while the async design ensures efficient handling of streams.

Our application is hosted on Hugging Face [here](https://huggingface.co/spaces/freddyaboulton/gemini-audio-video-chat). To learn more about WebRTC streaming with python, visit the gradio-webrtc [docs](https://freddyaboulton.github.io/gradio-webrtc/). Gradio is a great tool for building custom UIs in python, it works for any kind of AI application. Check out the docs [here](https://www.gradio.app/).