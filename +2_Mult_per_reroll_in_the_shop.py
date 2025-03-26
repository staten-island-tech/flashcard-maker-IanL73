class User:
    def __init__(self, email, password):
        self.password = password
        self.email = email
    
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"
    
class Student(User):
    def __init__(self, email, password):
        super().__init__(email, password) # Call the parent class constructor
    
class Teacher(User):
    def __init__(self, email, password, key):
        super().__init__(email, password)
        self.key = key