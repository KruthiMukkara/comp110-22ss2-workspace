"""EX02 - One Shot Wordle - Loops!."""
__author__ = "730462650"

secret_word = "python"
guess = str = input("What is your 6-letter guess?: ")

while len(guess) != len(secret_word):
    guess = input("That was not 6 letters! Try again: ")

if len(guess) == len(secret_word): 
    if guess == secret_word:
        print("Woo! You got it!")
    else: 
        print("Not quite. Play again soon!")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index: int = 0
resulting_emoji = ""


while index < len(guess):
    if secret_word[index] == guess[index]:
        resulting_emoji = resulting_emoji + GREEN_BOX
    else:
        character: bool = False
        alternate_index: int = 0
        while not character and alternate_index < len(secret_word):
            if secret_word[alternate_index] == guess[index]:
                character = True
            else:
                alternate_index = alternate_index + 1
        if character:
            resulting_emoji = resulting_emoji + YELLOW_BOX
        else: 
            resulting_emoji = resulting_emoji + WHITE_BOX
    index = index + 1

print(resulting_emoji)


    
