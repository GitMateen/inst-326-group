import random
from question_code_for_project import questions, answers

class TriviaGame:
    #open question
    def __init__(self):
        """
        Primary author:
        Suporting author:
        Supporting author: 

        Initializes, sets attributes.
        
        Side effects:
            Sets attributes.
        """
        self.questions = questions
        self.score1 = 0
        self.score2 = 0
        self.player1 = ''
        self.player2 = ''
        self.continue_playing = True

 # start the game and enter name and level
    def start(self):
        """
        Primary author:
        Suporting author:
        Supporting author:
        Starts the game by taking the players names and difficulty. 
        
        Side effects:
            Changes player1's and player2's attributes.
        """
        self.player1 = input("Hello, welcome to our Movie Trivia game where we will test your knowledge. Start by entering player 1's name: ")
        self.player2 = input("Player 2 enter your name: ")
        level = input("Enter the level that you both want to play on (easy, medium, hard): ")
        while level not in ["easy", "medium", "hard"]:
            level = input("Invalid level. Enter the level that you both want to play on (easy, medium, hard): ")
        self.play(level)
        
    # play the game for 5 rounds and keeps score
    def play(self, level):
        """
        Primary author:
        Suporting author:
        Supporting author:
        
        Starts playing the game to both players. Plays the game for 5 rounds, for each player.
        
        Args:
            level (str): the difficulty the players chose (easy, medium, or hard).
        
        Side effects:
             Prints to stdout        
        """
        asked_questions = []
        for i in range(5):
                if not self.continue_playing:
                    break
                # Randomly select an unasked question from the chosen level's dictionary and ask the first player
                question1 = self.get_unasked_question(level, asked_questions)
                asked_questions.append(question1)
                print(f"{self.player1}, {question1}")
                answer1 = input("Your answer: ")
                #if answer1.lower() == answers[level][question1].lower():
                    #print("Correct!")
                    #self.score1 += 1
                question_index = questions[level].index(question1)
                correct_answer = answers[level][question_index]
                for x in questions:
                    if x == question1:
                      if answer1.lower() == answers[level][question1].lower():
                          print("Correct!")
                          self.score += 1
                    else:
                        #print(f"Incorrect. The correct answer is {answers[level][question1]}")
                        print(f"Incorrect. The correct answer is {correct_answer}")
                    if not self.continue_playing:
                        break
                # Randomly select an unasked question from the same level's dictionary and ask the second player
                question2 = self.get_unasked_question(level, asked_questions)
                asked_questions.append(question2)
                print(f"{self.player2}, {question2}")
                answer2 = input("Your answer: ")
                #if answer2.lower() == answers[level][question2].lower():
                   # print("Correct!")
                   # self.score2 += 1
                #else:
                   # print(f"Incorrect. The correct answer is {answers[level][question2]}")
                question_index_two = questions[level].index(question2)
                correct_answer_two = answers[level][question_index_two]
                for y in questions:
                    if y == question2:
                      if answer2.lower() == answers[level][question2].lower():
                          print("Correct!")
                          self.score += 1
                    else:
                        #print(f"Incorrect. The correct answer is {answers[level][question1]}")
                        print(f"Incorrect. The correct answer is {correct_answer_two}")
                    
                # Print the current scores
                print(f"Current Scores:\n{self.player1}: {self.score1}\n{self.player2}: {self.score2}")
                
        # Print the final scores
        print(f"Final Scores:\n{self.player1}: {self.score1}\n{self.player2}: {self.score2}")
        
     
    def get_unasked_question(self, level, asked_questions):
        """ 
        Primary author:
        Suporting author:
        Supporting author:
        """
        unasked_questions = [question for question in self.questions[level] if question not in asked_questions]
        return random.choice(unasked_questions)

class Player(TriviaGame):
    """
    A class representing a player in the movie trivia game.
    """
    def __init__(self):
        """
        Primary author: Akpalu
        Suporting author:
        Supporting author:

        Emmanuel used to super(). 

        """
        super().__init__()

    def tie_breaker(self):
        """
        Primary author: Emmanuel Akpalu
        Suporting author:
        Supporting author:

        Emmanuel used f-strings.
        
        Starts a tiebreaker round to determine the winner in case of a tie. The level of difficulty is entered by the user. 
        The tiebreaker question is randomly selected from the list of unasked questions of the chosen level. 
        The score of the winner of the tiebreaker round is updated and the final scores and winner or tie message are printed.
        
        Side effects:
        - Modifies the score of the winner of the tiebreaker round
        - Prints the final scores and winner or tie message
        
        Returns:
        - None
        """
        print("We have a tiebreaker round to determine the winner!")
        level = input("Enter the level of difficulty for the tiebreaker round (easy, medium, hard): ")
        while level not in ["easy", "medium", "hard"]:
            level = input("Invalid level. Enter the level of difficulty for the tiebreaker round (easy, medium, hard): ")

        question_breaker = random.choice(self.get_unasked_question)

        # Ask the tiebreaker question
        tiebreaker_question = question_breaker
        print(f"Here's the tiebreaker question:\n{tiebreaker_question}")
        tiebreaker_answer = input("Your answer: ")
        if tiebreaker_answer.lower() == answers[level][tiebreaker_question].lower():
            print("Correct! You have won the tiebreaker!")
            self.score1 += 1
        else:
            print(f"Incorrect. The correct answer is {answers[level][tiebreaker_question]}")
            self.score2 += 1

        # Print the final scores
        print(f"Final Scores:\n{self.player1}: {self.score1}\n{self.player2}: {self.score2}")
        if self.score1 > self.score2:
            print(f"{self.player1} wins!")
        elif self.score2 > self.score1:
            print(f"{self.player2} wins!")
        else:
            print("It's a tie!")

class Scores:       
    """Class representing the score of a player"""  
    def __init__(self, score):
        """
        Primary author:
        Suporting author:
        Supporting author:

        Initializes, sets attributes.
        
        Args:
            score (int): a player's score.
        
        Side effects:
            Sets attributes.
        """
        self.score = score
            
    def __add__(self, other):
        """
        Primary author:
        Suporting author:
        Supporting author:

        Adds a players score with a number.
       
        Args:
            other (int): number being added to a player's score.
        """  
        combined_score = self.score + other
        return Scores(combined_score)
    
    def __sub__(self, other):
        """
        Primary author:
        Suporting author:
        Supporting author:

        Subtracts from a players score
        Args:
            other (int): number being used to subtract from the player's score.
        """
        removed_points = self.score - other
        return Scores(removed_points)
    
    def score(self):
        """
        Primary author:
        Suporting author:
        Supporting author:

        Keeps track of player's score and updates them per round of questions.
        """
        pass
    
    def final_score(self):
        """
        Primary author:
        Suporting author:
        Supporting author:

        Prints out the final socre after the 5 rounds. If its a tie, the code will start the tie_breaker method.
        """
        pass

play_again = True
while play_again:
    game = TriviaGame()
    game.start()
    play_again_input = input("Do you want to play again? (y/n) ")
    play_again = play_again_input.lower() == 'y'

