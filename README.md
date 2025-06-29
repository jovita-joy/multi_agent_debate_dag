# multi_agent_debate_dag
 Multi-Agent Debate DAG with LangGraph
This project simulates a structured debate between two AI agents using LangGraph, where each agent presents and rebuts arguments on a given topic. A judging node evaluates the debate and declares a winner.

## Features
LangGraph DAG architecture for modular, interpretable execution

Agent 1 gives an opening opinion on the topic

Agent 2 provides a counter-argument

Judge node decides the winner based on argument lengths

Easily extensible to support GPT-powered agents, multiple rounds, or complex judging logic

## How It Works
user_input_node – Takes a debate topic and produces an initial opinion.

agent_node – Reads Agent 1's opinion and provides a counter.

judge_node – Compares the two responses and declares a winner.

LangGraph manages the flow between nodes using a DAG (Directed Acyclic Graph).

## Setup Instructions
1. Clone the Repository
```sh
git clone https://github.com/your-username/multi_agent_debate_dag.git
cd multi_agent_debate_dag
```

2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate
# or venv\Scripts\activate  on Windows
```

3. Install Requirements
```sh
pip install langgraph
```

4. Run the Program
```sh
python run.py
```

## Future Improvements
🔁 Multi-turn debates (rebuttal rounds)

🧠 GPT-4 agents via OpenAI API

🎨 Web interface (Streamlit/Flask)

📊 Debate scoring logic beyond text length

📁 Logging debate history

OUTPUT

![Image](https://github.com/user-attachments/assets/9981573d-0170-48a2-a862-a19c89c4722d)


