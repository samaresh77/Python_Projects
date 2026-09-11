import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    app_name: str = os.getenv(
        "APP_NAME",
        "User Management System"
    )

    data_file: str = os.getenv(
        "DATA_FILE",
        "data/users.json"
    )

    debug: bool = os.getenv(
        "DEBUG",
        "False"
    ).lower() == "true"


settings = Settings()