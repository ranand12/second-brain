# Frequently Asked Questions about My Writing Process

Column: https://eugeneyan.com/writing/writing-faq/
Processed: Yes
created on: April 2, 2025 10:17 AM

Every month or so, I receive questions about my writing: “How did you get started?” “Why do you write?” “Who do you write for?” “What’s your writing process?”

I’ve procrastinated writing this FAQ for a while because, honestly, who cares about *my* writing process? But after answering the same questions again and again, I realized it’d be helpful to consolidate my responses somewhere. At the very least, it’ll save me from repeating myself. If you’re thinking about writing online but aren’t sure where or how to start, this FAQ is for you.

### How did you get started writing?

Years ago, when I was a junior data scientist, I reached out to several experienced folks—senior data scientists, heads of data science, even CTOs—and asked them: “What makes an effective data scientist?” Was it PhD-level research skills, coding expertise, the ability to analyze and prepare terabyte-level datasets, deep domain knowledge, or something else?

Their answers surprised me. While they acknowledged that those technical skills were important, a majority highlighted an entirely different skill—communication.

They explained that their most effective data scientists stood out because they could listen carefully, hear the real and unspoken challenges stakeholders faced, identify how machine learning could help, and write clear requirements for science and engineering teams. They could discuss statistics and machine learning clearly and simply, without relying on jargon like “Mahalanobis Distance” or “Restricted Boltzmann Machines” as a crutch, and instead focused on relatable outcomes like “catch more fraud” or “increase conversions”. As a result, these skilled communicators found it easier to gain buy-in, execute effectively, and earn trust.

I was skeptical. I had a hard time believing that a non-technical skill like communication could significantly impact success in a technical role like data science. But after hearing the same advice from several mentors, I decided to test it myself and committed to working on my communication for a year. In that year, I volunteered to speak at every internal workshop and external conference, wrote and edited company-wide newsletters, and started this site.

I’ve benefitted greatly from this habit since then. Writing consistently has reinforced my learning, sharpened my thinking, helped me make friends online, accelerated my career growth, and more. That’s why I continue to practice writing online.

### Why do you write?

First, I write to learn. This usually happens when I’m exploring a topic but struggle to find resources online. Maybe the information is scattered across papers and tech blogs, or perhaps the topic lacks a clear overarching framework. Diving into the literature, testing the ideas via experiments, and writing about it helps me simplify what I learn into practical, reusable patterns. Writing also reveals gaps in my understanding and helps me clarify my thoughts. Examples of such writing include [RecSys System Design](https://eugeneyan.com/writing/system-design-for-discovery/), [Feature Store Hierarchy of Needs](https://eugeneyan.com/writing/feature-stores/), [Patterns for LLM-based Systems](https://eugeneyan.com/writing/llm-patterns/), [Evaluating LLM-evaluators](https://eugeneyan.com/writing/llm-evaluators/), [Lessons from Applying LLMs](https://eugeneyan.com/writing/llm-lessons/).

I also write to share knowledge. Sometimes, this happens when I receive the same question multiple times and writing my response somewhere makes sharing more scalable. Other times, it’s because I believe the information is valuable and can help others. Examples of such writing are [OMSCS FAQ](https://eugeneyan.com/writing/georgia-tech-omscs-faq/), [Writing Why What How](https://eugeneyan.com/writing/writing-docs-why-what-how/), [Prompting Fundamentals](https://eugeneyan.com/writing/prompting/), [How to Interview ML/AI engineers](https://eugeneyan.com/writing/how-to-interview/), and [MacBook Pro Setup](https://eugeneyan.com/writing/mac-setup/).

Occasionally, I write to express disagreement. This might mean challenging the anti-pattern of data scientists throwing models over the wall to engineers to productionize, technical folks overcomplicating their work for publication or promotions, or voicing my frustration when academic evals of LLMs don’t match real-world product outcomes. Writing these pieces was somewhat cathartic, and some have sparked constructive debates, which gives me hope that they’ve positively influenced the field. Examples include [Data Scientists Should Be More End-to-End](https://eugeneyan.com/writing/end-to-end-data-science/), [Start without Machine Learning](https://eugeneyan.com/writing/first-rule-of-ml/), [Simplicity > Complexity](https://eugeneyan.com/writing/simplicity/), [LLM Evals that Don’t Work](https://eugeneyan.com/writing/evals/).

Lastly, all my writing (and social media) serves as my bat signal. It’s my way of saying, “Here’s what I’m thinking a lot about and working on! If you’re exploring similar ideas or have similar challenges, please reach out!” This has been surprisingly effective and has led to insightful discussions and valuable friendships with senpais and fellow practitioners in areas like RecSys, LLM-powered systems, and evals. I’ve learned lots and made many friends this way.

### Who do you write for?

First, I write for myself. Writing helps me reinforce what I’ve learned and clarify my thinking. And because I’m writing for myself, I focus on topics I’m actually interested in. The downside is that I can’t force myself to write about something I’m not passionate about, even if someone offers to pay me a lot of money. (I could, but the writing would be bad.)

I often compare writing to single-player and multiplayer games. While there are multiplayer benefits like networking, gaining a reputation, and job opportunities, I encourage focusing on the single-player aspects such as gaining skill points in communication (also persuasion and influence), learning more deeply, and leveling up yourself. This way, even if no one reads your work and the multiplayer benefits don’t pan out, you’ll always have the single-player gains.

My second audience is my team and fellow practitioners. With them I share industry-proven methods, best practices, and design patterns to help us be better at our work. Since they’re familiar with the field, I can comfortably use technical jargon to keep the writing concise; otherwise, each piece would become excessively long if I had to start from the basics and explain every concept. (My reference point for technical writing includes [Lilian Weng](https://lilianweng.github.io/posts/2024-11-28-reward-hacking/) and [Chip Huyen](https://huyenchip.com/2025/01/07/agents.html).) As a result, readers occasionally comment on the use of jargon (below). This is understandable and doesn’t bother me—not everyone is the intended audience.

> 
> 
> 
> I started listening to this article (using a text to speech model) after waking up.
> 
> I thought it was very heavy on jargon. Like, it was written to make the author appear very intelligent without necessarily effectively conveying information to the audience. This is something that I’ve often seen authors do in academic papers, and my one published research paper (not first author) is no exception.
> 
> I’m by no means an expert in the field of ML, so perhaps I am just not the intended audience. I’m curious if other people here felt the same way.
> 
> Hopefully this observation / opinion isn’t too negative. — [Source](https://news.ycombinator.com/item?id=43453259)
> 

My third audience is the leadership at my organization. For example, in early 2023, I received questions about finetuning, RAG, evaluations, etc. Thus, I spent several weeks researching and distilling my thoughts into practical patterns. The result was [Patterns for Building LLM-based Systems & Products](https://eugeneyan.com/writing/llm-patterns/). To my surprise, despite its length (over an hour of reading time), some leaders read it. This enabled our organization to move beyond basic questions and begin tackling thornier challenges in the trenches.

There’s a tension between balancing the needs of the tech team and leadership. The team values details on the data, methodology, evals, ablation studies, etc.—the “how”. Leadership, however, is more interested in the bigger picture and what it means for customers and the business—the “why”. I think that striving to write for both audiences simultaneously helps me become a more effective and practical writer.

Finally, I write for the community. My aim is to help others deepen their understanding and fill knowledge gaps. I’ve gained a lot from other writers on the internet and this is my way of contributing back, by patching gaps of information and knowledge via my writing.

### How do you decide what to write about?

I typically write about what’s relevant to my work at the time. For example, in 2020, I started a new role focused on [recommendation systems](https://eugeneyan.com/tag/recsys/) and wanted to consolidate my learning from Lazada, Alibaba, and Amazon. Then from 2023, as my work shifted toward experimenting and building with [LLMs](https://eugeneyan.com/tag/llm/), my writing has naturually reflected that new focus.

### How did you find your niche?

I never thought about my niche—I just wanted to write about what interests me and practice my writing. If there was anything, at the end of 2020, I noticed that my write-ups on machine learning and data science had consistently higher open rates (below). This suggested that my readers found these topics valuable.

![](https://eugeneyan.com/assets/openrate-2020-themes.jpg)

Email open-rate in 2020 by themes

With this insight, I started writing [teardowns](https://eugeneyan.com/tag/teardown/) of machine learning and recommendation systems in 2021 which became popular with the community. I considered popularity as a proxy metric for usefulness and thus continued writing similar pieces, including [surveys](https://eugeneyan.com/tag/survey/).

Nonetheless, I enjoy exploring and writing about other topics—such as [mechanisms](https://eugeneyan.com/tag/mechanism/), [writing](https://eugeneyan.com/tag/writing/), and [career](https://eugeneyan.com/tag/career/)—and put out pieces from time to time.

### How did you choose what platform to write on?

I started with WordPress because it was the simplest option at the time. It allowed me to focus on writing and not have to concern myself with the details of building the site or hosting it.

After a few years, I wanted more flexibility and customization than WordPress could offer, so I migrated to Jekyll. It was, and still is, free to host on GitHub Pages. This also gave me the opportunity to tinker with the frontend via basic CSS and JavaScript.

### What’s your writing pipeline? Do you have a template?

My writing usually begins as a bullet-point outline in Obsidian. At the top, I jot down what I’m planning to share, why I think it’s valuable, and who the intended audience is. Then, I sketch out section headers and add bullet points as I review literature or whenever something comes to mind. Drafting with bullet points helps me stay flexible—I can rearrange, remove, or expand points without worrying about the overall structure. In addition, writing bullet points feels easier and less intimidating than writing full sentences and paragraphs. This makes the drafting process more fun. At this stage, I leave the introduction and conclusion blank.

Once the outline is detailed enough, I convert it into prose. By this stage, the outline should have enough detail to make writing sentences straightforward. Although LLMs can do this now, I enjoy crafting the sentences and structuring the flow of paragraphs myself. After finishing the main body, I write the introduction and conclusion, putting extra effort into an introduction that tries to hook the reader without overselling the content.

In the final stage, I do the standard spelling and grammar checks. Finally, I read through it one last time and edit for clarity and readability. The finished markdown is then pasted into my Jekyll site and I add images as needed.

I don’t have a specific template.

### Can I write about a topic I just started learning about?

Yes! Think of expertise as a ladder—wherever you are on it, there are going to be people above *and below* you. While you’re learning from those above, those who are just starting can also learn from you. Beyond helping others, writing also reinforces your understanding of the topic. My friend Swyx has an inspiring essay on this approach called [Learning in Public](https://www.swyx.io/learn-in-public).

### What’s the right frequency to write?

Aim for a frequency that is just slightly beyond your comfort zone yet still sustainable.

If you’re just starting to write online, I recommend focusing on quantity over quality, at least until you build the habit. Aim to publish weekly, or at the very least, monthly. Once writing consistently becomes second nature, you can shift your focus to improving quality.

### How do you overcome the perfectionist mindset?

It helps to timebox each piece you write. Set a deadline by which you’ll publish and stick to it. Also, understand that writing will never be perfect—there’s always something that can be improved. Accepting this imperfection helps ease the pressure. Finally, publishing something doesn’t mean you can’t update or improve it later. The important thing is to hit “publish”.

### How did you build a brand for yourself?

I don’t think I have a brand, and even if I do, it wasn’t built consciously. If anything, it probably comes from consistent output and relatively clear writing at the practical intersection of recommender systems, LLM-powered products, and production.

### How do you balance writing (so much) and your day job?

When working on a substantial piece, I spend an hour or two each weeknight reading and taking notes on research papers and technical articles. Over the weekdays, this adds up to 5 - 10 papers. On weekends, aside from snowboarding in winter and hiking in summer, I can spend up to eight hours per day on research and writing.

Of course, having an incredibly understanding wife helps ❤️

### How do you set boundaries between work vs. personal writing?

Given my role in big tech, I intentionally steer clear of writing directly about my day-to-day work, despite how meaningful the work is and how useful the sharing would be. Instead, I focus my writing on broader concepts and design patterns. When I do want to discuss the details, I rely on publicly available sources like papers and technical articles. Thus, my employer only comes up in my writing through references that are already public.

### Have you written anything else on the topic of writing?

- [What I Did Not Learn About Writing In School](https://eugeneyan.com/writing/what-i-did-not-learn-about-writing-in-school/)
- [What I Learned from Writing Online - For Fellow Non-Writers](https://eugeneyan.com/writing/what-i-learned-from-writing-online/)
- [How to Write Better with The Why, What, How Framework](https://eugeneyan.com/writing/writing-docs-why-what-how/)
- [How to Write Design Docs for Machine Learning Systems](https://eugeneyan.com/writing/ml-design-docs/)
- [Seemingly Paradoxical Rules of Writing](https://eugeneyan.com/writing/paradox/)

If you found this useful, please cite this write-up as:

> 
> 
> 
> Yan, Ziyou. (Mar 2025). Frequently Asked Questions about My Writing Process. eugeneyan.com. https://eugeneyan.com/writing/writing-faq/.
> 

or

```
@article{yan2025writingfaq,
  title   = {Frequently Asked Questions about My Writing Process},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2025},
  month   = {Mar},
  url     = {https://eugeneyan.com/writing/writing-faq/}
}
```

Share on: