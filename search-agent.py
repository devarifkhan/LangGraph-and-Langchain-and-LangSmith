from typing import Any

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient()


@tool
def search(query: str) -> dict[str, Any]:
    """ Tool that searches over the internet
    Args:
        query (str): The query is searching for
    Returns: str: The search result
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
)

tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain agent")

    result = agent.invoke(
        {
            "messages": [
                HumanMessage(content="what is the weather of dhaka?")
            ]
        }
    )
    print("Agent result:", result)



if __name__ == "__main__":
    main()
