#!/usr/bin/python3
import os

#Task 1
print("You wake up in a dark room on a brown leather couch, you're certain how you got there.")
print("'There must have been one too many Mai Tais'")
print("You look around the room that appears to be an office.")
print("There is a large mahogany desk and leather chair. Bookshelves line the the walls opposite one another.")
print("There is only one door in the room. You happen to notice an envelope lying on the desk.")
print("As you decide what to do next you hear the voice of the Waze navigation coming from some unknown source")
print("'You have 5 minutes to leave the room before the poison gas is dispersed into the room'")

# Task 1 Loop
while True:
    print("1: Do you want to open the envelope?")
    print("2: Do you want to try the only door in the room?")
    print("3: Do you want to just sit there?")
    answer = input()
    os.system("clear")
    if answer == "1":
        print("You open the envelope and read the note.", "Which appears to be a riddle")
        break
    elif answer == "2":
        print("The door is locked and will not open")
    elif answer == "3":
        print("Time is wasting and you are getting no younger!")
    else:
        print("That's not an option, try something else.")


while True:
    print("Opening the envelope, you read the following question")
    print("What Goes Through Towns And Over Hills And Never Moves?")

# Task 2
    print("1: A Cloud")
    print("2: A Road")
    print("3: The Wind")
    answer = input()
    os.system("clear")
    os.system("clear")
    if answer == "1":
        print("That is not the correct answer, try once more.")
    elif answer == "2":
        print("Correct!")
        break
    elif answer == "3":
        print("That is not the correct answer, try once more.")
    else:
        print("That's not an option, try something else.")

while True:
    print("The voice tells you to locate a book of poems by Robert Frost")
    print("Opening the book reveals another note falling out")
    break
    print("You unfold th1e note, and read the question.")
    print("The voice reminds you that time is running out and informs you that you have approximately three minutes remain.")
    print("You peer at the door and notice there is a keypad above the door knob.")
    os.system("clear")
    print("What is the answer to the ultimate question of life, the universe and everything?")
    print("1: 51")
    print("2: 42")
    print("3: ")
    answer = input()
    if answer == "1":
        print("Close, but no cigar. Try again.")
    elif answer == "2":
        print("That is not the correct answer, try once more.")
    elif answer == "3":
        print("Precisely.")
        break
    os.system("clear")
    print("The voice breaks your reverie and says hitchhiking ain't what it used to be and sighs.")
    print("The voice recommends the you take a look at the book by Douglas Adams.")
    print("You pull down a worn and well read copy of the Hitchhiker's Guide to the Galaxy")
    break
    print("A postcard was being used as a bookmark, you pull it out to take a closer look.")
    print("The front has a picture of the Milky Way, the back has a handwritten note")
    os.system("clear")
    print(" that says you will need the first and last numbers for going on a Space Odyssey with HAL.")
    print("1: 2001")
    print("2: 1984")
    print("3: 1776")
    answer = input()
    if answer == "1":
        print("Bingo.")
    elif answer == "2":
        print("Big Brother says this is not the correct response.")
        break
    elif answer == "3":
        print("Are you even trying?")
