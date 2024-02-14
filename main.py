from termcolor import colored
import random
import sys


def read_random_word():
    with open("words.txt") as f:
        word_array = f.read().splitlines()
        return random.choice(word_array)


print("Let's play Wordle:")
print("Type a 5 letter word below and press Enter. You have 6 tries to guess the random word.\n")
print("x means the letter is not in the word")
print("o means the letter is in the word and in the wrong spot")
print("! means the letter is in the word and in the correct spot")

word = read_random_word()
print(word)

for attempt in range(1, 7):
    guess = input().lower()


    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
    output_string = ""

    for i in range(min(len(guess), 5)):
        if guess[i] == word[i]:
            output_string += "!"
        elif guess[i] in word:
            output_string += "o"
        else:
            output_string += "x"
    print(output_string)

    if guess == word:
        print("Congratulations! You guessed the word in %i guesses." % attempt)
    elif attempt == 6:
        print("You didn't guess the word within 6 tries, it was '%s'" % word)
