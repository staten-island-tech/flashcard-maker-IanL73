while True:
    mode = input("What mode? ")
    if mode == "Student" or mode == "student" or mode == "S" or mode == "s":
        print("In Student mode.")
        break
    elif mode == "Teacher" or mode == "teacher" or mode == "t" or mode == "T":
        print("In Teacher mode.")
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

    def create(self):
        new_question = input("Input the question for this card. ")
        new_answer = input("Input the answer for this card. ")
        new_card = Flash(new_question, new_answer)
        cards_data = 
        try:
            with open("FlashCards.json", "w") as file:
                cards_data json.load(file)