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
# .venv\scripts\python.exe
uv add fastapi
uv add python-dotenv
uv add fastapi-users[sqlalchemy]
uv add imagekitio
uv add uvicorn[standard]
uv add aiosqlite
uv add streamlit
# run
# http://localhost:8000/docs
# user auth: user1@user.net 123 /auth/register -> authorize
uv run main.py
# second terminal
uv run streamlit run frontend.py
```
