# Test Prompts — Fitness Coaching Team

Use these prompts to demo routing, tools, and each specialist.

## How to start

```powershell
cd "c:\Users\P1359064\OneDrive - NCS PTE LTD\NucleusMaterials_ChangXin\NUS-ISS\12 Architecting Agentic AI Solutions\Day 4\workshop-3"

$env:UV_LINK_MODE="copy"
uv sync
uv run python main.py
```

On first run, enter your profile or press Enter for defaults.

## How to stop

| Action | What happens |
|--------|----------------|
| Type `exit` and press Enter | Graceful end — generates session summary |
| Press `Ctrl+C` | Immediate quit (no summary) |
| Close the terminal window | Stops the app |

To start again, run `uv run python main.py`.

## Reading the output

Every turn shows two layers:

1. **Backend trace** (always on) — routing and tool calls  
   `[ROUTE] Head Coach  Routing to specialist (Alex)`  
   `[TRAIN] Alex  Auto-calling tool (log_workout: ...)`

2. **Coach card** — short bullet response from the specialist

**Note:** Logs reset at each app start (profile is kept). Tools auto-run when you say `Log workout:`, `Log meal:`, `Log sleep:`, or `How am I doing?`

Set `DEBUG=true` in `.env` for full LLM thought/action logs.

---

## Training (Alex)

```
Plan a 4-day program for my goal. I have dumbbells and a barbell only.
```

```
I have a knee injury from running. What leg exercises are safe?
```

```
Log workout: goblet squats 3x10, DB rows 3x12, plank 3x45s
```

```
What is good form for a deadlift?
```

Expected: routes to **Alex**, may call `exercise_lookup` or `log_workout`.

---

## Nutrition (Sam)

```
I ate McDonald's for lunch. Log it and tell me how to balance the rest of my day.
```

```
How much protein should I eat to build muscle?
```

```
Log meal: dinner grilled chicken, rice, broccoli
```

```
I drink only 2 glasses of water a day. Is that enough?
```

Expected: routes to **Sam**, may call `log_meal` or `progress`.

---

## Recovery (Jordan)

```
I slept 5 hours last night and feel exhausted.
```

```
Log sleep: 6 hours, poor quality
```

```
My knees are sore after yesterday's workout. Should I train today?
```

```
I'm stressed from work and skipping rest days.
```

Expected: routes to **Jordan**, may call `log_sleep` or `progress`.

---

## Progress check (any specialist)

```
How am I doing this week?
```

Expected: specialist calls `progress` tool, then gives a short summary.

---

## Multi-topic conversation (full demo script)

Run these in order for a good demo log:

1. `Plan a program to reach my fitness goal. I sleep 6 hours, female, 26, desk job.`
2. `I have dumbbells and barbells, knee injury from running, and I eat fast food often.`
3. `Log meal: lunch fast food burger and fries`
4. `Log workout: upper body DB press 3x10, rows 3x12`
5. `Log sleep: 6 hours, fair`
6. `How am I doing?`
7. `exit`

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| No API response | Check `OPENAI_API_KEY` in `.env` |
| `uv sync` fails on OneDrive | Run `$env:UV_LINK_MODE="copy"` first |
| Responses still long | Re-run — prompts now cap at ~60 words |
| Wrong coach answers | Backend trace shows routing; rephrase to focus one topic |
