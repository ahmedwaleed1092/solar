# TAYF Solar AI Assistant API

AI-powered conversational assistant for **TAYF** — an AI-Powered Solar
Plant Intelligence, Predictive Maintenance & Autonomous Operations
Platform (graduation project).

## Project structure

```
tayf-ai-assistant/
├── main.py            # FastAPI app, CORS, health & root endpoints
├── chat.py            # /api/chat router + TAYF system prompt + Groq call
├── requirements.txt   # Python dependencies
├── .env.example        # Copy to .env and fill in your real key
└── .gitignore
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env
# then edit .env and paste your real GROQ_API_KEY
```

## Run

```bash
uvicorn main:app --reload
```

- Docs: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health
- Chat endpoint: `POST http://127.0.0.1:8000/api/chat`

Example request body:

```json
{
  "message": "What is soiling in solar plants?"
}
```

## Fixes applied to the original code

1. **Double `/api` prefix (routing bug).**
   `chat.py` already declares `APIRouter(prefix="/api", ...)`, but
   `main.py` also called `app.include_router(router, prefix="/api")`.
   That made every route live at `/api/api/chat` instead of
   `/api/chat`, which would break any frontend calling `/api/chat`.
   Fixed by calling `app.include_router(router)` with no extra prefix.

2. **Invalid CORS configuration.**
   `allow_origins` included `"*"` together with
   `allow_credentials=True`. Browsers reject wildcard origins when
   credentials are allowed, so CORS would silently fail for real
   browser clients. Fixed by listing explicit dev origins only. Add
   your production frontend's origin (ideally from an environment
   variable) before deploying.

3. **Secrets hygiene.**
   The original `.env` contained a real-looking key. Replaced with
   `.env.example` (placeholder only) plus a `.gitignore` that excludes
   `.env`, so a real key never gets committed accidentally.

4. **Dependency pinning.**
   Added a `requirements.txt` with pinned versions so the project is
   reproducible for anyone who clones it.

Everything else (the TAYF system prompt, the anti-hallucination rules,
the `/api/chat` request/response models, error handling) was kept as
you wrote it — only the bugs above were touched.
