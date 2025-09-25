## Create a venv and install requirements:
```bash
    python -m venv .venv
    source .venv/bin/activate # or .venv\Scripts\activate on Windows
    pip install -r requirements.txt
```

## Add your OpenAI key:
```bash
    cp .env.example .env # # edit .env and add OPENAI_API_KEY=sk-...
```

## Run the CLI interactive planner:
```bash
    python main.py
```