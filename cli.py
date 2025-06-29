# src/cli.py

from src.dag import build_debate_dag

def run_cli():
    dag = build_debate_dag()
    initial_state = {
        "topic": "Is AI dangerous?",
        "agent_2_output": "I believe AI is beneficial if used responsibly."
    }

    result = dag.invoke(initial_state)

    print("\n--- Debate Results ---")
    print("Agent 1 said:", result.get("agent_1_output"))
    print("Agent 2 said:", result.get("agent_2_output"))
    print("Winner:", result.get("winner"))
