from typing import TypedDict, Optional, Annotated
import operator


class State(TypedDict):
    """
    Shared state for the fitness coaching LangGraph workflow.
    """
    messages: Annotated[list, operator.add]
    volley_msg_left: int
    next_agent: Optional[str]
    user_profile: dict
