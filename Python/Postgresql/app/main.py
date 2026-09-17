from fastapi import FastAPI

from app.database import engine

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "FastAPI is running"
    }


@app.get("/db-test")
def database_test():
    try:
        with engine.connect() as connection:
            return {
                "message": "Database connection successful"
            }
    except Exception as error:
        return {
            "message": "Database connection failed",
            "error": str(error)
        }