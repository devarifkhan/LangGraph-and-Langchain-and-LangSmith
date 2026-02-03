from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool, render_text_description
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import BaseOutputParser
from langchain_core.agents import AgentAction, AgentFinish
from typing import Union
import re


load_dotenv()

class ReActSingleInputOutputParser(BaseOutputParser):
    """Parser for ReAct-style agent output."""

    def parse(self, text: str) -> Union[AgentAction, AgentFinish]:
        # Check if this is a final answer
        if "Final Answer:" in text:
            return AgentFinish(
                return_values={"output": text.split("Final Answer:")[-1].strip()},
                log=text,
            )

        # Extract action and action input
        action_match = re.search(r"Action:\s*(.*?)(?:\n|$)", text, re.DOTALL)
        action_input_match = re.search(r"Action Input:\s*(.*?)(?:\n|$)", text, re.DOTALL)

        if action_match and action_input_match:
            action = action_match.group(1).strip()
            action_input = action_input_match.group(1).strip()

            return AgentAction(
                tool=action,
                tool_input=action_input,
                log=text,
            )

        # If we can't parse the output, return it as is
        return AgentFinish(
            return_values={"output": text},
            log=text,
        )

@tool
def get_text_length(text:str)->int:
    ''' Returns the length of text by characters '''
    return len(text)

if __name__ == "__main__":
    print("Hello React Langchain!")
    tools = [get_text_length]

    template ="""
    Answer the following questions as best you can. You have access to the following tools:

    {tools}

    Use the following format:
    
    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question
    
    Begin!
    
    Question: {input}
    Thought:
    """

    prompt = PromptTemplate.from_template(template=template).partial(tools=render_text_description(tools),tool_names=", ".join(t.name for t in tools))
    llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-2.5-flash")
    agent = {"input" :lambda x:x["input"] } | prompt | llm | ReActSingleInputOutputParser()

    res = agent.invoke({"input":"what is the text length of 'DOG' in characters?"})
    print(res)