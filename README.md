# AI Planning & Scheduling Assistant (MVP)

## Goal
Convert unstructured to-do lists into realistic, time-bound, executable schedules.

## MVP Capabilities
- Task decomposition
- Conservative time estimation
- Priority reasoning
- Daily schedule generation
- Risk & overload detection
- Re-planning support

## Architecture
- Rule-based scheduling
- LLM only for reasoning & decomposition
- Stateless API design

## Structure
- src/core → parsing & estimation
- src/planner → priority logic
- src/scheduler → schedule generation
- api → API layer
- tests → validation & edge cases

## Status
🚧 MVP scaffold complete
