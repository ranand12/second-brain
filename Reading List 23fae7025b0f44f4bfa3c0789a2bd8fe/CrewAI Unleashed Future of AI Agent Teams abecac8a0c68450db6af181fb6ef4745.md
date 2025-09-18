# CrewAI Unleashed: Future of AI Agent Teams

Column: https://blog.langchain.dev/crewai-unleashed-future-of-ai-agent-teams/
Processed: No
created on: April 4, 2024 10:15 PM

![](https://blog.langchain.dev/content/images/size/w1520/format/webp/2023/12/HighLevelChart_noBG.png)

**Editor's Note: this blog is from Joao Moura, maintainer of CrewAI. CrewAI is a multi-agent framework built on top of LangChain, and we're incredibly excited to highlight this cutting edge work.**

## AI Agents Crews are game-changing

AI agents are emerging as game-changers, quickly becoming partners in problem-solving, creativity, and innovation and that's where [CrewAI](https://github.com/joaomdmoura/crewai?ref=blog.langchain.dev) comes in.

Imagine turning a single line of thought into a comprehensive landing page in just minutes. It's a reality we're creating today with CrewAI.

Recently, [I demonstrated this in a tweet](https://x.com/joaomdmoura/status/1731064418136400139?s=20&ref=blog.langchain.dev), using CrewAI's and [LangChain](https://www.langchain.com/?ref=blog.langchain.dev) with OpenHermes2.5, powered by [Ollama](https://ollama.ai/?ref=blog.langchain.dev), transforming a one-liner into a complete landing page. The result was a revelation of the untapped potential in AI collaboration and the ability to early market test ideas faster than ever before, and that is only one use case ([play with the code in Replit](https://replit.com/@crewAI?ref=blog.langchain.dev)).

CrewAI's vision is clear, to allow engineers to harness the collective power of AI agents, moving beyond traditional automation, by bringing Agents together and allowing for streamlined decision-making, enhanced creativity, and solving complex challenges.

## Simplicity through Modular Design

CrewAI champions a principle that resonates with every engineer: simplicity through modularity. This means it's like a set of building blocks (much like LangChain).

CrewAI’s main components:

- **Agents:** These are like your dedicated team members, each with their role, background story, goal and memory
- **Tools:** The equipment our agents use to perform their tasks efficiently, you can use any existing ones from LangChain or quickly write your own
- **Tasks:** Small and focused mission a given Agent should accomplish
- **Process:** This is the workflow or strategy the crew follows to complete tasks.
- **Crew:** Where Agents, Tasks and a Process meet, this is the container layer where the work happens

We believe in the power of simplicity to unlock complexity. By breaking down the intricate world of Agents into these modular components, we make it approachable, manageable, and fun to work with.

[](https://lh7-us.googleusercontent.com/vqFaRak07ETDUvxfqlkK5LFU0u65GaLwqdkxG_nBjyBdq8LhUEX9fYJdv2zLBQnutHEBukd6vm3LUgCZEL1KeYYASfNgiRucueED4YeRvAS1Yki5VyruYTdGeWoBK_sbmTleuK0zXLGYTunjC2kXMFo)

While individual tasks are important, CrewAI truly excels when multiple agents come together to form a crew. It’s in teamwork – agents collaborating, sharing goals, and following a process to achieve a common objective – where you go from average results to very impressive ones!

One example of collaboration within CrewAI is delegation, thanks to it, agents can ask for assistance or allocate portions of their task to others, much like we do in our workplaces. This ability for spontaneous collaboration is one example of what sets this library apart.

I designed CrewAI for practical, real-world use. And we strive to make it a library you can integrate into your applications and use it almost as easily as you would call a function.

## Building with CrewAI

***Disclaimer:** The full code examples are available at [Replit as templates](https://replit.com/@crewAI?ref=blog.langchain.dev) you can customize and run in the cloud yourself but also at Github.*

Let's explore the idea of a crew that can build a landing page from a single-line idea. The best way to go about a new crew is to first map out what would the process you, as a human, would go through to do this yourself, and then we can translate that into a crew.

My need for landing pages came from the fact I want to quickly experiment with ideas and see if they have any traction, so I want to be able to quickly build a landing page and gauge people’s interest on it, so that only then I can spend more time on it. More than a landing page I really need to do a good job at communicating the product or service I'm offering to make sure it's compelling.

So this is what I would do as a human:

1. Start by writing a single line idea, something like "A healthy snack for dogs to lose weight".
2. Expand that with some research, understand the market and why this is a good idea.
3. Find the appropriate template for this idea's landing page.
4. Write the copy for the landing page.
5. Build the landing page using the appropriate template and copy.

So if I had to put together a team for this what would be the ideal hires I would make?

- **Senior idea analyst** to understand and expand upon the essence of ideas, make sure they are great and focus on real pain points.
- **Senior communications strategist** to craft compelling stories to captivate and engage people around an idea.
- **Senior react engineer** to build an intuitive, aesthetically pleasing, and high-converting landing page.
- **Senior content editor** to ensure the landing page content is clear, concise, and captivating.

Now that we have our crew, let's see how we can translate part of it into an initial CrewAI crew that can expand our one-liner into a fully fledged researched idea *(full code at [Replit](https://replit.com/@crewAI?ref=blog.langchain.dev) and Github).*

For that you’ll need to create each agent you wanna use, create the tasks you want them to perform and then put them together in a Crew.

```
# ... early imports, tools, setting OpenAI API key, etc
from crewai import Agent, Task, Crew

## Create Agents with goal, role, backstory and tools
idea_analyst = Agent(
 role="Senior Idea Analyst",
 goal= "Understand and expand upon the essence of ideas... [rest of it]",
 background_story="You're recognized as a thought leader... [rest of it]",
 verbose=True,
 tools=[
   SearchTools.search_internet,
   BrowserTools.scrape_and_summarize_website
 ]
)
# communications_strategist = Agent(...) another agent

## Create the tasks that will produce a fully formed idea proposal
expand_idea_task = Task(
 description="THIS IS A GREAT IDEA! Analyze it and conduct... [rest of description]",
 agent=idea_analyst
)
# refine_idea_task = Task(...) another task

## Create the crew that will produce a fully formed idea proposal
crew = Crew(
 agents=[idea_analyst, communications_strategist],
 tasks=[expand_idea_task, refine_idea_task],
 verbose=True
)

final_improved_idea = crew.kickoff() # returns the final idea proposal

```

## Make it Custom

The example we just explored is one of the most basic setups in CrewAI, and look how powerful it is! But that's just scratching the surface. Imagine the possibilities when you start customizing things (I’ll link to some fully working examples later in the post)

Think about mixing and matching different AI brains (LLMs) in your crew. Some might be based in the cloud, others right on your computer, up to you. And what if you have a unique challenge? No problem, you can always have a fine tuned model to be the brain of one of an Agent. What about integrations with external systems? You can craft your own tools or tap into the [vast tools that LangChain offers](https://python.langchain.com/docs/integrations/tools?ref=blog.langchain.dev), like in this example bellow:

```
# !pip install yfinance

from langchain.chat_models import ChatOpenAI
from langchain.llms import Ollama
from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool

from crewai import Agent, Task, Crew

stock_analyst = Agent(
 role="Senior Stock Analyst",
 goal= "Report on stocks and analysis with suggestions ...",
 background_story="You're recognized as a major trader...",
 llm = Ollama(model="openhermes2.5-mistral") # Using local model with Ollama
 tools=[ YahooFinanceNewsTool() ], # Using a LangChain tool
 verbose=True,
)

#  Create Other Agents, Tasks and Crew
```

***Disclaimer:** A little heads-up for those diving into local models: they can be a bit tricky right out of the box, especially the smaller ones. To get the best out of them, you might need to tweak a few settings. You should add 'Observation' as a stop word, and play around with parameters like 'top_p', 'repeat_last_n', and 'temperature' to get it working as you need. These little adjustments can make a world of difference in how your AI agents perform.*

## How it Works

Behind the scenes, each CrewAI Agent is essentially a LangChain Agent, but enhanced with a ReActSingleInputOutputParser. This parser is specially modified to better support role-playing, incorporates a binding stop word for contextual focus, and integrates a memory mechanism (using LangChain’s ConversationSummaryMemory) for continuity in tasks.

The fact that Agents are built on top of LangChain creates flywheel effects, the main one being that you get access to all LangChain [tools](https://python.langchain.com/docs/integrations/tools?ref=blog.langchain.dev) and [toolkits](https://python.langchain.com/docs/integrations/toolkits?ref=blog.langchain.dev) out of the box, and that alone already unlocks many use cases.

In the current iteration, Agents function autonomously, engaging in self-dialogue to determine the use of tools. Future versions of CrewAI, however, are planned to introduce diverse process types. These will enable collaborative executions in various group settings, allowing for dynamic task assignment among Agents during runtime

Tasks are assigned to Agents from their creation on the current version, and offer the ability to override the available tools that Agent will have at its disposal when performing work, this makes it easier to steer the same Agent in performing slightly different tasks while not overwhelming it with too many tools.

The Crew serves as a framework that encapsulates both Agents and Tasks, facilitating their sequential execution of work. In practice, you'll likely find it more effective to deploy multiple standalone Crews, each with a few Agents. This modular approach allows for diverse outcomes from each crew, as opposed to a singular, large Crew handling many tasks and Agents for a single output.

## Real Use Cases and Code

Other than building landing pages I’ve also been using Crews for many other cases, some of those are below with links for their Replit templates so you modify and try them yourself.

- [Assist in travel planning , finding places, messaging, schedule, costs.](https://replit.com/@crewAI/Trip-Planning-AI-Crew?v=1&ref=blog.langchain.dev)
- [Build a landing page from one-liner idea](https://replit.com/@crewAI/Idea-to-Landin-Page-AI-Crew?v=1&ref=blog.langchain.dev)
- [Individual Stock analysis *(disclaimer: not actual investment recommendation)*](https://replit.com/@crewAI/Stock-Analysis-AI-Crew-not-formal-stock-recommendation?v=1&ref=blog.langchain.dev)

## Future

Currently, CrewAI champions the 'sequential' process. Think of it as a relay race where each agent completes their part and then hands off their work to the next one. It's straightforward yet effective.

But this is not taking full advantage of all the different ways in which AI agents can work together, so we're not stopping there – we’re working on introducing more complex processes like 'consensual' and 'hierarchical' to unlock even more potential uses. We are super open for contributions [through both PRs and Issues in Github](https://github.com/joaomdmoura/CrewAI?ref=blog.langchain.dev), if you like it also [send me a post in X](https://twitter.com/joaomdmoura?ref=blog.langchain.dev) I’d love to hear more from people enjoying it!

## Summary

CrewAI represents a shift in AI agents by offering a thin framework that leverages collaboration and roleplaying, based on versatility and efficiency. It stands as a tool for engineers and creatives alike, enabling the seamless assembly of AI agents into cohesive, high-performing teams.

Whether it's transforming a single thought into a fully-fledged landing page or conducting complex idea analysis, CrewAI is adept at handling a diverse range of tasks through its processes.

The real-world applications of CrewAI, from boosting social media presence to building interactive landing pages, underscore its practicality and adaptability. Looking forward, CrewAI is set to evolve further, introducing more intricate processes and continuing to redefine the landscape of AI teamwork. With its user-friendly integration and customization options, CrewAI is not just a concept but a tangible, powerful tool to harness the power of AI Agents.