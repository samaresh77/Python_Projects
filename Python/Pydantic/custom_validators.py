# Custom Validators
# In Pydantic v2, the main tools are:
# field_validator
# model_validator

# Use field_validator when you want to validate or transform one particular field.
from pydantic import BaseModel, field_validator


class User(BaseModel):
    username: str
    age: int

    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str) -> str:
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters")

        return value

user = User(
    username="Rahul",
    age=25
)

print(user)

# @field_validator("field_name")
# @classmethod
# def validator_name(cls, value):
#     ...
#     return value

# Field() vs field_validator
#field
from pydantic import BaseModel, Field


class Product(BaseModel):
    price: float = Field(gt=0)

# validator
@field_validator("price")
@classmethod
def validate_price(cls, value):
    ...

# Model validator
from pydantic import BaseModel, model_validator


class RegisterUser(BaseModel):
    username: str
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def validate_passwords(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")

        return self

user = RegisterUser(
    username="rahul",
    password="hello123",
    confirm_password="hello123"
)
# user = RegisterUser(
#     username="rahul",
#     password="hello123",
#     confirm_password="hello456" #give error
# )
print(user)

# field_validator vs model_validator
# field_validator

# Validates one field.

# @field_validator("email")

# Example:

# email
#  ↓
# validate email

# model_validator

# Validates the whole model.

# @model_validator(mode="after")

# Example:

# password
#      +
# confirm_password
#      ↓
# compare them

#                  Request
#                     ↓
#               Pydantic Model
#                     ↓
#         ┌───────────┴───────────┐
#         ↓                       ↓
# field_validator         model_validator
#         ↓                       ↓
# clean username          compare passwords
#         ↓                       ↓
#         └───────────┬───────────┘
#                     ↓
#               Validated data
#                     ↓
#                 Service
#                     ↓
#                Database


# Validation error
from pydantic import BaseModel, ValidationError, field_validator


class User(BaseModel):
    username: str

    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str) -> str:
        value = value.strip()

        if len(value) < 3:
            raise ValueError(
                "Username must be at least 3 characters"
            )

        return value


try:
    user = User(username="AB")

except ValidationError as error:
    print("Validation failed!")
    print(error.errors())