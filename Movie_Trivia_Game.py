import random
"""Mateen used the with open to access the questions from the file and f string to display the game prompts"""
class TriviaGame:
    #open question
    def __init__(self, file):
        self.questions = {}
        self.score1 = 0
        self.score2 = 0
        self.player1 = ''
        self.player2 = ''
        with open(file) as file: #with open file
            level = ''
            for line in file:
                line = line.strip()
                if line in ['easy', 'medium', 'hard']:
                    level = line
                    self.questions[level] = []
                else:
                    self.questions[level].append(line.split(','))
# start the game and enter name and level
    def start(self):
        self.player1 = input("Hello, welcome to our Movie Trivia game where we will test your knowledge Start by Entering player 1's name: ")
        self.player2 = input("player 2 enter your name: ")
        level = input("Enter the level that you both want to play on (easy, medium, hard): ")
        self.play(level)
# play the game for 5 rounds and keeps score
    def play(self, level):
        for i in range(5):
            # Randomly select a question from the chosen level's dictionary and ask the first player
            question1 = random.choice(self.questions[level])
            print(f"{self.player1}, {question1[0]}") #f string
            answer1 = input("Your answer: ")
            if answer1.lower() == question1[1].lower():
                print("Correct!")
                self.score1 += 1
            else:
                print(f"Incorrect. The correct answer is {question1[1]}")

            # Randomly select a question from the same level's dictionary and ask the second player
            question2 = self.get_unasked_question(level, [question1])
            print(f"{self.player2}, {question2[0]}")
            answer2 = input("Your answer: ")
            if answer2.lower() == question2[1].lower():
                print("Correct!")
                self.score2 += 1
            else:
                print(f"Incorrect. The correct answer is {question2[1]}")
