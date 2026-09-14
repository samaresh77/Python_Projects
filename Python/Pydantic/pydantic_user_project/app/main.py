from pydantic import ValidationError

from app.config import settings
from app.models import User


def main() -> None:
    print(f"Application: {settings.app_name}")
    print(f"Debug: {settings.debug}")

    user_data = {
        "name": "  Rahul  ",
        "age": 25,
        "email": "  RAHUL@EXAMPLE.COM  ",
        "skills": [
            " Python ",
            " FastAPI ",
            " PostgreSQL "
        ],
        "address": {
            "city": "Kolkata",
            "state": "West Bengal",
            "country": "India"
        },
        "social_links": {
            "github": "github.com/rahul",
            "linkedin": "linkedin.com/in/rahul"
        },
        "password": "hello123",
        "confirm_password": "hello123"
    }

    try:
        user = User.model_validate(user_data)

        print("\nUser created successfully!")
        print(user)

        print("\nEmail:")
        print(user.email)

        print("\nCity:")
        print(user.address.city)

        print("\nSkills:")
        print(user.skills)

        print("\nSerialized data:")
        print(user.model_dump())

        print("\nJSON:")
        print(user.model_dump_json())

    except ValidationError as error:
        print("\nValidation failed!")
        print(error.errors())


if __name__ == "__main__":
    main()