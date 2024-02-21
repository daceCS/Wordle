import numpy as np
import pickle
import os
import sys

from configs import Configs


class HumanPlayer:
    def __init__(self, name):
        self.name = name

    def chooseAction(self):
        while True:
            guess = input().lower()
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')

            return guess

    # append a hash state
    def addState(self, state):
        pass

    # at the end of game, backpropagate and update states value
    def feedReward(self, reward):
        pass

    def reset(self):
        pass