from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def daashboard():
    return {"message": "Welcome to the Dashboard 🎉"}