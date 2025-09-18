# Generative AI exists because of the transformer

Column: https://ig.ft.com/generative-ai/?s=03
Processed: No
created on: October 17, 2023 2:41 PM

![http%3A%2F%2Fft-ig-images-prod.s3-website-eu-west-1.amazonaws.com%2Fv1%2F8306005515-kvnos.jpg](Generative%20AI%20exists%20because%20of%20the%20transformer%2000e4d33203b748f08ceb64c0bded6355/http3A2F2Fft-ig-images-prod.s3-website-eu-west-1.amazonaws.com2Fv12F8306005515-kvnos.jpg)

Over the past few years, we have taken a gigantic leap forward in our decades-long quest to build intelligent machines: the advent of the large language model, or LLM.

This technology, based on research that tries to model the human brain, has led to a new field known as generative AI — software that can create plausible and sophisticated text, images and computer code at a level that mimics human ability.

Businesses around the world have begun to experiment with the new technology in the belief it could transform media, finance, law and professional services, as well as public services such as education. The LLM is underpinned by a scientific development known as the transformer model, made by Google researchers in 2017.

“While we’ve always understood the breakthrough nature of our transformer work, several years later, we’re energised by its enduring potential across new fields, from healthcare to robotics and security, enhancing human creativity, and more,” says Slav Petrov, a senior researcher at Google, who works on building AI models, including LLMs.

LLMs’ touted benefits — the ability to increase productivity by writing and analysing text — are also why it poses a threat to humans. According to Goldman Sachs, it could expose the equivalent of 300mn full-time workers across big economies to automation, leading to widespread unemployment.

As the technology is rapidly woven into our lives, understanding how LLMs generate text means understanding why these models are such versatile cognitive engines — and what else they can help create.

To write text, LLMs must first translate words into a language they understand.

First a block of words is broken into tokens — basic units that can be encoded. Tokens often represent fractions of words, but we’ll turn each full word into a token.

In order to grasp a word’s meaning, work in our example, LLMs first observe it in context using enormous sets of training data, taking note of nearby words. These datasets are based on collating text published on the internet, with new LLMs trained using billions of words.

Eventually, we end up with a huge set of the words found alongside work in the training data, as well as those that weren’t found near it.

As the model processes this set of words, it produces a vector — or list of values — and adjusts it based on each word’s proximity to work in the training data. This vector is known as a word embedding.

A word embedding can have hundreds of values, each representing a different aspect of a word’s meaning. Just as you might describe a house by its characteristics — type, location, bedrooms, bathrooms, storeys — the values in an embedding quantify a word’s linguistic features.

The way these characteristics are derived means we don’t know exactly what each value represents, but words we expect to be used in comparable ways often have similar-looking embeddings.

A pair of words like sea and ocean, for example, may not be used in identical contexts (‘all at ocean’ isn't a direct substitute for ‘all at sea’), but their meanings are close to each other, and embeddings allow us to quantify that closeness.

By reducing the hundreds of values each embedding represents to just two, we can see the distances between these words more clearly.

We might spot clusters of pronouns, or modes of transportation, and being able to quantify words in this way is the first step in a model generating text.

But this alone is not what makes LLMs so clever. What unlocked their abilities to parse and write as fluently as they do today is a tool called the transformer, which radically sped up and augmented how computers understood language.

Transformers process an entire sequence at once — be that a sentence, paragraph or an entire article — analysing all its parts and not just individual words.

This allows the software to capture context and patterns better, and to translate — or generate — text more accurately. This simultaneous processing also makes LLMs much faster to train, in turn improving their efficiency and ability to scale.

Research outlining the transformer model was first [published](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html) by a group of [eight AI researchers at Google in June 2017](https://www.ft.com/content/37bb01af-ee46-4483-982f-ef3921436a50). Their 11-page research paper marked the start of the generative AI era.

A key concept of the transformer architecture is self-attention. This is what allows LLMs to understand relationships between words.

Self-attention looks at each token in a body of text and decides which others are most important to understanding its meaning.

Before transformers, the state of the art AI translation methods were recurrent neural networks (RNNs), which scanned each word in a sentence and processed it sequentially.

With self-attention, the transformer computes all the words in a sentence at the same time. Capturing this context gives LLMs far more sophisticated capabilities to parse language.

In this example, assessing the whole sentence at once means the transformer is able to understand that interest is being used as a noun to explain an individual’s take on politics.

If we tweak the sentence . . .

. . . the model understands interest is now being used in a financial sense.

And when we combine the sentences, the model is still able to recognise the correct meaning of each word thanks to the attention it gives the accompanying text.

For the first use of interest, it is no and in that are most attended.

For the second, it is rate and bank.

This functionality is crucial for advanced text generation. Without it, words that can be interchangeable in some contexts but not others can be used incorrectly.

Effectively, self-attention means that if a summary of this sentence was produced, you wouldn’t have enthusiasm used when you were writing about interest rates.

This capability goes beyond words, like interest, that have multiple meanings.

In the following sentence, self-attention is able to calculate that it is most likely to be referring to dog.

And if we alter the sentence, swapping hungry for delicious, the model is able to recalculate, with it now most likely to refer to bone.

The benefits of self-attention for language processing increase the more you scale things up. It allows LLMs to take context from beyond sentence boundaries, giving the model a greater understanding of how and when a word is used.

One of the world’s largest and most advanced LLMs is GPT-4, OpenAI’s latest artificial intelligence model which the company says exhibits “human-level performance” on several academic and professional benchmarks such as the US bar exam, advanced placement tests and the SAT school exams.

GPT-4 can generate and ingest large volumes of text: users can feed in up to 25,000 English words, which means it could handle detailed financial documentation, literary works or technical manuals.

The product has reshaped the tech industry, with the world’s biggest technology companies — including Google, Meta and Microsoft, who have backed OpenAI — racing to dominate the space, alongside smaller start-ups.

The LLMs they have released include Google’s PaLM model, which powers its chatbot Bard, Anthropic’s Claude model, Meta’s LLaMA and Cohere’s Command, among others.

While these models are already being adopted by an array of businesses, some of the companies behind them are [facing legal battles](https://www.ft.com/content/704d0bba-2653-4a27-bee1-ee45c6ed1080) around their use of copyrighted text, images and audio scraped from the web.

The reason for this is that current LLMs are trained on most of the English-language internet — a volume of information that makes them far more powerful than previous generations.

From this enormous corpus of words and images, the models learn how to recognise patterns and eventually predict the next best word.

After tokenising and encoding a prompt, we’re left with a block of data representing our input as the machine understands it, including meanings, positions and relationships between words.

At its simplest, the model’s aim is now to predict the next word in a sequence and do this repeatedly until the output is complete.

To do this, the model gives a probability score to each token, which represents the likelihood of it being the next word in the sequence.

And it continues to do this until it is happy with the text it has produced.

But this method of predicting the following word in isolation — known as “greedy search” — can introduce problems. Sometimes, while each individual token might be the next best fit, the full phrase can be less relevant.

Not necessarily always wrong, but perhaps not what you’d expect either.

Transformers use a number of approaches to address this problem and enhance the quality of their output. One example is called beam search.

Rather than focusing only on the next word in a sequence, it looks at the probability of a larger set of tokens as a whole.

With beam search, the model is able to consider multiple routes and find the best option.

This produces better results, ultimately leading to more coherent, human-like text.

But things don’t always go to plan. While the text may seem plausible and coherent, it isn’t always factually correct. LLMs are not search engines looking up facts; they are pattern-spotting engines that guess the next best option in a sequence.

Because of this inherent predictive nature, LLMs can also fabricate information in a process that researchers call “hallucination”. They can generate made-up numbers, names, dates, quotes — even web links or entire articles.

Users of LLMs have shared examples of links to non-existent news articles on the FT and Bloomberg, made-up references to research papers, the wrong authors for published books and biographies riddled with factual mistakes.

In one [high-profile incident in New York](https://www.nytimes.com/2023/06/08/nyregion/lawyer-chatgpt-sanctions.html), a lawyer used ChatGPT to create a brief for a case. When the defence interrogated the report, they discovered it was littered with made-up judicial opinions and legal citations. “I did not comprehend that ChatGPT could fabricate cases,” the lawyer later told a judge during his own court hearing.

Although researchers say hallucinations will never be completely erased, Google, OpenAI and others are working on limiting them through a process known as “grounding”. This involves cross-checking an LLM’s outputs against web search results and providing citations to users so they can verify.

Humans are also used to provide feedback and fill gaps in information — a process known as reinforcement learning by human feedback (RLHF) — which further improves the quality of the output. But it is still a big research challenge to understand which queries might trigger these hallucinations, as well as how they can be predicted and reduced.

Despite these limitations, the transformer has resulted in a host of cutting-edge AI applications. Apart from powering chatbots such as Bard and ChatGPT, it drives autocomplete on our mobile keyboards and speech recognition in our smart speakers.

Its real power, however, lies beyond language. Its inventors discovered that transformer models could recognise and predict any repeating motifs or patterns. From pixels in an image, using tools such as Dall-E, Midjourney and Stable Diffusion, to computer code using generators like GitHub CoPilot. It could even predict notes in music and DNA in proteins to [help design](https://www.ft.com/content/dd557790-a39b-4fd1-8f18-c73532a61b3e) drug molecules.

For decades, researchers built specialised models to summarise, translate, search and retrieve. The transformer unified all those actions into a single structure capable of performing a huge variety of tasks.

“Take this simple model that predicts the next word and it . . . can do anything,” says Aidan Gomez, chief executive of AI start-up Cohere, and a co-author of the transformer paper.

Now they have one type of model that is “trained on the entire internet and what falls out the other side does all of that and better than anything that came before”, he says.

“That is the magical part of the story.”

*This story is free to read so you can share it with family and friends who don’t yet have an FT subscription.*

[Madhumita Murgia](https://www.ft.com/madhumita-murgia) is the FT’s artificial intelligence editor.

Visual storytelling team: [Dan Clark](https://www.ft.com/dan-clark), [Sam Learner](https://www.ft.com/sam-learner), [Irene de la Torre Arenas](https://www.ft.com/irene-de-la-torre-arenas), [Sam Joiner](https://www.ft.com/sam-joiner), [Eade Hemingway](https://www.ft.com/eade-hemingway) and [Oliver Hawkins](https://www.ft.com/oliver-hawkins).

With thanks to Slav Petrov, Jakob Uszkoreit, Aidan Gomez and Ashish Vaswani.

To generate the 50D word embeddings we used the GloVe 6B 50D pre-trained model and converted to Word2Vec format. To generate the 2D representation of word embeddings we used the BERT large language model and reduced dimensionality using UMAP. The self-attention values and the probability scores in the beam search section are conceptual.

We used the free version of [ChatGPT-3.5](https://chat.openai.com/) to generate some of the example sentences used in the visual part of the word embedding and self attention section.