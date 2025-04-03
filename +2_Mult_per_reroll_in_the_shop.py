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

if teacher == True:

    new_or_add = input("Would you like to create a new card set or add to an old one? ")

    if new_or_add == "new" or new_or_add == "New":
        cards = []
        while True:
            question = input("What is the question for this flashcard?")
            answer = input("What is the answer for this flashcard?")
            new_card = Flash(question, answer)
            cards.append(new_card.to_dict())
            cont = input("more card?")
            if cont == "no" or cont == "No":
                break
        with open("cards.json", "w") as file:
            json.dump(cards, file, indent=4)

    elif new_or_add == "add" or new_or_add == "Add":

        cards = []

        while True:
            question = input("What is the question for this flashcard?")
            answer = input("What is the answer for this flashcard?")
            new_card = Flash(question, answer)
            cards.append(new_card.to_dict())
            cont = input("more card?")

            if cont == "no" or cont == "No":
                break

        try:
            with open("cards.json", "r") as file:
                cards_data = json.load(file)
        except FileNotFoundError:
            cards_data = []
        
        cards_data.append(cards)

        with open("cards.json", "w") as file:
            json.dump(cards_data, file, indent=4)

if teacher == False:
    while True:
        streak = 0
        score = 0
        with open("cards.json", "r") as file:
            cards_data = json.load(file)
        for card in cards_data:
            guess = input(card["Question"])
            if guess == card["Answer"]:
                print("correct! :D")
                streak = streak + 1
                if streak >= 1:
                    score = score + (100 * streak)
                else:
                    score =+ 100
                print(f"Score: {score}!")
                print(f"Streak: {streak}!")
                print()
            else:
                print("incorrect >:(")
                streak = 0
                print("streak reset")
                print(streak)
                print()
        print("FINISH!!")
        break