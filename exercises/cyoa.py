"""COMP110- Create Your Own Adventure Program- Buzzfeed Quiz- Are You More Like Monica or Rachel?"""

__author__ = "730462650"

from random import randint

HAPPY: str = "\U0001F603"
SAD: str = "\U0001F622"
HOME: str = "\U0001F3D8"
GO_OUT: str = "\U0001F483"
SUN: str = "\U0001F304"
NIGHT: str = "\U0001F30C"
YUM: str = "\U0001F60B"
SWEET: str = "\U0001F366"
SAVORY: str = "\U0001F35F"
TEA: str = "\U0001F375"

points: int = 0
player: str = ""


def greet() -> None: 
    """Greets the player and asks for name."""
    global player
    print("Welcome to the 'Are You More Like Monica or Rachel?' Quiz!")
    player = str(input("What is your name?: "))
    print(f"Let's get started {player}!")

     
def customprocedure() -> None:
    """Personality quiz."""
    global player
    print(f"{player}, you have chosen the personality quiz!")
    global points
    answer = str(input("Which word would you use to describe yourself? (friendly/sassy/sensitive/proud): "))
    if answer == "friendly" or "sassy": 
        points += randint(0, 51)
    elif answer == "sensitive" or "proud": 
        points += randint(51, 101)
    answer2 = str(input(f"Would you rather go out {GO_OUT} or stay in {HOME}? (go out/stay in): "))
    if answer2 == "go out": 
        points += randint(0, 51)
    elif answer2 == "stay in": 
        points += randint(51, 101)
    answer3 = str(input(f"Are you an early bird {SUN} or night owl {NIGHT}? (early bird/night owl): "))
    if answer3 == "early bird":
        points += randint(0, 51)
    elif answer3 == "night owl": 
        points += randint(51, 101)

    
def customfunction(score: int) -> int: 
    """Food quiz."""
    global player
    print(f"{player}, you have chosen the food quiz {YUM}!")
    answer = str(input("What is your favorite meal? (dessert/breakfast/lunch/dinner): "))
    if answer == "breakfast" or "dessert": 
        score += randint(0, 51)
    elif answer == "lunch" or "dinner": 
        score += randint(51, 101)
    answer2 = str(input(f"Do you like sweet {SWEET} or savory {SAVORY} food? (sweet/savory): "))
    if answer2 == "sweet": 
        score += randint(0, 51)
    elif answer2 == "savory": 
        score += randint(51, 101)
    answer3 = str(input(f"Are you a coffee or tea person {TEA}? (coffee/tea): "))
    if answer3 == "coffee": 
        score += randint(0, 51)
    elif answer3 == "tea":
        score += randint(51, 101)
        print(score)
    return score


def main() -> None: 
    """The entrypoint of the program and the main game loop."""
    greet() 
    choice: str = ""
    global points
    while choice != "quit":
        print(f"Points: {points}")
        choice = input("Would you like to take a personality quiz, a food quiz, or quit? (food/personality/quit): ")
        if choice == "food": 
            points = customfunction(points)
        if choice == "personality":
            customprocedure()
        if points > 150: 
            print("You are more like Monica!")
        else: 
            print("You are more like Rachel!")

    
if __name__ == "__main__":
    main() 