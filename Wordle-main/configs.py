import random

def read_random_word():
    with open("words.txt") as f:
        word_array = f.read().splitlines()
        return random.choice(word_array)

class Configs():
    def __init__(self):
        self.answer = read_random_word()
#        self.POLICIES_DIR = './policies'
#        self.lr = 0.2
#        self.decay_gamma = 0.9
#        self.exp_rate = 0.3