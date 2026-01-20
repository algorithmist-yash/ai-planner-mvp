# 🗓️ AI Planning & Scheduling Assistant (MVP)

A **risk-aware, time-bound AI planning system** that converts unstructured to-do lists into **realistic, executable daily plans**.

This project focuses on **execution over optimism**:
- No overbooking
- Conservative time estimates
- Transparent risk flags
- Deterministic, explainable logic

Built as a **product-grade MVP**, not a demo toy.

---

## 🚀 Key Capabilities

### 🧠 Task Intelligence
- Accepts unstructured to-do lists
- Detects ambiguous tasks
- Breaks tasks into atomic units
- Conservative time estimation with buffers

### ⚖️ Priority Reasoning
- Rule-based, deterministic priority scoring
- Deadline-aware urgency detection
- Ambiguity penalties for transparency
- Explainable priority reasons

### ⏰ Realistic Scheduling
- Time-blocked daily planning
- Respects available time strictly
- 15% buffer to prevent overload
- Never hides impossible schedules

### ⚠️ Risk Awareness
- Flags overloads explicitly
- Detects tight deadlines
- Highlights vague / ambiguous tasks
- Fail-safe behavior by design

### 🔁 Re-Planning Support
- Preserves completed work
- Re-optimizes remaining tasks
- Stateless, safe re-execution

---

## 🖥️ Product Interfaces

### 1️⃣ FastAPI Backend
- Single endpoint: `POST /plan`
- Stateless, API-first design
- Clean JSON input/output
- Swagger UI enabled

### 2️⃣ Professional Planner UI (Streamlit)
- Task inbox
- Priority-tagged to-do list
- Time-blocked daily schedule
- Clock-based planner feel
- Risk & next-action panels

### 3️⃣ Dockerized Deployment
- One-command startup
- No local Python or venv required
- UI + API orchestrated together

---

## 📦 Project Structure

ai-planner-mvp/
├── api/
│ ├── app.py # FastAPI app
│ └── schemas.py # API request/response models
│
├── src/
│ ├── core/ # Task parsing & schemas
│ ├── planner/ # Priority, risk, replanning logic
│ ├── scheduler/ # Time-block scheduling engine
│ └── utils/ # Validators & output formatting
│
├── ui.py # Streamlit planner UI
├── Dockerfile
├── docker-compose.yml
├── requirements.prod.txt
├── README.md
└── .gitignore

yaml
Copy code

---

## 🔌 API Usage

### Endpoint
POST /plan

css
Copy code

### Example Request
```json
{
  "tasks": [
    { "text": "Study AI" },
    { "text": "Prepare exam", "deadline": "2026-01-20" }
  ],
  "available_minutes": 180,
  "day": "Today"
}
Response Structure
Task Breakdown

Priority Table

Schedule Plan

Risk Flags

Next Actions

All fields are explicit and deterministic.

🧪 Local Development (Without Docker)
1️⃣ Activate environment
bash
Copy code
source venv/bin/activate
2️⃣ Run API
bash
Copy code
uvicorn api.app:app --reload
3️⃣ Run UI
bash
Copy code
streamlit run ui.py
UI → http://localhost:8501

API Docs → http://localhost:8000/docs

🐳 Run with Docker (Recommended)
One Command
bash
Copy code
docker compose up --build
Access
UI → http://localhost:8501

API Docs → http://localhost:8000/docs

To stop:

bash
Copy code
docker compose down
🛡️ Design Principles
Deterministic over creative

Rule-based where possible

LLM optional, never required

No hidden assumptions

Fail loudly, not silently

Execution > aesthetics > theory

🎯 Target User
A single power user managing complex goals:

Study

Work

Learning

Fitness

Long-term planning

Built to prevent burnout, not cause it.

🧠 Current Status
✅ Core MVP complete
✅ API + UI integrated
✅ Dockerized deployment
✅ Clean GitHub repository

🔜 Possible Next Extensions
Weekly & multi-day planning

Calendar export (Google / iCal)

LLM-assisted task decomposition

Persistence (SQLite / Postgres)

Multi-user support

Testing & benchmarking suite

👤 Author
Yash Raj
AI Systems Engineer | Planner Systems | Agentic AI

GitHub: https://github.com/algorithmist-yash

Focus Areas: AI systems, productivity engineering, intelligent agents

This project was designed and implemented end-to-end with a product-first, execution-focused mindset, emphasizing real-world constraints and engineering rigor.
