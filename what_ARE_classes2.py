class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"
    
class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email) # Call the parent class constructor
        self.student_id = student_id

    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"
    
class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Subject: {self.subject}"
    
class Administrator(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role
    
    def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"
    
    def manage_system(self):
        return f"{self.role} {self.name} is managing the system."
    
student = Student("Alice", "alice@example.com", "S12345")
teacher = Teacher("Mr. Smith", "smith@example.com", "Mathematics")
administrator = Administrator("Ms. Johnson", "johnson@example.com", "Principal")

print(student.display_info())  # Output: Student: Alice, Email: alice@example.com, Student ID: S12345
print(teacher.display_info())  # Output: Teacher: Mr. Smith, Email: smith@example.com, Subject: Mathematics
print(administrator.display_info())  # Output: Administrator: Ms. Johnson, Email: johnson@example.com, Role: Principal

admin = Administrator("Ms. Johnson", "johnson@example.com", "Principal")
print(admin.manage_system())  # Output: Ms. Johnson (Principal) is managing the system.

my_teacher = Teacher("Mr. Brown", "brown@example.com", "Science")
print(my_teacher.display_info())  # Output: User: Mr. Brown, Email: brown@example.com, Subject: Science