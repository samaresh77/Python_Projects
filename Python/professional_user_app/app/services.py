import json
from dataclasses import asdict

from app.config import settings
from app.enums import UserRole
from app.logger import logger
from app.models import User


def load_users() -> list[User]:
    try:
        with open(settings.data_file, "r") as file:
            data = json.load(file)

        return [
            User(
                id=user["id"],
                name=user["name"],
                age=user["age"],
                role=UserRole(user["role"])
            )
            for user in data
        ]

    except FileNotFoundError:
        logger.warning("User data file not found")
        return []


def save_users(users: list[User]) -> None:
    data = [
        {
            "id": user.id,
            "name": user.name,
            "age": user.age,
            "role": user.role.value
        }
        for user in users
    ]

    with open(settings.data_file, "w") as file:
        json.dump(data, file, indent=4)

    logger.info("Users saved successfully")


def add_user(
    users: list[User],
    name: str,
    age: int,
    role: UserRole
) -> User:

    if not name.strip():
        raise ValueError("Name cannot be empty")

    if age <= 0:
        raise ValueError("Age must be greater than 0")

    new_id = max(
        (user.id for user in users),
        default=0
    ) + 1

    user = User(
        id=new_id,
        name=name,
        age=age,
        role=role
    )

    users.append(user)

    save_users(users)

    logger.info("User created: %s", user.name)

    return user


def find_user(
    users: list[User],
    user_id: int
) -> User | None:

    for user in users:
        if user.id == user_id:
            return user

    return None


def delete_user(
    users: list[User],
    user_id: int
) -> bool:

    user = find_user(users, user_id)

    if user is None:
        return False

    users.remove(user)
    save_users(users)

    logger.info("User deleted: %s", user.name)

    return True