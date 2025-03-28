while True:
    mode = input("What mode? ")
    if mode == "Student" or mode == "student" or mode == "S" or mode == "s":
        print("In Student mode.")
        teacher = False
        break
    elif mode == "Teacher" or mode == "teacher" or mode == "t" or mode == "T":
        print("In Teacher mode.")
        teacher = True
        break
    else:
        print("Invalid input.")
        print()

import json

class Flash:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    
    def to_dict(self):
        return {"question": self.question, "answer": self.answer,}

if teacher == True:
    while True:
        new_cardset = []
        new_question = input("what question ")
        new_answer = input("what answer ")
        new_flash = Flash(new_question, new_answer)
        new_cardset.append(new_flash.to_dict())
        cont = input("continue? ").lower
        if cont == "no":
            break