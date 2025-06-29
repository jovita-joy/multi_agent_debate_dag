from langgraph.graph import StateGraph, END
from typing import TypedDict
from src.nodes import user_input_node, agent_node, judge_node

# Define the state schema
class DebateState(TypedDict, total=False):
    topic: str
    user_input: str
    agent_response: str
    winner: str

def build_debate_dag():
    sg = StateGraph(DebateState)  # ✅ Pass schema here

    sg.add_node("user_input", user_input_node)
    sg.add_node("agent", agent_node)
    sg.add_node("judge", judge_node)

    sg.set_entry_point("user_input")
    sg.add_edge("user_input", "agent")
    sg.add_edge("agent", "judge")
    sg.add_edge("judge", END)

    return sg.compile()
