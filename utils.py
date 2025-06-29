import json
from datetime import datetime

LOG_FILE = "logs/debate_log.json"

def summarize_debate(history):
    return "\n".join([f"[Round {h['round']}] {h['agent']}: {h['argument']}" for h in history])

def decide_winner(memory):
    scores = {agent: sum(len(arg.split()) for arg in args) for agent, args in memory.items()}
    winner = max(scores, key=scores.get)
    reason = f"{winner} presented more detailed and information-rich arguments."
    return winner, reason

def log_state(state, node):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "node": node,
        "state_snapshot": json.loads(json.dumps(state))
    }
    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []
    logs.append(entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)
