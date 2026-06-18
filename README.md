# Fitness Coaching Team — Multi-Agent System

A LangGraph-based multi-agent fitness coach that plans training, tracks nutrition and sleep, and summarizes your session. Built for the NUS-ISS Agentic AI workshop assignment.

## Overview

This system simulates a **coaching team** with distinct specialist agents:

| Agent | Role | Tools (exclusive access) |
|-------|------|--------------------------|
| **Head Coach** (orchestrator) | Routes user messages to the right specialist | — |
| **Alex** (training planner) | Workouts, exercise form, training plans | `log_workout`, `exercise_lookup`, `progress` |
| **Sam** (nutrition advisor) | Meals, fueling, hydration | `log_meal`, `progress` |
| **Jordan** (recovery coach) | Sleep, rest, soreness | `log_sleep`, `progress` |
| **Summarizer** | End-of-session recap | `progress` (read-only via code) |

**Coordination:** LangGraph orchestrator pattern — user → Head Coach → specialist(s) → user loop, with conditional routing and shared state.

**State:** Conversation history, user profile, volley counter, and next agent selection flow through a shared `State` TypedDict.

**Persistence:** Workouts, meals, and sleep logs are stored in `data/user_data.json`.

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager
- OpenAI API key (`OPENAI_API_KEY`)

Recommended models (per assignment): `gpt-5-nano` or `gpt-5-mini` with `temperature=1`.

## Setup

1. Clone or unzip this project.

2. Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_key_here
DEBUG=true
```

- **Backend trace** (routing + tools) is always shown in the terminal.
- Set `DEBUG=true` for verbose raw LLM logs (thought/action iterations).

3. Install dependencies and run (OneDrive users: use copy mode):

```powershell
$env:UV_LINK_MODE="copy"
uv sync
uv run python main.py
```

## Start and stop

| Action | Result |
|--------|--------|
| `uv run python main.py` | Start the app |
| Type `exit` | End session with summary |
| `Ctrl+C` | Quit immediately (no summary) |

See `TEST_PROMPTS.md` for a full list of example prompts and a demo script.

## Usage

1. Enter your profile (or press Enter for defaults).
2. Type your question at the `>` prompt.
3. Watch the **backend trace** (who was routed, which tools ran).
4. Read the specialist's short bullet response.
5. Type `exit` to end the session and receive a summary.

### Example prompts

- `Plan a 4-day program. I have dumbbells and a barbell only.`
- `I had chicken rice for lunch — log it`
- `I only slept 5 hours and my knee hurts`
- `How am I doing this week?`

## Project structure

```
fitness-coach/
├── main.py              # Entry point, graph build, CLI
├── state.py             # Shared LangGraph state
├── nodes.py             # Graph nodes (human, specialist, summarizer)
├── display.py           # Terminal formatting and backend trace
├── utils.py             # Verbose DEBUG logging
├── agents/
│   ├── orchestrator.py  # Head Coach router
│   ├── specialist.py    # Training / nutrition / recovery agents
│   └── summarizer.py    # Session summary
├── tools/
│   ├── log_workout.py
│   ├── log_meal.py
│   ├── log_sleep.py
│   ├── get_progress.py
│   └── storage.py       # JSON persistence
└── data/                # Created at runtime (gitignored)
```

## Demo log

See `DEMO_LOG.txt` for a sample run highlighting agent routing, tool usage, and session summary.

## Assignment checklist

- [x] 3+ distinct agents with personas
- [x] Orchestrator coordination (Head Coach)
- [x] Tool integration with per-agent access control
- [x] Shared state and message history
- [x] LangGraph + OpenAI
