lsof -t -i tcp:8003 | xargs kill -9
uvicorn main:app --reload --port=8003