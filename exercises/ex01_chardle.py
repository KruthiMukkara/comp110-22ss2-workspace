"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730462650"

word = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters.")
    quit()
character = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Word must be a single character")
    quit()
print("Searching for " + character + " in " + word)


if character == word[0]:
    print(character + " found at index " + "0")

if character == word[1]:
    print(character + " found at index " + "1")

if character == word[2]:
    print(character + " found at index " + "2")

if character == word[3]:
    print(character + " found at index " + "3")

if character == word[4]:
    print(character + " found at index " + "4")

count = str(word.count(character))
if count == str(0):
    print("No instances of " + character + " found in " + word)
else:
    if count == str(1):
        print(count + " instance of " + character + " found in " + word)
    else:
        print(count + " instances of " + character + " found in " + word)