import random
from question_code_for_project import questions, answers

class TriviaGame:
    """A class representing a game of movie trivia.

    Attributes:
        questions (dict): A dictionary containing questions for different levels.
        score1 (int): The score of player 1.
        score2 (int): The score of player 2.
        player1 (str): The name of player 1.
        player2 (str): The name of player 2.
        continue_playing (bool): A flag indicating whether the game should continue.

    Methods:
        start(): Begins the game and prompts players to enter their names and the desired level of play.
        play(level): Plays the game for 5 rounds and keeps score.
        get_unasked_question(level, asked_questions): Returns a randomly selected unasked question from the specified level's dictionary.
        check_for_tie(): Checks if the game ended in a tie, if so it then executes the tie_breaker method.
    """

    def __init__(self):
        """
        Initializes a new instance of the class.
        """
        self.questions = questions
        self.score1 = 0
        self.score2 = 0
        self.player1 = ''
        self.player2 = ''
        self.continue_playing = True

    def start(self):
        """Begins the game and prompts players to enter their names and the desired level of play."""
        self.player1 = input("Hello, welcome to our Movie Trivia game where we will test your knowledge. Start by entering player 1's name: ")
        self.player2 = input("Player 2 enter your name: ")
        level = input("Enter the level that you both want to play on (easy, medium, hard): ")
        while level not in ["easy", "medium", "hard"]:
            level = input("Invalid level. Enter the level that you both want to play on (easy, medium, hard): ")
        self.play(level)
        
    # play the game for 5 rounds and keeps score
    def play(self, level):
        """
        Main Author: Mateen Lachir : F - Strings 
        Play the game for 5 rounds and keep score.

        Args:
            level (str): the level of the game to play (e.g., 'easy', 'medium', or 'hard')

        Side effects:
            - Updates the game score for player 1 and player 2.
            - Prints messages to the console to prompt the user for input and to display the results of each round.
            - Prints the final scores to the console.

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
            if answer1.lower() == answers[level][question1].lower():
                print("Correct!")
                self.score1 += 1
            else:
                print(f"Incorrect. The correct answer is {answers[level][question1]}")
            if not self.continue_playing:
                break
            # Randomly select an unasked question from the same level's dictionary and ask the second player
            question2 = self.get_unasked_question(level, asked_questions)
            asked_questions.append(question2)
            print(f"{self.player2}, {question2}")
            answer2 = input("Your answer: ")
            if answer2.lower() == answers[level][question2].lower():
                print("Correct!")
                self.score2 += 1
            else:
                print(f"Incorrect. The correct answer is {answers[level][question2]}")
                
        # Print the final scores
        print(f"Final Scores:\n{self.player1}: {self.score1}\n{self.player2}: {self.score2}")
        
    def get_unasked_question(self, level, asked_questions):
        """
        Main Author Mateen Lachir : List Comprehension.
        Returns a randomly selected unasked question from the specified level's dictionary.

        Args:
            level (str): the level of the game to play (e.g., 'easy', 'medium', or 'hard')
            asked_questions (list): a list of questions that have already been asked

        Returns:
            str: a randomly selected unasked question from the specified level's dictionary
        """
        unasked_questions = [question for question in self.questions[level] if question not in asked_questions]
        return random.choice(unasked_questions)

    def check_for_tie(self, tie_breaker_level="Medium"):
        """
        Check if there is a tie between the players and call the tie_breaker method if needed.

        Primary author: Emmanuel Akpalu.
        Emmanuel uses an optional argument. If the user doesn't provide a specific level, medium is used as the defualt level.

        Side effects:
            Prints a message and calls the tie_breaker method if there is a tie.
        """
        if self.score1 == self.score2:
            print("The game ended in a tie! Starting a tiebreaker round.")
            tiebreaker_player = Player(self.score1, self.score2, self.player1, self.player2)
            tiebreaker_player.tie_breaker(level = tie_breaker_level)

class Player(TriviaGame):
    """
    A class representing a player in the movie trivia game.

    Attributes:
        Inherits attributes from TriviaGame class

    Methods:
        __init__(score1, score2, player1, player2): Initializes a Player instance with the given scores and player names.
        tie_breaker(): Starts a tiebreaker round to determine the winner in case of a tie.
    """

    def __init__(self, score1, score2, player1, player2):
        """
        Initializes a Player instance with the given scores and player names.

        Args:
            score1: Score for player 1
            score2: Score for player 2
            player1: Name of player 1
            player2: Name of player 2

        Primary author: Akpalu.
        Emmanuel used super.

        """
        super().__init__(self, score1, score2, player1, player2)

    def tie_breaker(self):
        """
        Starts a tiebreaker round to determine the winner in case of a tie. The level of difficulty is entered by the user. 
        The tiebreaker question is randomly selected from the list of unasked questions of the chosen level. 
        The score of the winner of the tiebreaker round is updated and the final scores and winner or tie message are printed.
        
        Side effects:
            Modifies the score of the winner of the tiebreaker round
            Prints the final scores and winner or tie message
        
        Returns:
            None

        Primary author: Emmanuel Akpalu.
        Emmanuel used conditional expressions.
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
        Primary author: Romeo Alvarenga.

        Initializes, sets attributes.
        
        Args:
            score (int): a player's score.
        
        Side effects:
            Sets attributes.
        """
        self.score = score
            
    def __add__(self, other):
        """
        Primary author: Romeo Alvarenga.

        Adds a players score another person score.
       
        Args:
            other (int): number being added to a player's score.
            
        Returns:
            The added integer.
        """  
        combined_score = self.score + other.score
        return Scores(combined_score)
    
    def __sub__(self, other):
        """
        Primary author: Romeo Alvarenga.

        Subtracts from a players score by another player score.
        Args:
            other (int): number being used to subtract from the player's score.
        
        Returns:
            The subtracted integer/
        """
        removed_points = self.score - other.score
        return Scores(removed_points)
    
    def __and__(self, other):
        """ 
        Primary author: Romeo Alvarenga.
        
        Takes in sets as scores and gives union of score from two sets.
        
        Args:
            other (set): a set of integers for scores.
            
        Returns:
            union set
        """
        combine = self.score & other.score
        return Scores(combine)

    def __or__(self, other):
        """
        Primary author: Romeo Alvarenga.
        
        Takes in sets of scores and gives intersection of scores from the sets.
        
        Args:
            other (set): a set of integers for scores.
            
        Returns:
            Intersection of set.
        """
        combine = self.score | other.score
        return Scores(combine)
    
if __name__ == "__main__":
    play_again = True
    while play_again:
        game = TriviaGame()
        game.start()
        play_again_input = input("Do you want to play again? (y/n) ")
        play_again = play_again_input.lower() == 'y'
