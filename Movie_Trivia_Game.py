import random
from question_code_for_project import questions as questions
from question_code_for_project import answers as answers

class TriviaGame:
    #open question
    def __init__(self, file):
        self.questions = {}
        self.score1 = 0
        self.score2 = 0
        self.player1 = ''
        self.player2 = ''

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
    def get_unasked_question(self, level, asked_questions):
        unasked_questions = [question for question in self.questions[level] if question not in asked_questions]
        return random.choice(unasked_questions)
    
class Scores:       
    """Class representing the score of a player"""  
    def __init__(self, score):
        self.score = score
            
    def __add__(self, other):
        """Adds a players score with a number.
       
        Args:
            other (int): number being added to a player's score.
        """  
        combined_score = self.score + other
        return Scores(combined_score)
    
    def __sub__(self, other):
        """Subtracts from a players score
        Args:
            other (int): number being used to subtract from the player's score.
        """
        removed_points = self.score - other
        return Scores(removed_points)
    
    
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
        # get_unasked_question = [] things will be appended to it at the end.
        #for x in . loop through the asked questions
        #put all the questions that haven't been asked yet. append those to the get_unasked_question variable
        #we need 6 questions for easy mode. we only have 5 questions. imma add one more question later
        pass
