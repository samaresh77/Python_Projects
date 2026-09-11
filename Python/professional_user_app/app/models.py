from dataclasses import dataclass

from app.enums import UserRole


@dataclass
class User:
    id: int
    name: str
    age: int
    role: UserRole