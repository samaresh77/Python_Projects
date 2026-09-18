# A SQLAlchemy model is a Python class that represents a database table.
# For example:

# class User(Base):
#     ...

# represents:

# users

# And:

# id
# name
# age
# represent the table's columns.

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    age: Mapped[int] = mapped_column(
        nullable=False
    )