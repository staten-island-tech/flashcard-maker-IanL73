import json


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

class Flash:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def display_info(self):
        return f"{self.question} {self.answer}"
    
    def to_dict(self):
        return {"Question": self.question, "Answer": self.answer}
    
    def quiz(self):
        if input(f"{self.question} ") == self.answer:
            print("Correct!")
        else:
            print("Wrong!!")

    def create_new(self):
        cards_data = [card.to_dict() for card in new_cards]
        with open("FlashCards.json", "w") as file:
            json.dump(cards_data,file, intent=4)

if teacher == True:
    question = input("What is the question for this flashcard?")
    answer = input("What is the answer for this flashcard?")
    new_card = 