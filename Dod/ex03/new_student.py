# new_student.py
import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random 15-letter lowercase identifier."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represents a student with an auto-generated id and login."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Compute the login after initialization using name and surname."""
        self.login = self.name[0].upper() + self.surname.lower()
