from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def dashboard():    
    return {"message": "Welcome to the Dashboard 🎉"}