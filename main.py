from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def search(query:str)->str:
    """
    Tool that searches over the internet
    Args:
        query (str): The query is searching for
    Returns:
        str: The search result
    """
    print(f"Searching for {query}")
    return "Dhaka weather is sunny"

def main():
    print("Hello from langchain agent")

if __name__ == "__main__":
    main()