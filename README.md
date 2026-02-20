# Backend Project
Backend project using python fastapi to upload, store and delete images with user authentication. 

## Dependencies
- [python](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv)
- [imagekit](https://imagekit.io/)

## Environment Setup
```bash
cd backend_project
uv init .
# venv & dependencies 
# python interpreter: .venv\scripts\python.exe
# fill api keys on .env
uv add fastapi python-dotenv "fastapi-users[sqlalchemy]" imagekitio "uvicorn[standard]" aiosqlite streamlit
# run
# http://localhost:8000/docs
# user auth: user1@user.net 123 /auth/register -> authorize
uv run main.py
# second terminal
uv run streamlit run frontend.py
```
