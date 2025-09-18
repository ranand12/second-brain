# Build a Gemini Full-Stack Research Agent with Agent Development Kit | by Debi Cabrera - Googler | Google Cloud - Community | Sep, 2025 | Medium

Column: https://medium.com/google-cloud/build-a-gemini-full-stack-research-agent-with-agent-development-kit-11192e8e9165
Processed: Yes
created on: September 17, 2025 6:37 PM

# **Build a Gemini Full-Stack Research Agent with Agent Development Kit**

[Debi Cabrera - Googler](https://miro.medium.com/v2/da:true/resize:fill:32:32/0*u1ZOA68tifqee4mo)

[Debi Cabrera - Googler](https://medium.com/@debicabrera?source=post_page---byline--11192e8e9165---------------------------------------)

9 min read

·

7 hours ago

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*rY5m_1Y_ucf_Q8TsNJgj2Q.png)

Have questions/comments about this? I’m posting this in [r/googlecloud](https://www.reddit.com/r/googlecloud/) (same title)— so ask away and I’ll do my best to answer them!

Do you ever research stuff? This Full-stack team of highly specialized agents can seriously decrease your research time. It takes your request about a specific research topic, for example “a report on the life and teachings of Thich Nhat Hanh”, and turns it into a comprehensive, well researched, and cited report.

It’s rocking a React frontend and an ADK-powered FastAPI backend, with deployment options for Google Cloud Run and Vertex AI Agent Engine. Oh and it’s all done with a backend that is less than 400 lines of code 😮

Agent Development Kit is an open-source framework from Google designed to simplify the full stack end-to-end development of agents and multi-agent systems. ADK makes it easier for developers like you to build production-ready agentic applications with greater flexibility and precise control.

Need a crash course in ADK? Check out this [codelab](https://codelabs.developers.google.com/onramp/instructions#0?utm_campaign=CDR_0x347ce846_user-journey&utm_medium=external&utm_source=blog) to go from beginner to expert.

This architecture clearly shows the flow of agents and sub-agents in our full-stack research agent. There are also sub-agents of sub-agents, so keep referring to the visual if it’s all becoming convoluted.

First, I’ll take you through each piece and then I’ll show you how it all comes together in action.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*Q5rsPZ0DhIW1ClKjLKL3Vg.png)

**Phase 1, “Plan and Refine”** involves a human in the loop. The **Root agent —** the agent that gets invoked first in the interaction with the user — aka the **Interactive Planner**, collaborates directly with the user to create and refine a research plan. That’s it, it does not conduct any research itself. It takes the initial topic, uses the **Plan Generator** to create a draft, presents it to the user for feedback, and once approved, delegates the entire plan to the research pipeline.

The **Plan Generator** is an **agent tool** used by the Interactive Planner. (we’ll get to what that is in a second) It considers what needs to be researched and what needs to be delivered, generating a bulleted list of goals, tagging each one as either “[RESEARCH]” for something to look up or “[DELIVERABLE]” for something to create, like a table or summary, with a few more tags for context. These tags are then used by downstream agents.

So, what is an Agent Tool? The [AgentTool](https://google.github.io/adk-docs/agents/multi-agents/#c-explicit-invocation-agenttool) class is a special wrapper that allows you to treat an entire agent as a single tool. You can create a specialized agent and then ‘package’ it as a tool for another base agent to use, in this case the Interactive Planner. This allows your architecture to remain organized and lets agents hand off jobs to each other, so complex tasks can be completed smoothly.

It’s included as an import in agent.py

```
from google.adk.tools.agent_tool import AgentTool
```

The Plan Generator agent is defined

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*F6KUS8m9TwgLUpoTOSlvPQ.png)

Then it’s provided as a tool in the root agent definition with the AgentTool wrapper. Preety cool! Yes, **preety,** cool.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*jFT0AIdhVhB_CPa_zqkNvw.png)

And that is a nice segway into Phase 2 — because the first sub-agent is also defined there in the root agent — the Research Pipeline Agent (if you’re a visual person like me, it might help to scroll back up to that architecture right aboot now)

**Phase 2: Execute Autonomous Research**. The sub-agent, called the **Research Pipeline**, functions as an Autonomous Research Department. This [SequentialAgent](https://google.github.io/adk-docs/agents/workflow-agents/sequential-agents/) takes the approved plan and executes it from start to finish without further human intervention, serving as the engine room of the entire operation. It contains several sub-agents that run in order.

Its first sub-agent, **Section Planner**, acts as an Architect, taking the approved plan and designing the structure of the final report, creating a markdown outline such as an introduction or key announcements. The next sub-agent, **Section Researcher**, is the initial researcher. It goes through all the “[RESEARCH]” tasks in the plan, runs multiple web searches for each, and synthesizes the results, also tracking every source it consults for citations.

Once the initial research is done the sequence boops into the **Iterative Refinement Loop** (basically quality assurance), which is a [LoopAgent](https://google.github.io/adk-docs/agents/workflow-agents/loop-agents/). A loop agent will repeatedly execute its sub-agents for a set number of iterations or, as it is in this case, until a specific termination condition is met. This loop agent ensures that the research conducted is high quality and meets desired standards, looping until it receives a passing grade. (the termination condition)

Inside the loop agent we have three sub-agents.

First, the **Research Evaluator,** which critically evaluates the initial research findings and assigns a grade of “pass” or “fail.” If it fails, it provides detailed feedback and a list of follow-up search queries.

Second, **Escalation Checker**, it’s a simple custom agent for loop control that verifies the grade from the critic. If the grade is a “pass,” the loop stops. This agent **does not** assign the pass/fail grade; it only checks the assigned grade to continue or stop the loop. If the loop continues due to a “fail” grade, our third sub-agent comes into play.

**Enhanced Search Executor**, runs the follow-up queries and integrates new findings to improve the research and the loop continues until the “pass” grade is achieved.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*o_PsbIGGBI0-b4kIGROWXg.png)

Once the loop stops, it goes to our final agent, the **Report Composer**, aka the Author. At this point, we know the research is fire and ready to be put into a report. 🔥This agent takes all the verified findings, the report outline, and the list of sources to write a polished report, complete with citations.

Let’s see this agent in action. I’m going to run it in a local environment using an [API key from Google AI Studio](https://aistudio.google.com/app/apikey) to test it out. (these steps are all in the readme 🙂)

Make sure you have Python 3.10+, Node and [uv](https://github.com/astral-sh/uv) installed.

First I can ask my request to my Interactive Planner (root agent):

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*zvrOsn_vp8nfZem8etffjw.png)

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*Z77LTKumZ7Vxy7_yH8szqw.png)

It called the Plan Generator AgentTool to put together a plan with tags. At this point, the human is still in the loop and you can decide if you like the plan or want to make any edits. I dig the plan, and tell the agent “looks good!”, so that it knows to move forward.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*sFvGrA_rYMVpnpQThtCG5Q.png)

This is the output. Hmm, but Debi, what is this transfer_to_agent function? I don’t see it defined in the /app/agent.py. Ah yes! Fabulous observation reader. 🔬

## Get Debi Cabrera - Googler’s stories in your inbox

Join Medium for free to get updates from this writer.

This is because transfer_to_agent **is not a function you write;** it’s a fundamental action built into the ADK framework itself. It’s the mechanism ADK uses when one agent needs to delegate a task to another agent.

The instructions for the Interactive Planner (Root agent) say:

```
**Execute:** Once the user gives EXPLICIT approval (e.g., "looks good, run it"),
you MUST delegate the task to the `research_pipeline` agent, passing the approved plan.
```

That’s when the ADK framework takes over and says alright, pass it over to the other agent (whichever agent is specified as a sub_agent), in this case the Research Pipeline. This function is basically saying, “please, hold while I transfer your call.”

More info, if you wanna [get nerdy wid it](https://google.github.io/adk-docs/agents/multi-agents/#b-llm-driven-delegation-agent-transfer). Also, this is where it lives in our environment.

```
venv/lib/python3.9/site-packages/google/adk/tools/transfer_to_agent_tool.py
```

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*Jc8RTZ9neQfomwfxr8dsNw.png)

Ok, let’s get on with the autonomous party. Here we go.

Section Planner does its thing and creates a report outline.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*gOiWxXJIeNUf5kZAN6qXDA.png)

Then, Section Researcher takes over and goes wild with Google Search (tool) to gather some research.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*MqLt4gTXLv0rtqnXZh5NXg.png)

It goes all in, gathering research and taking in the tags from the previous agents to create the necessary [DELIVERABLE](s).

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*n0EES3DwSU8lr8N0xFoVqQ.png)

At the bottom of this, it lists out all the sources it used in the research — because who has time to make a bibliography these days?

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*2LEx2QtKn3pOPxjobN4RfQ.png)

This wonderful gift is because of instructions that specifically request it to do so after the agent finishes its turn, in what’s called an [after_agent_callback.](https://google.github.io/adk-docs/callbacks/types-of-callbacks/#after-agent-callback) These are functions that run at specific points in the workflow, they’re “useful for cleanup tasks, post-execution validation, logging the completion of an agent’s activity, modifying final state, or augmenting/replacing the agent’s final output.”

Every time a research agent (Section Researcher or Enhanced Search Executor) uses the google_search tool, a special function, **collect_research_sources_callback**, is triggered (by the after_agent_callback). This function’s job is to inspect the search results and save all the source URLs and their details into the session’s memory.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*8SakdyQPbkQUFAtkBvIh4g.png)

Press enter or click to view image in full sizeafter_agent_callback at the bottom here.

![](https://miro.medium.com/v2/resize:fit:700/1*zT4T6lAzsxnZGUQcVIBj2Q.png)

Next, the Research Evaluator gets the research and meticulously reviews everything to provide a grade of “pass” or “fail”. It passed, with flying colors! “The logical flow is impeccable” I mean, okay, slay queen 💅👑

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*ua5cZd_pjqGuK597waLn_g.png)

There’s no output but the Escalation Checker receives the “pass” grade and sends it over to the Report Composer for the final report.

The final agent, Report Composer, aka the “author,” is explicitly instructed to insert special citation placeholders in the form of (<cite source=”…”/>) to place citations within the text. This is done to avoid including the real, full URLs to avoid adding too much ‘stuff’ into the agent’s context window. It would increase latency, cost and drastically reduce the quality of the generated report.

Instead, all placeholders are replaced with the final citations using a python function — **citation_replacement_callback,** which is executed automatically after the Report Composer finishes its work to put in the final citations. The function is attached to the agent as another after_agent_callback and is responsible for replacing all the placeholders with the correct, full Markdown-formatted links using the source data collected earlier in the workflow. This ensures that the final report has accurate and clean citations without relying on the LLM for a simple find-and-replace task. You’ll see this in the final report.

This, by the way, is a great example of context engineering 😀(structuring and shaping the information provided to an LLM to improve the quality, accuracy, and predictability of its output for a specific task.)

**The Final Report:**

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*qYr_fkywo2pOgJjISFfHUg.png)

GLORIOUS! College me would have loved this help, instead I was up at 4am spending time looking for the research and THEN learning it.

This is a great example of how to build a FullStack multi-agent system quickly and efficiently!! Plus, If you have questions, or want to play with this yourself here is the [repo](https://github.com/google/adk-samples/tree/main/python/agents/gemini-fullstack).

If you want to do a hands-on lab that has similar features, like a multi-agent system with a loop agent, go [here](https://codelabs.developers.google.com/instavibe-adk-multi-agents/instructions#0?utm_campaign=CDR_0x347ce846_user-journey&utm_medium=external&utm_source=blog)!

Reminder, that this is posted in [r/googlecloud](https://medium.com/www.reddit.com/r/googlecloud/), so if you have questions/comments I’ll be on the lookout for a few weeks to see if I can answer them and probably learn a lot from you all 🥹

Peace, love, cheese. ✌️❤️🧀