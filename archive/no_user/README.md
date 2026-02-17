## Dependencies
- [python](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv)
- [imagekit](https://imagekit.io/)

## Environment Setup
```bash
cd backend_project
uv init .
# venv & dependencies 
# .venv\scripts\python.exe
uv add fastapi
uv add python-dotenv
uv add fastapi-users[sqlalchemy]
uv add imagekitio
uv add uvicorn[standard]
uv add aiosqlite
# run
# http://localhost:8000/docs
uv run main.py
```
