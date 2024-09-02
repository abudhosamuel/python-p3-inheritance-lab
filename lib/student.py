# Ensure that the User class is imported correctly
from lib.user import User

# Define the Student class as a subclass of User
class Student(User):
    def __init__(self, first_name, last_name):
        # Initialize the parent class (User)
        super().__init__(first_name, last_name)
        # Initialize the knowledge attribute as an empty list
        self.knowledge = []

    def learn(self, knowledge_str):
        # Add knowledge to the student's knowledge list
        self.knowledge.append(knowledge_str)
