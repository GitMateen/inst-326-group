import random

class TriviaGame:
    def __init__(self):
        self.questions = {
            "easy": [
                "What is the ",
                "What is the ",
                "What is the ",
                "What is the ",
                "What is the "
            ],
            "medium": [
                "What is the ",
                "What is the ",
                "What is the ",
                "What is the",
                "Who was the "
            ],
            "hard": [
                "What is ",
                "What is ",
                "What is =",
                "What is ",
                "What is "
            ]
        }
        self.answers = {
            "": "easy",
            "": "easy",
            "": "easy",
            "": "easy",
            "": "easy",
            "": "medium",
            "": "medium",
            "": "medium",
            "": "medium",
            " ": "medium",
            "": "hard",
            "": "hard",
            "": "hard",
            "": "hard",
            "": "hard"
        }
        self.questions_asked = []
        self.num_correct = 0
        self.num_wrong = 0

    def get_question(self, level):
        """Randomly selects a question from the given difficulty level."""
        question = random.choice(self.questions[level])
        # Make sure we haven't asked this question already
        while question in self.questions_asked:
            question = random.choice(self.questions[level])
        self.questions_asked.append(question)
        return question
    
    def play(self):
        print("Welcome to the Trivia Game!")
        while True:
            # Ask the user for the difficulty level
            level = input("Choose a difficulty level (easy, medium, hard): ")
            if level not in self.questions:
                print("Invalid difficulty level. Please choose again.")
                continue
            # Get a question and ask the user
            question = self.get_question(level)
            print(question)
            answer = input("Enter your answer: ").lower()
            # Check if the answer is correct
            if answer == self.answers.get(question.lower()):
                print("Correct!")
                self.num_correct += 1
            else:
                print("Wrong.")
                self.num_wrong += 1
            # Ask if the user wants to continue playing
            choice = input("Do you want to continue playing? (y/n): ").lower()
            if choice != "y":
                break
        # Print the final score
        print("Game over!")
        print(f"Number of correct answers: {self.num_correct}")
        print(f"Number of wrong answers: {self.num_wrong}")