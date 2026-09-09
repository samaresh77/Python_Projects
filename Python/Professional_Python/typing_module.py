# Optional means:
# This value can be a particular type or None.

from typing import Optional
name: Optional[str] = None

def find_user(user_id: int) -> Optional[dict]:
    ...

# Union
from typing import Union

def process_value(value: Union[int, str]) -> Union[int, str]:
    return value

# Any
from typing import Any

value: Any = 10
value = "Python"
value = True
value = [1, 2, 3]

# calable
from typing import Callable

def execute_operation(
    operation: Callable,
    value: int
):
    return operation(value)

def square(number: int) -> int:
    return number * number

result = execute_operation(square, 5)

print(result)

# TypeAlias
from typing import TypeAlias

User: TypeAlias = dict[str, int | str]
def get_user() -> User:
    ...

#Literal
from typing import Literal

def get_user(
    role: Literal["admin", "user"]
):
    ...