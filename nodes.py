# src/nodes.py

from typing import Dict

def user_input_node(state: Dict) -> Dict:
    topic = state.get("topic", "No topic provided")
    response = f"My opinion on '{topic}' is that it's a nuanced issue with multiple sides."
    return {"user_input": response}

def agent_node(state: Dict) -> Dict:
    user_input = state.get("user_input", "")
    response = f"As an AI debater, I counter: '{user_input}'. But I acknowledge some valid points."
    return {"agent_response": response}

def judge_node(state: Dict) -> Dict:
    user_input = state.get("user_input", "")
    agent_response = state.get("agent_response", "")

    if len(user_input) > len(agent_response):
        winner = "User"
    elif len(agent_response) > len(user_input):
        winner = "Agent"
    else:
        winner = "Draw"

    return {
        "winner": winner,
        "user_input": user_input,
        "agent_response": agent_response
    }
