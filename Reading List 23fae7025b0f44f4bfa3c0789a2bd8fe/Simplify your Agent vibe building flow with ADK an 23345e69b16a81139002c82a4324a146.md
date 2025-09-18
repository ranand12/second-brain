# Simplify your Agent "vibe building" flow with ADK and Gemini CLI - Google Developers Blog

Column: https://developers.googleblog.com/en/simplify-agent-building-adk-gemini-cli/?trk=feed_main-feed-card_feed-article-content
Processed: Yes
created on: July 17, 2025 8:02 AM

![ADK + Gemini CLI: Supercharge Your Agent Building Vibe](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/adk-gemini-cli-agent-building-banner.original.png)

ADK + Gemini CLI: Supercharge Your Agent Building Vibe

For developers, the state of "flow" is sacred. It’s that magical space where your ideas translate into code almost effortlessly. The biggest enemy to this flow is friction— the reading of documentation, the framework selection, and the context-switching that pulls you out of the creative zone.

That's why we’re excited to announce updates to [Agent Development Kit](https://developers.googleblog.com/en/agent-development-kit-easy-to-build-multi-agent-applications/) (ADK) that, when paired with the [Gemini CLI](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/), are designed to eliminate friction and supercharge your agent "vibe coding" experience. This combination allows for all the right context in a seamless conversation between you and Gemini, turning your high-level ideas into functional agents with unprecedented speed and fluidity. This way, you can spend more time solving real-world problems using agents and far less time coding them from scratch.

The heart of this upgrade is the revamped [`llms-full.txt`](https://github.com/google/adk-python/blob/main/llms-full.txt) file included in the ADK repository. Think of this file as a perfectly organized, condensed guide to the entire ADK framework. It’s a map that details all the ADK’s components, functions, and best practices.

Specifically, we shortened the file by more than 50% (fewer tokens, yay!) and made it easier for LLMs to understand. This is the key to a better vibe coding experience because it means: **Gemini has a full understanding of ADK…without eating your context window or falling prey to “context rot”.**

So now paired with Gemini CLI, you have a powerful coding assistant that you’ve transformed into an ADK specialist at far lower cost and improved accuracy. CLI gains a deep, native understanding of the framework, enabling it to translate your high-level plans directly into accurate, idiomatic multi-agent code. This dramatically accelerates the speed-to-prototype; because you can generate a functional agent in minutes, you are free to experiment and iterate without a heavy upfront investment in coding time.

Let's see what this feels like in a real-world scenario. We'll build an AI agent to label ADK’s Github issues for easier issue prioritization and assignment, going from a simple idea to a working ADK agent in just a few steps.

Download the `llms-full.txt` from [adk-python](https://github.com/google/adk-python) to your working directory.

### **Step 1: Ideate the Plan with Gemini CLI**

First, we use the Gemini CLI as a brainstorming partner to create a high-level plan.

**You:** *I want to build an AI agent, leveraging the ADK framework, to help me label Github issues with Gemini in my repo (https://github.com/google/adk-python). It should read the Github issues and label it with some predefined labels* (please come up with some common labels first)*. Come up with a plan on how to do it. @llms-full.txt*

**Gemini CLI:**

**Plan: GitHub Issue Labeling Agent**

The goal is to create a Python-based AI agent that can analyze a GitHub issue and apply a relevant, predefined label from your repository. We'll use the ADK framework to orchestrate the agent's logic and a Gemini model for the analysis.

**Phase 1: Project Setup & Configuration**

1. **Initialize Project:** Set up a new Python project directory.

2. **Install Dependencies:** Install the `google-adk` library and a GitHub API client library like `PyGithub`.

3. **GitHub Authentication:** Create a GitHub Personal Access Token (PAT) with `repo` permissions to allow the agent to read issues and apply labels. This token will be configured securely as an environment variable.

**Phase 2: Develop Custom Tools for GitHub**

The agent needs tools to interact with GitHub. We will create a `github_tools.py` file containing the following functions, which will be exposed to the agent:

- `get_issue(repo_name, issue_number)`: Fetches the title and body of a specific GitHub issue.
- `get_available_labels(repo_name)`: Retrieves the list of all existing labels for the repository.
- `apply_label(repo_name, issue_number, label)`: Applies a given label to a specific issue.

**Phase 3: Build the Labeling Agent**

Using the ADK framework, we will define a new `Agent` in a `main.py` file:

1. **Agent Definition:** The agent will be configured to use a Gemini model (e.g., `gemini-1.5-flash`).

2. **Tool Integration:** The custom GitHub tools from Phase 2 will be provided to the agent.

3. **Core Instruction (Prompt):** The agent's system prompt will instruct it to follow a clear workflow:

- First, use the `get_issue` tool to understand the issue's content.
- Then, use the `get_available_labels` tool to see the valid options.
- Based on its analysis, decide on the single best label to apply.
- Finally, use the `apply_label` tool to add the chosen label to the issue.

**Phase 4: Create the Application Entrypoint**

We will create a simple command-line interface (CLI) in `main.py` that allows you to run the agent. It will accept the GitHub repository name and an issue number as input, and then trigger the agent to perform the labeling task.

Would you like me to proceed with the implementation of this plan?

You've defined the logic without writing a single line of code.

### **Step 2: Convert the Plan into an ADK Agent**

Now, let's use the ADK's `llms-full.txt` to turn that plan into a real agent.

**You:** *Great. Now, generate the code for this plan using the Python ADK. @llms-full.txt* (The Gemini CLI now references the ADK's `llms-full.txt` to translate the plan into correct ADK code.)

**Gemini CLI**

```
import argparse
import asyncio
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from github_tools import get_issue, get_available_labels, apply_label

labeling_agent = Agent(
    name="github_labeler",
    model="gemini-1.5-flash",
    instruction="""You are an AI agent that labels GitHub issues.
    1. First, use the 'get_issue' tool to read the issue's title and body.
    2. Then, use the 'get_available_labels' tool to see all possible labels for the repository.
    3. Analyze the issue content and choose the most relevant label from the available options.
    4. Finally, use the 'apply_label' tool to add the chosen label to the issue.
    5. Respond with a confirmation message stating which label was applied.
    """,
    tools=[get_issue, get_available_labels, apply_label],
)
```

```
from github import Github
from config import GITHUB_TOKEN

g = Github(GITHUB_TOKEN)

def get_issue(repo_name: str, issue_number: int) -> str:
    """Fetches the title and body of a specific GitHub issue."""
    repo = g.get_repo(repo_name)
    issue = repo.get_issue(number=issue_number)
    return f"Title: {issue.title}\nBody: {issue.body}"

def get_available_labels(repo_name: str) -> list[str]:
    """Retrieves the list of all existing labels for the repository."""
    repo = g.get_repo(repo_name)
    labels = [label.name for label in repo.get_labels()]
    return labels

def apply_label(repo_name: str, issue_number: int, label: str) -> str:
    """Applies a given label to a specific issue."""
    repo = g.get_repo(repo_name)
    issue = repo.get_issue(number=issue_number)
    issue.add_to_labels(label)
    return f"Successfully applied label '{label}' to issue #{issue_number}."
```

(It also generated requirements.txt, [label_config.py](http://config.py/) but we will not list it here for brevity.)

Instantly, you have a complete, functional agent application that correctly uses the ADK framework. The CLI handled all the boilerplate because the `llms-full.txt` file gave it the necessary context.

### **Step 3 & 4: Test and Improve in the Flow**

With the code generated, you can test it locally. Maybe you find a bug or think of an improvement. For example, you want a summary after the ADK agent completes the labels. You stay in your flow and simply ask for the change.

**You:** *Could you add a new label called “some_new_label” to the agent?*

The Gemini CLI, still holding the context of your script, refactors the code to implement the change. There's no need to manually edit the code or lose your momentum.

### **Step 5: Rinse and Repeat**

This iterative loop is the new workflow:

1: **Ideate** on your agent's logic.

2: **Generate** the ADK code with Gemini CLI.

3: **Test** it instantly.

4: **Improve** it with simple, conversational requests.

You can repeat this cycle until your agent is perfect, all without the friction that typically pulls you out of your creative zone.