from typing import Dict,Any,List
from uuid import UUID

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.outputs import LLMResult

class AgentCallbackHandler(BaseCallbackHandler):
    def on_llm_start(self,serialized:Dict[str,Any],prompts:List[str],**kwargs:Any)->Any:
        """ Run when LLM starts running. """
        print(f"***Prompt to LLM was:***\n{prompts[0]}")
        print("*****")

    def on_llm_end(
        self,
        response: LLMResult,
        *,
        run_id: UUID,
        parent_run_id: UUID | None = None,
        tags: list[str] | None = None,
        **kwargs: Any,
    ) -> Any:
        """ Run when LLM ends running """
        print(f"***LLM Response:***\n{response.generations[0][0].text}")
        print("*****")