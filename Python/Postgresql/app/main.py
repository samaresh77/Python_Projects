from fastapi import FastAPI

from app.database import Base, engine
from app.models import User

app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message": "FastAPI is running"
    }


@app.get("/db-test")
def database_test():
    try:
        with engine.connect():
            return {
                "message": "Database connection successful"
            }
    except Exception as error:
        return {
            "message": "Database connection failed",
            "error": str(error)
        }