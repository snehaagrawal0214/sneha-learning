# Learning & Code Review — sneha-learning

**Reviewed:** 2026-06-27 (Day 0 of the plan)
**Against:** `~/Documents/prep-job-switch/sneha_job_switch_plan_v5.html` (MLE + DE Master Plan 2026–27)
**Reviewer:** Claude Code
**Scope:** All 27 files staged in the repo + project setup/hygiene

> This is a **living document**. Re-run the review (ask me to "update the learning review")
> at the end of each phase. The rubric and per-area checklists at the bottom are what each
> file gets graded against once it has real content.

---

## TL;DR (honest headline)

You are on **Day 0**. Today's date is the exact "Real Start: 27 Jun 2026" / "Tonight" date in
your plan. The repo is a **freshly created scaffold** — the folder structure is in place and
maps cleanly onto the plan, but **every learning file is an empty placeholder** (1–3 lines) and
the notebook is blank.

So there is genuinely **no code to assess for quality yet** — and I won't pretend otherwise.
What follows is:

1. A review of the **scaffold and setup** (the part that *does* exist), and
2. A **target spec + rubric** for each area so you know what "good" looks like before you write it.

This is the right state to be in on Day 0. The structure decision (folders mirroring the plan's
phases) is good and will pay off. The main risks are setup hygiene and the temptation to leave
files as stubs.

---

## What exists today

| Area | Files | State |
|------|-------|-------|
| `python-internals/` | memory_model, gil_demo, async_fetcher, decorators, generators | 5 placeholders |
| `dsa/` | arrays_hashing, sliding_window, trees | 3 placeholders |
| `leetcode/` | arrays/ (3), sliding_window/, trees/, graphs/, sql/ | 7 placeholders |
| `sql/` | window_functions, query_optimisation | 2 placeholders |
| `aws-glue/` | job_bookmark_demo, glue_vs_lambda_tradeoffs | 2 placeholders |
| `ml/` | sklearn_pipeline, mlflow_tracking, no_show_eda.ipynb | 3 placeholders (notebook empty) |
| `llm/` | bedrock_invoke, faiss_demo, prompt_patterns | 3 placeholders |
| `system-design/` | rag_system, healthcare_pipeline, feature_store | 3 placeholders |
| root | README.md | minimal but present |

**Verdict on structure:** Good. The taxonomy matches the plan's dual-track (DE / ML / LLM) and
the phase ordering. Nothing to reorganise.

---

## Setup & hygiene findings (fix these first — they're quick)

These are the only *actionable code-level* findings available today, and they matter because they
compound over 22 weeks.

### ✅ 1. Python upgraded to 3.12 (was 3.9.6) — RESOLVED 2026-06-27
The `.venv` was Python **3.9.6** (EOL Oct 2025). Rebuilt on **Python 3.12.13** via Homebrew
(`/opt/homebrew/bin/python3.12`). This unlocks modern `asyncio` (`TaskGroup`, `asyncio.to_thread`),
a faster interpreter, and current `sentence-transformers` / `faiss` / `mlflow` wheels.

### ✅ 2. `requirements.txt` added — RESOLVED 2026-06-27
Dependency manifest created, grouped by plan phase/track with `>=` floors. Phase 1 essentials
(`aiohttp`, `pandas`, `numpy`) installed and import-verified. Install the rest per-phase; run
`pip freeze > requirements.lock` when you want an exact pin.

### ✅ 3. `.gitignore` added — RESOLVED 2026-06-27
Python `.gitignore` in place covering `.venv/`, `__pycache__/`, `.ipynb_checkpoints/`, `mlruns/`,
FAISS indexes, datasets (incl. the Kaggle no-show CSV), and `.env`/secrets.

### 🟡 4. README is too thin
Current README is two lines. It's the first thing a recruiter/engineer clicks. It doesn't need to
be big, but it should state: what this repo is, the structure, and (later) link to the
Healthcare No-Show project as the centrepiece.

### 🟡 5. Empty notebook committed
`ml/no_show_eda.ipynb` is an empty notebook. Either flesh it out when you reach Week 4 or leave it
out of commits until then — an empty `.ipynb` adds noise and merge-diff pain.

### 🟢 6. Good: folder structure, naming, early Git habit
Folders mirror the plan, names are clear and consistent (`snake_case`, sensible grouping), and you
created the repo on Day 0 as instructed. That's the single most important habit and you've started it.

---

## Per-area target spec (what "good" looks like — your fill-in guide)

Each section below is what I'll grade the file against once it has content. Use it as the
acceptance bar while you write. Plan week references in **(Wk N)**.

### `python-internals/` — DE track, **(Wk 1–2)**
- **memory_model.py** — REPL snippets for mutable vs immutable, shallow vs deep copy, `id()` vs `==`.
  *Bar:* each snippet has a comment with your **predicted** output above the actual. That prediction
  habit is the whole point.
- **gil_demo.py** — CPU-bound threading vs single-thread (timed) proving the GIL blocks parallelism;
  I/O-bound version showing the GIL releases. *Bar:* prints both timings; a comment states the ratio
  and *why*.
- **async_fetcher.py** — `aiohttp` fetch of 5 URLs concurrently vs sequential, with measured speedup.
  *Bar:* uses `asyncio.gather`, has a sequential baseline, prints speedup. (On 3.11+ show `TaskGroup`.)
- **decorators.py** — `@timer` from scratch, `@retry(n)` with exponential backoff, a class-based
  decorator via `__call__`. *Bar:* all use `functools.wraps`; a comment explains what breaks without it.
- **generators.py** — lazy file reader with `yield`; a `CSV → filter → transform` pipeline with **no
  intermediate lists**; demonstrate `yield from`. *Bar:* memory point is shown, not just asserted.

### `dsa/` + `leetcode/` — daily, **(all phases)**
- *Bar per problem:* a docstring with the approach + **time/space complexity**; a clean solution;
  ideally one alternative (brute-force vs optimal) noted. The plan's value here is *verbal fluency*,
  so a one-line "how I'd explain this" comment is worth more than a second solution.
- Decide on **one** home for DSA: you have both `dsa/` and `leetcode/`. Suggest `leetcode/` for
  per-problem solutions and `dsa/` for pattern/topic notes — but make the split explicit in the README
  so it doesn't drift into duplication.

### `sql/` + `leetcode/sql/` — DE track, **(Wk 2)**
- **window_functions.sql** — `ROW_NUMBER / RANK / DENSE_RANK / LAG / LEAD`, running total, 7-day moving
  average with explicit frame boundaries. *Bar:* a comment explaining the `RANK` vs `DENSE_RANK`
  tie-breaking difference (a classic interview question).
- **query_optimisation.sql** — same query written 3 ways (CTE / subquery / temp table) + `EXPLAIN
  ANALYZE` notes distinguishing full scan vs index scan. *Bar:* you can answer "how do you diagnose a
  slow query?" from this file alone.

### `aws-glue/` — DE track, **(Wk 3)**
- **job_bookmark_demo.py** — a Glue job sketch showing bookmark enable/checkpoint semantics.
- **glue_vs_lambda_tradeoffs.md** — currently "Add notes here." Target: a comparison table (Glue vs
  Lambda vs Step Functions) across cold start, runtime limits, cost model, data volume, and a
  one-paragraph DynamicFrame vs DataFrame tradeoff. This is verbal-prep gold; don't leave it stubbed.

### `ml/` — ML track, **(Wk 4–5)** — *this is your portfolio centrepiece*
- **no_show_eda.ipynb** — EDA on the Kaggle no-show dataset: class imbalance, null rates, distributions,
  documented findings.
- **sklearn_pipeline.py** — `ColumnTransformer` + `XGBoost` end-to-end. *Bar:* a comment explaining
  *why the Pipeline prevents leakage* (fit on train, transform test). Stratified k-fold + AUC/F1 +
  confusion matrix; XGBoost vs LogisticRegression compared.
- **mlflow_tracking.py** — log params/metrics/artifacts across ≥3 runs. *Bar:* runnable; `mlruns/`
  gitignored.
- The plan treats this (Healthcare No-Show Prediction Platform) as the portfolio piece. Hold it to a
  higher bar than the practice files: real README section, "why I built it this way," a metrics screenshot.

### `llm/` — LLM track, **(Wk 4–5)**
- **faiss_demo.py** — tiny FAISS index with `sentence-transformers`: embed ~20 sentences, query top-3.
- **bedrock_invoke.py** — invoke a model via `boto3`; note Knowledge Bases + Agents API at a high level.
  ⚠️ *Bar:* **no AWS keys in code** — use env/role; this is a security red flag if it leaks into Git.
- **prompt_patterns.py** — few-shot, chain-of-thought, structured JSON output with **Pydantic
  validation**. *Bar:* ties to your real Accenture LLM pipeline story (chunking, extraction, failure
  handling) — that's the production experience you own in interviews.

### `system-design/` — **(Phase 3)**
- Three `.md` files (rag_system, healthcare_pipeline, feature_store) currently "Add notes here."
  *Bar:* each is a written design with a diagram (even ASCII), components, data flow, failure modes,
  and tradeoffs. These are talk-tracks, so write them in the voice you'd use out loud.

---

## Reusable review rubric (per file, once it has content)

Grade each file 0–3 on each axis. Aim for ≥2 everywhere before calling a topic "done."

| Axis | 0 | 1 | 2 | 3 |
|------|---|---|---|---|
| **Runs** | errors / placeholder | runs with edits | runs as-is | runs + has a `__main__` / clear entrypoint |
| **Correctness** | wrong | mostly right | correct | correct + edge cases considered |
| **Explains the "why"** | no comments | restates code | explains intent | explains the interview-relevant tradeoff |
| **Measured/verified** | claims only | partial | demonstrates the point | quantifies it (timings, metrics, query plan) |
| **Interview-ready** | can't discuss | shaky | can explain cold | can explain *and* defend tradeoffs in 2 min |

The plan's recurring instruction — *"predict before running," "explain cold, out loud," "record
yourself"* — maps directly to the last two columns. Those are what get you hired; the green checkmarks
are just the scaffolding.

---

## Setup status — all done as of 2026-06-27

| Tool | Action | Status |
|------|--------|--------|
| Python | Upgrade to 3.12 | ✅ 3.12.13 via Homebrew |
| uv | Install + init | ✅ 0.11.25, `pyproject.toml` + `uv.lock` |
| OpenMP | Install for XGBoost | ✅ libomp via Homebrew |
| .gitignore | Python template | ✅ in place |
| Deps | Phase 1+2 all locked | ✅ 4400-line `uv.lock` |

**How to use uv going forward:**
- `uv sync` — recreate `.venv` from lock file (reproducible, repeatable).
- `uv add <package>` — add a new package (updates `pyproject.toml` + `uv.lock`).
- `.venv/bin/python script.py` — run scripts; or activate with `source .venv/bin/activate` if preferred.

## Recommended next actions (in order)

1. **Tonight's plan box first** — GitHub account (done), repo (done), **first real commit** (do this next:
   see below), LinkedIn Open-to-Work, bookmark NeetCode.
2. **First real commit** — Stage and push `.gitignore`, `pyproject.toml`, `uv.lock`, and the updated
   `docs/learning-review.md`. Use message: "Setup: uv environment, Python 3.12, deps lock."
3. **Replace placeholders as you go** — don't batch-create stubs ahead of where you are. A folder of
   empty files reads as abandoned; files that appear as you progress read as momentum.
4. **Re-run this review at the end of Phase 1 (≈17 Jul).** By then `python-internals/`, `sql/`, and
   `aws-glue/` should have real content and there'll be actual code to critique.

---

## What I could not assess today (and why)

- **Code quality / correctness** — no code exists yet.
- **Whether explanations hold up "cold"** — that's a spoken-practice signal the plan tracks via
  recordings, not something in the repo. Consider a `recordings/` note or log so it's visible.
- **Portfolio polish** — the no-show project is the thing that matters most to reviewers, and it's not
  started yet (correctly — it's Week 4+).

*Bottom line: nothing here is behind — you're exactly at the start line. The scaffold is sound. Fix the
three setup items, then let the placeholders turn into real files week by week, and ask me to re-review
at each phase boundary.*
