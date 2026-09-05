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
    print("******HANGMAN*******")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("********************")




def display_hint(hint):
    print(" ".join(hint))

def display_word(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:

        display_man(wrong_guesses)
        display_hint(hint)
        guess = input(f"Guess a letter with {len(hint)} letters: ").lower()
        print("____________________________")

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a letter")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            print("Guess again another letter")

            continue
        guessed_letters.add(guess)

        if guess in answer:

            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_hint(hint)
            display_word(answer)
            print("You won the game!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            print("You lost the game!")
            print(f"the correct answer was ({answer}).")
            is_running = False













if __name__ == "__main__":
    main()


