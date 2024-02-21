import numpy as np

from configs import Configs
import random
import sys



class State():
    def __init__(self, p1):
        self.configs = Configs()

        #        self.POLICIES_DIR = self.configs.POLICIES_DIR

        self.p1 = p1


#        self.board = np.zeros((self.BOARD_ROWS, self.BOARD_COLS))
#        print(self.board)
#        print(self.board.ndim)
        self.boardHash = None
        self.isEnd = False
        self.attempts = 0

        #self.playerSymbol = 1

    #    def getHash(self):
    #        self.boardHash = str(self.board.reshape(self.BOARD_ROWS * self.BOARD_COLS))
    #        return self.boardHash

    def getAvailablePositions(self):
        positions = []

        return positions

    def winner(self, guess):
        if guess == self.configs.answer:
            self.isEnd = True
            return 1
        elif self.attempts == 6:
            self.isEnd = True
            return 0

        # game continues
        self.isEnd = False
        return None

    def find_duplicates(string):
        # Initialize an empty list to store duplicate letters
        duplicates = []
        count = 0

        # Loop over each letter in the string
        for letter in string:
            # Check if the letter appears more than once and if it's not already in the duplicates list
            if string.count(letter) > 1 and letter not in duplicates:
                # Append the letter to the duplicates list
                duplicates.append(letter)
                count += 1

        # Return the list of duplicate letters
        return duplicates, count

    def updateStates(self, guess):
        output_string = ""
        for attempt in range(1, 7):


            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')


            for i in range(min(len(guess), 5)):
                if guess[i] == self.configs.answer[i]:
                    output_string += "!"

                elif guess[i] in self.configs.answer:
                    output_string += "o"
                else:
                    output_string += "x"


        return output_string[:5]

    def reset(self):
        self.attempts = 0
        self.word = self.configs.answer
        self.isEnd = False


    #    def giveReward(self):
    #        """
    #        At game end only
    #        """
    #        result = self.winner()
    #
    #        if result == 1:
    #            self.p1.feedReward(1)
    #            self.p2.feedReward(0)
    #
    #        elif result == -1:
    #            self.p1.feedReward(0)
    #            self.p2.feedReward(1)
    #
    #        else:
    #            # if its a draw
    #            self.p1.feedReward(0.1) # less reward
    #            self.p2.feedReward(0.5) # to make p1 more aggressive

    # play 2 humans
    def playGame(self):
        while not self.isEnd:
            # Player 1
            print(self.configs.answer)

            p1_action = self.p1.chooseAction()

            # take action and upate board state
            print(self.updateStates(p1_action))

            # check board status if it is end
            self.attempts += 1
            win = self.winner(p1_action)
            if win is not None:
                if win == 1:
                    print("Congratulations! You guessed the word in %i guesses." % self.attempts)
                else:
                    print("You didn't guess the word within 6 tries, it was '%s'" % self.word)
                self.reset()
                break