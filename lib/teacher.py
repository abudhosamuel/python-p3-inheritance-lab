# Ensure that the User class is imported correctly
from lib.user import User

import random

# Define the Teacher class as a subclass of User
class Teacher(User):
    def __init__(self, first_name, last_name):
        # Initialize the parent class (User)
        super().__init__(first_name, last_name)
        # Initialize the knowledge attribute with predefined knowledge
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]

    def teach(self):
        # Return a random piece of knowledge
        return random.choice(self.knowledge)
