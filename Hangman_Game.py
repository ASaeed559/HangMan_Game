import time
import random

#Hangman Game


words = ("apple", "banana", "cherry", "mango", "grape", "strawberry")

#dictionary for arts:

hangman_art = {
        0: ("       ",
            "       ",
            "       "),
        1: ("   o   ",
            "       ",
            "       "),
        2: ("   o   ",
            "   |  ",
            "       "),
        3: ("   o   ",
            "  /|   ",
            "       "),
        4: ("   o  ",
            "  /|\\ ",
            "       "),
        5: ("   o   ",
            "  /|\\  ",
            "  /    "),
        6: ("   o   ",
            "  /|\\  ",
            "  / \\  ")}


def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)




def display_hint(hint):
    print(" ".join(hint))

def display_word(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    is_running = True

    while is_running:

        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()


        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a letter")
            continue

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        elif guess not in answer:
            wrong_guesses += 1













if __name__ == "__main__":
    main()


