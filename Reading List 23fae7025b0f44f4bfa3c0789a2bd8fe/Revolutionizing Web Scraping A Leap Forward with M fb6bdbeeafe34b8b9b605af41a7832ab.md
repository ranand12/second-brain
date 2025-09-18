# Revolutionizing Web Scraping: A Leap Forward with Multimodal Language Models | by Somnath Banerjee | Dec, 2023 | Medium

Column: https://somnath-banerjee.medium.com/revolutionizing-web-scraping-a-leap-forward-with-multimodal-language-models-96485dd17f07
Processed: No
created on: December 10, 2023 9:03 PM

# Revolutionizing Web Scraping: A Leap Forward with Multimodal Language Models

![](Revolutionizing%20Web%20Scraping%20A%20Leap%20Forward%20with%20M%20fb6bdbeeafe34b8b9b605af41a7832ab/1q8gs5FEu3FQZGeAJhNrstw.jpeg)

[Somnath Banerjee](https://somnath-banerjee.medium.com/?source=post_page-----96485dd17f07--------------------------------)

·

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fab6dc6e45e61&operation=register&redirect=https%3A%2F%2Fsomnath-banerjee.medium.com%2Frevolutionizing-web-scraping-a-leap-forward-with-multimodal-language-models-96485dd17f07&user=Somnath+Banerjee&userId=ab6dc6e45e61&source=post_page-ab6dc6e45e61----96485dd17f07---------------------post_header-----------)

5 min read

·

19 hours ago

Authors: [Somnath Banerjee](https://www.linkedin.com/in/somnath-banerjee/) and [Matt Herich](https://www.linkedin.com/in/matt-herich/)

Web scraping, the extraction of data from websites, is a crucial practice in various industries for gathering valuable data and insights. From retailers analyzing competitor pricing to sales teams prospecting leads on LinkedIn, web scraping fuels valuable insights and informed decision-making.

Despite its widespread use, web scraping comes with challenges, especially in maintaining the scraper’s accuracy amidst HTML page changes. Teams often struggle to keep up with modifications in HTML and CSS classes, which can render scrapers ineffective.

Enter the transformative potential of multimodal large language models (LLMs) like OpenAI’s GPT-4 and Google’s Gemini. These advanced models possess image understanding capabilities, enabling them to extract data directly from website screenshots, bypassing the need for complex HTML/CSS parsing. By utilizing screenshots of webpages, these LLMs can replace hundreds or thousands of lines of code with just a few natural language sentences, revolutionizing the web scraping landscape. This paradigm shift dramatically simplifies the web scraping technology and reduces development and maintenance costs significantly.

In this article, we do a comparative analysis between GPT-4 and BARD (currently powered by Gemini Pro) in the following information extraction tasks across Sales and Real Estate use cases.

## Sales use cases

1. [Extract customer names from a company homepage](https://somnath-banerjee.medium.com/revolutionizing-web-scraping-a-leap-forward-with-multimodal-language-models-96485dd17f07#7c40)
2. [Obtain company information from a logo](https://somnath-banerjee.medium.com/revolutionizing-web-scraping-a-leap-forward-with-multimodal-language-models-96485dd17f07#6caf)
3. [Extract company information from LinkedIn Sales Navigator](https://somnath-banerjee.medium.com/revolutionizing-web-scraping-a-leap-forward-with-multimodal-language-models-96485dd17f07#6b36)
4. [Extract people information from LinkedIn Sales Navigator](https://somnath-banerjee.medium.com/revolutionizing-web-scraping-a-leap-forward-with-multimodal-language-models-96485dd17f07#3e6c)

## Real Estate use cases

1. [Extract property information from a Zillow listing](https://somnath-banerjee.medium.com/revolutionizing-web-scraping-a-leap-forward-with-multimodal-language-models-96485dd17f07#f8ef)
2. [Extract property information from an Airbnb listing](https://somnath-banerjee.medium.com/revolutionizing-web-scraping-a-leap-forward-with-multimodal-language-models-96485dd17f07#75c2)

In many of the information extraction tasks GPT-4 outperforms BARD. Only in the case of obtaining company information from a given logo BARD performs much better.

# Conclusion

The capability to extract information directly from webpage screenshots represents a groundbreaking shift in technology. This innovation holds the potential to streamline web scraping processes, boosting efficiency, and substantially reducing costs. GPT-4 continues to stand out as the leading model for extracting information from web pages, while BARD showcases exceptional abilities in recognizing company logos, thereby broadening the range of potential applications for this remarkable technology.

# Appendix

Provided below are the exact prompts and screenshots used for readers to explore. You need ChatGPT plus account to run the GPT-4 tests. Keep in mind that GPT-4 and BARD are not deterministic, and results may vary based on the dynamic nature of these models and potential changes in the image when downloaded from medium platform.

## Extract customer names from a company homepage

**Prompt**

```
Attached screenshot is a company homepage. At the bottom of the page there are logos of their customers. Extract all the customer names corresponding to those logos
```

![](Revolutionizing%20Web%20Scraping%20A%20Leap%20Forward%20with%20M%20fb6bdbeeafe34b8b9b605af41a7832ab/1jqy1i5_eOiwjR3POT8EXJw.png)

**GPT-4**

**Note:** We need to update the prompt asking ChatGPT not to use code interpreter

![](Revolutionizing%20Web%20Scraping%20A%20Leap%20Forward%20with%20M%20fb6bdbeeafe34b8b9b605af41a7832ab/1HghQgBxpubqKdbnhAgaeBw.png)

**BARD**

![](Revolutionizing%20Web%20Scraping%20A%20Leap%20Forward%20with%20M%20fb6bdbeeafe34b8b9b605af41a7832ab/17HB5ss4gmFT2Ufq7ZCoQvw.png)

**Note:** GPT-4 got all the customer names correct whereas BARD got *DCP Midstream* wrong

## Obtain company information from a logo

**Prompt**

```
Which company's logo is this?
```

![](Revolutionizing%20Web%20Scraping%20A%20Leap%20Forward%20with%20M%20fb6bdbeeafe34b8b9b605af41a7832ab/1wial4ZAE2MamXKhdkkvsXw.png)

**GPT-4**

![](Revolutionizing%20Web%20Scraping%20A%20Leap%20Forward%20with%20M%20fb6bdbeeafe34b8b9b605af41a7832ab/19KSeZLCLdJ0RDpxzTmborg.png)

**BARD**

![](Revolutionizing%20Web%20Scraping%20A%20Leap%20Forward%20with%20M%20fb6bdbeeafe34b8b9b605af41a7832ab/1jgJ7S3lobW2zIrJGhDLGPw.png)

We found GPT-4 often fails in this tasks, whereas BARD excels at recognizing company logos.

Interestingly we found that Google image search performs significantly better when searching by company logos, suggesting it could provide better training data for Gemini. Below is a comparison of Google and Bing searches for the Opsera logo.

![](Revolutionizing%20Web%20Scraping%20A%20Leap%20Forward%20with%20M%20fb6bdbeeafe34b8b9b605af41a7832ab/1n0tyOBCafSovBAjTnscegg.png)

## Extract company information from LinkedIn Sales Navigator

**Prompt**

```

Extract all the texts from the screenshot. The texts are a list of company name, linkedin industry, number of employees and 1 line about the company. Extract all the texts you can and put it in a list format
```

![](Revolutionizing%20Web%20Scraping%20A%20Leap%20Forward%20with%20M%20fb6bdbeeafe34b8b9b605af41a7832ab/1LVaqSJmNYG6cE1B2uOrEaQ.png)

**GPT-4**

![](Revolutionizing%20Web%20Scraping%20A%20Leap%20Forward%20with%20M%20fb6bdbeeafe34b8b9b605af41a7832ab/14Vg3YET6pZLsAsEAXm5lxA.png)

**BARD**

![](Revolutionizing%20Web%20Scraping%20A%20Leap%20Forward%20with%20M%20fb6bdbeeafe34b8b9b605af41a7832ab/1BbqgAIWGl4CiwH5pHRgOtw.png)

## Extract people information from LinkedIn Sales Navigator

**Prompt**

```
Extract all the texts from the screenshot. The texts are a list of person names, their title, time in current role, time in current company, a short description about them and their experience. Extract all the texts you can and put it in a list format
```

![](Revolutionizing%20Web%20Scraping%20A%20Leap%20Forward%20with%20M%20fb6bdbeeafe34b8b9b605af41a7832ab/1nPF6XMYCEsJHn0oXcA-ZFA.png)

**GPT-4**

**BARD**

![](Revolutionizing%20Web%20Scraping%20A%20Leap%20Forward%20with%20M%20fb6bdbeeafe34b8b9b605af41a7832ab/17SHAdNuIIIF9bm0ji597NQ.png)

## Extract property information from a Zillow listing

**Prompt**

```

Attached is the screenshot of a property listing page on Zillow. Extract property price, address, beds, bath, square feet, HOA information from the screenshot
```

![](Revolutionizing%20Web%20Scraping%20A%20Leap%20Forward%20with%20M%20fb6bdbeeafe34b8b9b605af41a7832ab/1NkmKtCmIeeExZJmd81ER6g.png)

**GPT-4**

![](Revolutionizing%20Web%20Scraping%20A%20Leap%20Forward%20with%20M%20fb6bdbeeafe34b8b9b605af41a7832ab/118E3wHcRiJKzwPQK1ajbhA.png)

**BARD**

Unable to extract information from this page

## Extract property information from an Airbnb listing

**Prompt**

```
Attached is a screenshot of an Airbnb listing. Extract nightly rate, number of reviews, rating, city state, guests, beds and baths from the screenshot.
```

![](Revolutionizing%20Web%20Scraping%20A%20Leap%20Forward%20with%20M%20fb6bdbeeafe34b8b9b605af41a7832ab/1nVxljV8n5y92eEM7VhAQaA.png)

**GPT-4**

![](Revolutionizing%20Web%20Scraping%20A%20Leap%20Forward%20with%20M%20fb6bdbeeafe34b8b9b605af41a7832ab/1AbEfGyHnqye9K56ad33tVw.png)

**BARD**

![](Revolutionizing%20Web%20Scraping%20A%20Leap%20Forward%20with%20M%20fb6bdbeeafe34b8b9b605af41a7832ab/18bXlynWwVT68tSxy3YPuTw.png)