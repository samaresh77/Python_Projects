from pydantic import BaseModel, Field, field_validator, model_validator


class Address(BaseModel):
    city: str
    state: str
    country: str


class User(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=50
    )

    age: int = Field(
        ge=18,
        le=100
    )

    email: str

    skills: list[str]

    address: Address

    social_links: dict[str, str]

    password: str = Field(
        min_length=8
    )

    confirm_password: str

    @field_validator("name")
    @classmethod
    def clean_name(cls, value: str) -> str:
        return value.strip()

    @field_validator("email")
    @classmethod
    def clean_email(cls, value: str) -> str:
        return value.strip().lower()

    @field_validator("skills")
    @classmethod
    def validate_skills(cls, value: list[str]) -> list[str]:
        cleaned_skills = [
            skill.strip()
            for skill in value
        ]

        if not cleaned_skills:
            raise ValueError("At least one skill is required")

        return cleaned_skills

    @model_validator(mode="after")
    def validate_passwords(self):
        if self.password != self.confirm_password:
            raise ValueError(
                "Password and confirm password must match"
            )

        return self