# Building a AI Podcast Generator Inspired by Google’s NotebookLM and Illuminate | by Sascha Heyer | Google Cloud - Community | Medium

Column: https://medium.com/google-cloud/building-a-dynamic-podcast-generator-inspired-by-googles-notebooklm-and-illuminate-e585cfcd0af1
Processed: Yes
created on: March 2, 2025 9:45 AM

# Building a AI Podcast Generator Inspired by Google’s NotebookLM and Illuminate

![](https://miro.medium.com/v2/resize:fill:44:44/1*0OH3M299jiP0PVYNOJq12A.png)

![](https://miro.medium.com/v2/resize:fill:24:24/1*FUjLiCANvATKeaJEeg20Rw.png)

[Sascha Heyer](https://medium.com/@saschaheyer?source=post_page---byline--e585cfcd0af1---------------------------------------)

·

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F57d0091b2e22&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fgoogle-cloud%2Fbuilding-a-dynamic-podcast-generator-inspired-by-googles-notebooklm-and-illuminate-e585cfcd0af1&user=Sascha+Heyer&userId=57d0091b2e22&source=post_page-57d0091b2e22--byline--e585cfcd0af1---------------------post_header------------------)

Published in

[Google Cloud - Community](https://medium.com/google-cloud?source=post_page---byline--e585cfcd0af1---------------------------------------)

·

5 min read

·

Sep 16, 2024

- -

Google introduced two innovative products, **NotebookLM** and **Illuminate.** That has garnered significant attention on platforms like LinkedIn.

Both offerings showcase the power of AI in transforming content consumption by creating dynamic podcasts featuring two people discussing a topic.

Inspired by this concept, I implemented my version to fully control the voices and the prompts used.

In this article, I’ll walk you through my journey of building this dynamic podcast generator, explaining the code and technologies involved.

# Experience the AI-Generated Podcasts

Before we delve into the technical journey of building this dynamic podcast generator, I invite you to listen to four podcasts I’ve created using this code. Each podcast transforms one of my articles into an engaging conversation between the two podcast hosts, **Sascha** and **Marina**.

# Understanding NotebookLM and Illuminate

Illuminate and NotebookLM greatly influenced and inspired this article.

## What is Illuminate?

**Illuminate** is an experimental technology developed by Google that leverages AI to adapt content to individual learning preferences. It generates audio featuring two AI-generated voices in conversation, discussing key points of selected academic papers, primarily optimized for published computer science research.

> “As an experimental product, the generated audio with two AI-generated voices in conversation may not always perfectly capture the nuances of the original research papers. Please be aware that there may be occasional errors or inconsistencies and that we are continually iterating to improve the user experience.”
> 

## What is NotebookLM

NotebookLM is a personalized AI research assistant that helps users delve deeper into topics by generating summaries, answering questions, and facilitating a better understanding of complex materials.

# Creating a Custom Dynamic Podcast

To replicate and customize this experience, I utilized the following services:

- **Google Text-to-Speech (TTS)** with two new experimental voices.
- **ElevenLabs** for training a cloned voice.
- **Google Cloud Storage** to store the generated podcast.
- **Gemini**, to transform articles into engaging conversations between two people.

podcast generator flow

![](https://miro.medium.com/v2/resize:fit:700/1*g84QELhnckcnGC-2Jo-qDw.png)

## The Goal

- Create a dynamic podcast featuring two speakers, **Sascha** and **Marina**, discussing a given article.
- Have full control over the voices and prompts.
- Generate natural-sounding conversations with emotional depth and realism.

# Diving into the Code

## Defining the System Prompt to generate the Conversation

This prompt guides the AI model in generating a natural, engaging conversation and is suitable for conversion into speech. Play with it, and let me know if you find some nice tricks to optimize the conversation further.

```
system_prompt = """you are an experienced podcast host...

- Based on text like an article, you can create an engaging conversation between two people.
- Make the conversation at least 30,000 characters long with a lot of emotion.
- In the response, for me to identify, use Sascha and Marina.
- Sascha is writing the articles, and Marina is the second speaker who asks all the good questions.
- The podcast is called The Machine Learning Engineer.
- Use short sentences that can be easily used with speech synthesis.
- Include excitement during the conversation.
- Do not mention last names.
- Sascha and Marina are doing this podcast together. Avoid sentences like: "Thanks for having me, Marina!"
- Include filler words like "uh" or repeat words to make the conversation more natural.
"""
```

With this prompt and Gemini, we can create the conversation as a list of alternating discussions. Using Gemini 1.5 Flash produced really good results, and we can make advantage of the low usage costs.

```
generation_config = GenerationConfig(
    max_output_tokens=8192,
    temperature=1,
    top_p=0.95,
    response_mime_type="application/json",
    response_schema={
        "type": "ARRAY",
        "items": {
            "type": "OBJECT",
            "properties": {
                "speaker": {"type": "STRING"},
                "text": {"type": "STRING"}
            }
        }
    },
)

def generate_conversation():
    vertexai.init(project="YOUR_PROJECT_ID", location="us-central1")
    model = GenerativeModel(
        "gemini-1.5-flash-001",
        system_instruction=[system_prompt]
    )
    responses = model.generate_content(
        [article],
        generation_config=generation_config,
        stream=False,
    )

    json_response = responses.candidates[0].content.parts[0].text
    json_data = json.loads(json_response)
    formatted_json = json.dumps(json_data, indent=4)
    print(formatted_json)
    return json_data
```

## Mapping Speakers to Specific Voices

As mentioned, I am using ElevenLabs with my cloned voice. If you don’t want to clone your voice, you can simply use a Google Speech-to-Text voice by adapting the mapping.

```
speaker_voice_map = {
    "Sascha": "ElevenLabs",            # Sascha's voice via ElevenLabs API
    "Marina": "en-US-Journey-O"        # Marina's voice via Google TTS
}
```

# Google Text-to-Speech

This function synthesizes speech using Google TTS for the specified speaker and saves the audio file.

```
def synthesize_speech_google(text, speaker, index):
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name=speaker_voice_map[speaker]
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    filename = f"audio-files/{index}_{speaker}.mp3"
    with open(filename, "wb") as out:
        out.write(response.audio_content)
    print(f'Audio content written to file "{filename}"')
```

## ElevenLabs Text-to-Speech

This function handles speech synthesis for my cloned voice using ElevenLabs API. You can also take advantage of ElvenLabs amazing pre-trained voices.

```
def synthesize_speech_elevenlabs(text, speaker, index):
    data = {
        "text": text,
        "model_id": "eleven_turbo_v2_5",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }
    response = requests.post(elevenlabs_url, json=data, headers=elevenlabs_headers)
    filename = f"audio-files/{index}_{speaker}.mp3"
    with open(filename, "wb") as out:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                out.write(chunk)
    print(f'Audio content written to file "{filename}"')
```

## Generating the Podcast Audio

As the almost final step, we take the conversation and create individual audio clips. Each audio clip is a synthesized speech for each part of the conversation.

Finally, we merge all individual clips into the final full podcast.

```
def generate_audio(conversation):
    os.makedirs('audio-files', exist_ok=True)
    for index, part in enumerate(conversation):
        speaker = part['speaker']
        text = part['text']
        synthesize_speech(text, speaker, index)
    audio_folder = "./audio-files"
    output_file = "podcast.mp3"
    merge_audios(audio_folder, output_file)
```

# Costs to generate a podcast

Given a normal article with 1000 words, let's break down the costs.

![](https://miro.medium.com/v2/resize:fit:700/1*55EXY3chg0_9cwzcR_s-dg.png)

# Conclusion

By leveraging Google’s Text-to-Speech, ElevenLabs, and Vertex AI services, we’ve created a dynamic podcast generator that transforms written articles or any type of text or topic into engaging audio conversations.

This project demonstrates the power of combining AI language models with speech synthesis technologies to create innovative content consumption methods. Whether for educational purposes or enhancing accessibility, the possibilities are vast and exciting.

And don’t forget we could easily produce this podcast in multiple languages within a few minutes. This can also help get more content out for languages that are underrepresented.

# The full code for this article is available on GitHub

## [gen-ai-livestream/podcast-automation at main · SaschaHeyer/gen-ai-livestream](https://github.com/SaschaHeyer/gen-ai-livestream/tree/main/podcast-automation?source=post_page-----e585cfcd0af1---------------------------------------)

### [Contribute to SaschaHeyer/gen-ai-livestream development by creating an account on GitHub.](https://github.com/SaschaHeyer/gen-ai-livestream/tree/main/podcast-automation?source=post_page-----e585cfcd0af1---------------------------------------)

[github.com](https://github.com/SaschaHeyer/gen-ai-livestream/tree/main/podcast-automation?source=post_page-----e585cfcd0af1---------------------------------------)

# Thanks for reading and listening

*I appreciate your feedback and questions. You can find me on* [LinkedIn](https://www.linkedin.com/in/saschaheyer/)*. Even better, subscribe to my [YouTube](https://www.youtube.com/@ml-engineer) channel* ❤️*.*

![](https://miro.medium.com/v2/resize:fit:700/1*rFQZv7_kqHi3sVwN4iv34w.png)