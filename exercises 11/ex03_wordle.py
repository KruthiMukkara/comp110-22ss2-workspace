"""EX03 - Structured Wordle."""
__author__ = "730462650"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, character: str) -> bool:
    """Finds the single character at any index of word."""
    assert len(character) == 1
    index: int = 0
    while index < len(word): 
        if word[index] == character: 
            return True 
        index += 1
    return False 


def emojified(guess: str, secret: str) -> str: 
    """Returns a colored emoji box based on accuracy of guess."""
    resulting_emoji: str = ""
    index: int = 0 
    assert len(guess) == len(secret)
    while index < len(guess):
        if contains_char(secret, guess[index]):
            if guess[index] == secret[index]: 
                resulting_emoji += GREEN_BOX
            else:
                if contains_char(secret, guess[index]) is True: 
                    resulting_emoji += YELLOW_BOX
        else: 
            resulting_emoji += WHITE_BOX 
        index = index + 1
        
    return resulting_emoji 


def input_guess(length: int) -> str: 
    """Given an integer, prompts user for guess of an expected lesngth.""" 
    guess = str(input(f"Enter a {length} character word: "))
    while len(guess) != length: 
        guess = str(input(f"That wasn't {length} chars! Try again: "))
    return guess 

                
def main() -> None: 
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    resulting_emoji: str = ""
    length: int = len(secret)
    turn: int = 1
    while (turn <= 6) and (resulting_emoji != GREEN_BOX * length): 
        print(f"=== Turn {turn}/6 ===")
        resulting_emoji = emojified(input_guess(length), secret)
        print(resulting_emoji)
        if resulting_emoji == GREEN_BOX * length: 
            print(f"You won in {turn}/6 turns!")
        turn = turn + 1
    if turn > 6: 
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()