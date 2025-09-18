# Function Calling with Gemini API and Google Apps | Appsbroker CTS Google Cloud Tech Blog

Column: https://medium.com/cts-technologies/genai-for-google-workspace-exploring-gemini-api-function-calling-with-google-apps-script-part-3-028785dafe3b
Processed: No
created on: January 9, 2024 3:45 PM

# GenAI for Google Workspace: Exploring Gemini API Function Calling with Google Apps Script — Part 3

[](Function%20Calling%20with%20Gemini%20API%20and%20Google%20Apps%20A%20c121be37a3554b6697a89b4dfdfdd66e/0nVPVK_nhjM107SHr)

![](Function%20Calling%20with%20Gemini%20API%20and%20Google%20Apps%20A%20c121be37a3554b6697a89b4dfdfdd66e/1ea1fDs94xA_eHofoFkjBZQ.png)

[Martin Hawksey](https://medium.com/@martin.hawksey?source=post_page-----028785dafe3b--------------------------------)

·

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F58fd88568021&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fcts-technologies%2Fgenai-for-google-workspace-exploring-gemini-api-function-calling-with-google-apps-script-part-3-028785dafe3b&user=Martin+Hawksey&userId=58fd88568021&source=post_page-58fd88568021----028785dafe3b---------------------post_header-----------)

Published in

[Appsbroker CTS Google Cloud Tech Blog](https://medium.com/cts-technologies?source=post_page-----028785dafe3b--------------------------------)

·

6 min read

·

1 day ago

![](Function%20Calling%20with%20Gemini%20API%20and%20Google%20Apps%20A%20c121be37a3554b6697a89b4dfdfdd66e/1pWQ-FPI_4eSXzTvsA1dklA.jpeg)

Having previously looked at the [possibilities with the PaLM 2 API and Google Sheets data](https://medium.com/cts-technologies/genai-for-google-workspace-exploring-the-palm-2-api-and-llm-capabilities-in-google-sheets-part-2-bb75aaef8d9f), in this post we switch to the newly announced Google Gemini API. Gemini is a family of multimodal generative AI models, which come with new capabilities including [Function Calling](https://cloud.google.com/vertex-ai/docs/generative-ai/multimodal/function-calling):

> Function calling lets developers create a description of a function in their code, and then pass that description to a language model in a request. The response from the model includes the name of a function that matches the description and the arguments to call it with. … Function calling returns JSON with the name of a function and the arguments to use in your code.
> 

Function calling isn’t new and several existing generative AI products, including OpenAI’s ChatGPT, already have this capability. In terms of Google Workspace, function calling has already been made easier with the publication of the [ChatGPTApp library](https://github.com/scriptit-fr/ChatGPTApp) by the team at Scriptit.fr which uses OpenAI’s ChatGPT models.

The ChatGPTApp library has been published on Github with an open source licence and given both ChatGPT and Gemini use a similar API definition I’ve used this as the basis of a [GeminiApp library](https://github.com/mhawksey/GeminiApp) which supports function calling.

The [GeminiApp library](https://github.com/mhawksey/GeminiApp) repo includes some examples of function calling but for this post, I wanted to focus on Gemini’s capabilities with Google Sheets data. For this I’ve revisited the [original example shared by Romain Vailard included as part of the original ChatGPTApp launch](https://romain-vialard.medium.com/introducing-chatgptapp-a-new-library-for-google-apps-script-aee672b8d22a) (If this is something you would like to test yourself at the end of the post I’ve shared all the code and setup instructions).

Function Calling in Google Sheets with Gemini Pro

![](Function%20Calling%20with%20Gemini%20API%20and%20Google%20Apps%20A%20c121be37a3554b6697a89b4dfdfdd66e/1qfELmTUAC6DBV6_cmDgduA.gif)

# The scenario

The scenario is creating a personalised mail merge based on subscribers' preferred topics. To summarise what is happening here, we are declaring two functions to Gemini, one to `getContactList()` to return Google Sheet data; and `sendMessage()` which can send an email to one of our contacts with their personalised tip.

This is orchestrated in a single function which declares the functions we can run, the parameters (if required) and an initial message to start the interaction with Gemini:

```
function sendCodingTipsByEmail() {
  GeminiApp.init(VERTEX_AI_LOCATION_ID, PROJECT_ID);

  var getContactList = GeminiApp.newFunction()
    .setName("getContactList")
    .setDescription("Retrieves a list of contacts, including their name, email address and tip topic from the values in a 2D Array format with a header in row 1");

  var sendMessageFunction = GeminiApp.newFunction()
    .setName("sendMessage")
    .setDescription("Send an email to a list of contacts")
    .addParameter("recipientEmail", "STRING", "The email address of the recipient")
    .addParameter("subject", "STRING", "The email subject")
    .addParameter("body", "STRING", "The email body in Markdown format (e.g. CommonMark or GitHub Flavored Markdown (GFM))");

  var resp = GeminiApp.newChat()
    .addContent(`Send a useful personalised Google Apps Script coding tip for each of my contacts using the suggested tip topic from my Google Sheet data. You must provide responses to sendMessage until there are no email addresses left in the Google Sheet data. The tip message must be over 400 words`)
    .addFunction(getContactList)
    .addFunction(sendMessageFunction)
    .run({ temperature: 0.4 });

  console.log(resp.content.parts[0].text);
}
```

Gemini doesn’t run the functions, it only provides the function name and parameters, which are then executed in Apps Script. This means the functions will be run as the user, in other words, the next time your boss asks for a bunch of personalised emails you can look like the hero thanks to Gemini.

# Conversations with data

To understand the power of what is happening here it’s worth taking a closer look at the `getContactList()` function:

```
function getContactList() {
  const data = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0].getDataRange().getValues();
  return { values: data }
}
```

All this function is doing is returning a 2D array from our Google Sheet. Gemini is then able to interpret the data based on how it has been described:

> Retrieves a list of contacts, including their name, email address and tip topic from the values in a 2D Array format with a header in row 1
> 

Of course it is relatively easy to script something that turns a Google Sheet into easier to use data, however, with Gemini there is the opportunity to do something less constrained by code. For example, rather than getting all of the data from the first tab you can start using natural language to let the user describe what data they need.

So instead of:

> ‘Send a personalised Google Apps Script coding tip for each of my contacts.’
> 

it could be:

> ‘Send a Google Apps Script debugging tip for all my contacts that work at CTS’
> 

or:

> 'Send a recommendation to watch Totally Unscripted (https://tu.appsscript.info) for all my contacts that have the first name Martin in my Google Sheet data.'
> 

What I’m trying to emphasise here is there is an opportunity to use natural language to allow users to have conversations with their data. With the capabilities of function calling in Gemini it is possible to turn those conversations into actions.

# Try it

If you would like to try this yourself you can follow these steps:

1. [Select or create a Cloud Platform project](https://console.cloud.google.com/project)
2. [Enable the Vertex AI API](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com)
3. Copy [Gemini Pro Function Calling [Shared]](https://docs.google.com/spreadsheets/d/1Qv-j2-l4A562HgZinfoPdv0shZA8Zgp0szMBv88GGGs/copy)

In your copy of the Google Sheet

1. Update the data in Sheet1 with test email addresses and topics
2. Open **Extensions > Apps Script** and for PROJECT_ID insert the Cloud Project ID from Step 1 and click Save
3. **Run > sendCodingTipsByEmail** (you will probably need to do this twice, the first time to authenticate)

# Caveats and considerations

Gemini is still in public preview and final functionality may change. A couple of callouts from my own experimentations with Gemini are:

- **Fiddling with the data returned (especially if you require formatting)** — For larger pieces of text such as email messages you might have to do a little post-processing. In my testing I found requesting Markdown syntax then converting to HTML with [Showdown.js](https://github.com/showdownjs/showdown) was more reliable than just requesting HTML, even then there was a little tidy-up required.
- **Human mediation** — In this example we’ve gone straight to the send button, which given the nature of LLMs is risky as they can be very random. This means that it’s important to be careful when using them in production applications. For example, instead of sending it would be better to generate drafts from human approval.
- **Prototyping not production (yet)** — Gemini is in public preview and the current quotas are aligned to experimentation, not production applications. The `us-central1` data region used in this example has the most generous quota limit with 60 content requests per minute. The good news is you can try Gemini for free until general availability later this year, so there is plenty of opportunity to prototype without busting the bank. General availability [pricing has been announced](https://blog.google/technology/ai/gemini-api-developers-cloud/#:~:text=Cloud%20blog.-,Gemini%20Pro%20pricing,-Right%20now%2C%20developers) and summarised below:

Image credit: Google — Gemini Pro pricing

[](Function%20Calling%20with%20Gemini%20API%20and%20Google%20Apps%20A%20c121be37a3554b6697a89b4dfdfdd66e/0evhoXgWGS7ca-JNj)

# Finally…

If you would like to discover more about function calling Google has [published a Google Colab notebook on Function Calling with the Vertex AI Gemini API & Python SDK](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/intro_function_calling.ipynb). If you are interested in integrating Gemini into your Google Workspace experience feel free to [get in touch](https://cts.co/contact-us/).

A big thank you also to Guillemine Allavena and Romain Vialard at Scriptit.fr for sharing the original ChatGPTApp library, without it this post wouldn’t have been possible.