# Add Text-to-Speech to Your Web App with 5 Lines of Python Code | by Pavlo Sydorenko | Medium

Column: https://medium.com/@pavlo_sydorenko/add-text-to-speech-to-your-web-app-with-5-lines-of-python-code-8c4707f2dc93
Processed: No
created on: January 14, 2024 10:20 PM

# Add Text-to-Speech to Your Web App with 5 Lines of Python Code

![](Add%20Text-to-Speech%20to%20Your%20Web%20App%20with%205%20Lines%20of%20761d99d66952482db4750f5f2b2a2f23/1YDWbAa5dvJ92kvJ42butoQ.jpeg)

[Pavlo Sydorenko](https://medium.com/@pavlo_sydorenko?source=post_page-----8c4707f2dc93--------------------------------)

·

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F87415e59d82&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40pavlo_sydorenko%2Fadd-text-to-speech-to-your-web-app-with-5-lines-of-python-code-8c4707f2dc93&user=Pavlo+Sydorenko&userId=87415e59d82&source=post_page-87415e59d82----8c4707f2dc93---------------------post_header-----------)

2 min read

·

Sep 7, 2022

If you want to add a Text-to-Speech feature to your Streamlit app to be able to play sound directly, you should try gTTS.

Photo by [Volodymyr Hryshchenko](https://unsplash.com/@lunarts?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

[](Add%20Text-to-Speech%20to%20Your%20Web%20App%20with%205%20Lines%20of%20761d99d66952482db4750f5f2b2a2f23/0kogZD8ywuIMezyRg)

Google Text-to-Speech *(*gTTS) is a “[Python library and CLI tool to interface with Google Translate’s text-to-speech API](https://pypi.org/project/gTTS/)” (*gTTS is not associated with Google, just to make sure*). So, if you need to convert text into audio, write it to an mp3 file or a file-like object for further manipulations, I suggest you try gTTS. It’s simple and fast to implement, and it provides a relatively decent experience with the most popular languages.

If you are not satisfied with its out-of-the-box performance, you can try to improve the default pre-processing and tokenizing features, adding your own functions, e.g. to account for language-specific abbreviations, etc. It’s highly likely that you will want to play with customization features in case of less popular languages. Also, as of today, there is only one voice available for the audio output.

However, if you want to add a text-to-speech feature to your web app and be able to play sound directly, i.e. without saving it as an mp3 file, you will find gTTS quite useful. And, as promised, you need only a few lines of code to implement this solution, after ‘*pip install gTTS’*.

```
>>> fromgttsimport gTTS
>>> fromioimport BytesIO>>>sound_file = BytesIO()
>>>tts = gTTS('Add text-to-speech to your app', lang='en')
>>>tts.write_to_fp(sound_file)
```

Now, you can easily process this file in e.g. Streamlit.

```
>>>st.audio(sound_file)
```

If can try it with this demo app.

Thank you for taking the time to read or listen to this article!