# Hangman game by Ryan C. McDermott #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Using the SOWPODS dictionary contained in the sowpods.txt file, a word is
# selected at random and the user has 6 guesses in order to reveal the random
# word. Good luck!

import random
import string

filename = "sowpods.txt"
alph = string.ascii_uppercase

# Initialising game render and parts of hanged man

ROW1 = "    ________   "
ROW2 = "    |       |   "
ROW3 = ["    |      ",""]
ROW4 = ["    |   ","","",""]
ROW5 = ["    |    ","",""]
ROW6 = "____|          "

head = "O"
left_arm = "o-"
right_arm = "-o"
left_leg = "_/"
right_leg = "\_"
torso1 = "  |"
torso2 = "|"



# function to read text file, create list of values within file and return random element in list
def choose_random_word(filename):
    word_list = []
    with open(filename, 'r') as f:
        for i in f:
            word_list.append(i)
    return word_list[random.randint(0, len(word_list))]

# Player input
def player_guess():
    guess = input("Guess a letter (upper-case):\n>")
    return guess

def draw_hanged_man(lives):
    if lives == 6:
        print(ROW1), print(ROW2), print(ROW3[0],ROW3[1])
        print(ROW4[0],ROW4[1],ROW4[2],ROW4[3]), print(ROW5[0],ROW5[1],ROW5[2])
        print(ROW6)
    if lives == 5:
        ROW3[1] = head
        print(ROW1), print(ROW2), print(ROW3[0],ROW3[1])
        print(ROW4[0],ROW4[1],ROW4[2],ROW4[3]), print(ROW5[0],ROW5[1],ROW5[2])
        print(ROW6)
    if lives == 4:
        ROW4[2] = torso1
        print(ROW1), print(ROW2), print(ROW3[0],ROW3[1])
        print(ROW4[0],ROW4[1],ROW4[2],ROW4[3]), print(ROW5[0],ROW5[1],ROW5[2])
        print(ROW6)
    if lives == 3:
        ROW4[2] = torso2
        ROW4[1] = left_arm
        print(ROW1), print(ROW2), print(ROW3[0],ROW3[1])
        print(ROW4[0],ROW4[1],ROW4[2],ROW4[3]), print(ROW5[0],ROW5[1],ROW5[2])
        print(ROW6)
    if lives == 2:
        ROW4[3] = right_arm
        print(ROW1), print(ROW2), print(ROW3[0],ROW3[1])
        print(ROW4[0],ROW4[1],ROW4[2],ROW4[3]), print(ROW5[0],ROW5[1],ROW5[2])
        print(ROW6)
    if lives == 1:
        ROW5[1] = left_leg
        print(ROW1), print(ROW2), print(ROW3[0],ROW3[1])
        print(ROW4[0],ROW4[1],ROW4[2],ROW4[3]), print(ROW5[0],ROW5[1],ROW5[2])
        print(ROW6)
    if lives == 0:
        ROW5[2] = right_leg
        print(ROW1), print(ROW2), print(ROW3[0],ROW3[1])
        print(ROW4[0],ROW4[1],ROW4[2],ROW4[3]), print(ROW5[0],ROW5[1],ROW5[2])
        print(ROW6)

# Clean game
def fresh_game():
    ROW3[1] = ""
    ROW4[2] = ""
    ROW4[1] = ""
    ROW4[3] = ""
    ROW5[1] = ""
    ROW5[2] = ""

# Draw initial game
def draw_game(word_to_guess):
    print(ROW1), print(ROW2), print(ROW3[0],ROW3[1])
    print(ROW4[0],ROW4[1],ROW4[2],ROW4[3]), print(ROW5[0],ROW5[1],ROW5[2])
    print(ROW6)
    print("Welcome to Hang-man!\n***********")
    print("You have 6 lives!\n***********")
    print(f"Your word contains {len(word_to_guess)} letters\n***********")
    game = ["_"]*len(word_to_guess)
    for i in range(0, len(word_to_guess)):
        print(game[i], end = ' ')
    print("\n")
    return game

# Checks player's guess and returns correct element index
def guess_check(guess, word):
    correct = [pos for pos, char in enumerate(word) if char == guess]
    return correct

# Updates the original game state
def update_game(game, correct_elements, guess):
    for i in correct_elements:
        game[i] = guess
    for j in range(0, len(game)):
        print(game[j], end = ' ')
    print("\n")
    return game


def main():
    # Initialisation of game
    word_to_guess = choose_random_word(filename)
    game = draw_game(word_to_guess)
    play = True
    turn = 0
    lives = 6
    correct_guesses = 0


    while play == True:

        # Calls player input function and returns error if invalid characters are used
        guess = player_guess()
        while guess in game:
            print("You have already guessed that. Please try again:")
            guess = player_guess()
        while len(guess) > 1:
            print("Too many values, expected 1. Please try again:")
            guess = player_guess()
        while guess not in alph:
            print("Invalid input. Please try again:")
            guess = player_guess()
        while guess == "":
            print("Invalid input. Please try again:")
            guess = player_guess()

        correct = guess_check(guess, word_to_guess)
        if not correct:
            lives -= 1
        game = update_game(game, correct, guess)
        turn += 1
        print(f"Lives remaining: {lives}")
        draw_hanged_man(lives)
        correct_guesses += len(correct) # To ensure double correct letters added
        if correct_guesses == len(word_to_guess):
            print(f"Congratulations, you win! You took {turn} turns")
            play = False
        if lives == 0:
            print("Out of lives!")
            play = False

    # Player input to play again
    play_again = input("Would you like to play again? (y/n):\n>")
    while play_again != "y" and play_again != "n":
        print("Invalid input")
        play_again = input("Would you like to play again? (y/n):\n>")
    if play_again == "y":
        fresh_game()
        main()
    if play_again == "n":
        print("Thank you for playing!")
        pass


if __name__ == '__main__':
    main()
