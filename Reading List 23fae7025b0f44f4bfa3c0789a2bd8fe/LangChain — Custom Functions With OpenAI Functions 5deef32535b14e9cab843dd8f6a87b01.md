# LangChain — Custom Functions With OpenAI Functions | by Prince Krampah | Medium

Column: https://medium.com/@princekrampah/langchain-custom-functions-with-openai-functions-90e2deefd707
Processed: No
created on: April 4, 2024 10:12 PM

# LangChain — Custom Functions With OpenAI Functions

![](https://miro.medium.com/v2/resize:fill:88:88/1*K0tJZ-nblOhECZsmmoTuUw.jpeg)

[Prince Krampah](https://medium.com/@princekrampah?source=post_page-----90e2deefd707--------------------------------)

·

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F43f5ed8aa6e0&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40princekrampah%2Flangchain-custom-functions-with-openai-functions-90e2deefd707&user=Prince+Krampah&userId=43f5ed8aa6e0&source=post_page-43f5ed8aa6e0----90e2deefd707---------------------post_header-----------)

2 min read

·

Jul 25, 2023

In the last articel, we have gone over how to use OpenAI function agents. In this article, we’ll go over how to create custom functions with OpenAI functions. In this article we’ll build a custom function that returns my personal profile info.

![](https://miro.medium.com/v2/resize:fit:700/1*GaGkcbs5ZqE53UtZnUjgyQ.png)

This article builds on all the previous articles, we have gone over in the last posts. You can checkout those articles.

## Custom Function

This function will be used to return John’s profile, one attribute at a time.

```
def my_profile(att: str):
    """Function to return an aspect of my profile"""
    profile_details: dict = {
        "first_name": "John",
        "second_name": "Doe",
        "email": "john@doe.com",
        "age": 34,
        "residence": "Nairobi",
        "street": "Street xyz"
    }

    return my_profile.get(att)
```

**Testing it out**

```
print(my_profile("first_name"))
```

That works fine.

## Building The Custom Tool

Let’s go ahead and build a simple tool using the custom function we just wrote.

```
from typing import Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool
# import for agent creation
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from decouple import config

def my_profile(att: str):
    """Function to return an aspect of my profile"""
    profile_details: dict = {
        "first_name": "John",
        "second_name": "Doe",
        "email": "john@doe.com",
        "age": 34,
        "residence": "Nairobi",
        "street": "Street xyz"
    }

    return profile_details.get(att)

class MyProfileInput(BaseModel):
    """Inputs for my_profile function"""
    attribute: str = Field(description="Attribute of profile detail")

class MyProfileTool(BaseTool):
    name = "my_profile"
    description = """
        Useful when you want to get profile details of John Doe.
        You should enter the attribute of the profile information you want
        """
    args_schema: Type[BaseModel] = MyProfileInput

    def _run(self, attribute: str):
        profile_detail_attribute = my_profile(attribute)
        return profile_detail_attribute

    def _arun(self, attribute: str):
        raise NotImplementedError(
            "my_profile does not support async calls")

llm = ChatOpenAI(
    temperature=0, model="gpt-3.5-turbo-0613",
    openai_api_key=config("OPANAI_API_KEY")
)

tools = [
    MyProfileTool()
]

agent = initialize_agent(
    tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True)

agent.run("What is the age of John?")T
```

That works fine, now let’s try a couple more questions to the agent.

```
agent.run("Where does John Doe reside")
```

Code Output

![](https://miro.medium.com/v2/resize:fit:700/1*vzjN5QEW75UdOFCWHWWOqg.png)

## Conclusion

Congratulations for making it this far!! hope you find this helpful. In the next post I’ll be going over MRKL systems(pronouced “Miracle” Systems).

If you enjoyed this post and want more of such content in video format, you can follow me on [YouTube @codewithprince](https://www.youtube.com/@CodeWithPrince/featured) for video content as well.

Happy coding, cheers!!!