import random
from question_code_for_project import questions
from question_code_for_project import answers

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

class Player:
    """
    A class representing a player in the movie trivia game.
    """
    def __init__(self):
        pass

    def name(self):
        pass

    def score(self):
        """
        Keeps track of player's score and updates them per round of questions.
        """
        pass

    def final_score(self):
        """
        Prints out the final socre after the 5 rounds. If its a tie, the code will start the tie_breaker method.
        """
        pass

    def tie_breaker(self):
        """
        When player_one and player_two have the same score at the end of all the rounds. 
        There is one final question break the tie and decide a winner.
        """
        pass

    def get_unasked_question(self):
        """
        Get the random questions that have not been asked yet in the current game round.
        Implement this in the play method at the end.
        """
        pass