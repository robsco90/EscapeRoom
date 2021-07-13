


## The Escape room is a riddle based game, if you answer three questions in a row correctly, you win and escape. If you answer four questions in a row incorrectly you lose and are sent to a locker room to clean toe jam for a month. Best of luck to you!

# Functions

def start_room():
    start_room_options = ["1","2","3"]
    user_choice =""
    while user_choice not in start_room_options:
        print("\n" * 10)
        print("You wake up in a dark room on a brown leather couch, you're certain how you got there.")
        print("There must have been one too many Martinis. You look around the room that appears to be an office.")
        print("There is a large mahogany desk and leather chair. Bookshelves line the the walls opposite one another.")
        print("There is only one door in the room. You happen to notice an envelope lying on the desk.")
        print("As you decide what to do next you hear a monotone robotic voice coming from some unknown source")
        print("'You have 5 minutes to leave the room before the poison gas is dispersed into the room'")
        print("1: Do you want to open the envelope?")
        print("2: Do you want to try the only door in the room?")
        print("3: Do you want to just sit there?")
        user_choice = str(input("Enter option number: "))
        #print("You have selected " + user_choice)
        if user_choice == start_room_options[0]:
            blue_room()
        elif user_choice == start_room_options[1]:
            red_room()
        elif user_choice == start_room_options[2]:
            green_room()

def blue_room():
    blue_room_options = ["1", "2", "3"]
    user_choice = ""
    while user_choice not in blue_room_options:
        print("\n" * 10)
        str="--> You have entered the Blue Room"
        print("Opening the envelope, you read the following question")
        print("The your shoes begin to get wet as you notice water is coming through the floor")
        print("What Goes Through Towns And Over Hills And Never Moves?")
        print("1: A Cloud")
        print("2: A Road")
        print("3: The Wind")
        user_choice = str
        print("You have selected " + user_choice)
        if user_choice == blue_room_options[0]:
            yellow_room: object
            yellow_room()
        elif user_choice == blue_room_options[1]:
            red_room()
        elif user_choice == blue_room_options[2]:
            green_room: object
            green_room()

def red_room() -> object:
    red_room_options: list[str] = ["1", "2", "3"]
    user_choice = ""
    while user_choice not in red_room_options:
        str= "--> You have entered the Red Room"
        print("The voice tells you to locate a book of poems by Robert Frost")
        print("Opening the book reveals another note falling out")
        print("You unfold th1e note, and read the question.")
        print("The voice reminds you that time is running out and informs you that you have approximately three minutes remain.")
        print("The room has gotten hotter and you feel perspiration running down the back of your shirt and down your temple.")
        print("You peer at the door and notice there is a keypad above the door knob.")
        print("What is the answer to the ultimate question of life, the universe and everything?")
        print("1: 51")
        print("2: 78")
        print("3: 42")
        print("You have selected " + user_choice)
        if user_choice == red_room_options[0]:
            yellow_room()
        elif user_choice == red_room_options[1]:
            orange_room()
        elif user_choice == red_room_options[2]:
            green_room()

def green_room() -> object:
    green_room_options = ["1", "2", "3"]
    user_choice = ""
    while user_choice not in green_room_options:
        print("\n" * 10)
        str="--> You have entered the Green Room"
        print(str)
        print("The voice breaks your reverie and says hitchhiking ain't what it used to be and sighs.")
        print("The voice recommends the you take a look at the book by Douglas Adams.")
        print("You pull down a worn and well read copy of the Hitchhiker's Guide to the Galaxy")
        print("The room begins to rotate it feels like the rotor ride at the carnival.")
        print("A postcard was being used as a bookmark, you pull it out to take a closer look.")
        print("The front has a picture of the Milky Way, the back has a handwritten note")
        print(" that says you will need the first and last numbers for going on a Space Odyssey with HAL.")
        print("1: 2001")
        print("2: 1984")
        print("3: 1776")
        if user_choice == green_room_options[3]:
            yellow_room()
        elif user_choice == green_room_options[4]:
            orange_room()
        elif user_choice == green_room_options[5]:
            violet_room: object
            violet_room()

def yellow_room():
    yellow_room_options: list[str] = ["1", "2", "3"]
    user_choice = ""
    str: str="--> You have entered the Yellow Room"
    print(str)
    print("Strange laughter fills the room as teleport in.")
    print("You appear to be in a locker room")
    print("You will be trapped in here forever")
    print("Riddle me this!")
    print("I help you from head to toe. The more I work, the smaller I grow. What am I?")
    print("1: Soap")
    print("2: Donut")
    print("3: Pencil")
    if user_choice == red_room_options[3]:
        violet_room: object
        violet_room()
    elif user_choice == red_room_options[4]:
        orange_room()
    elif user_choice == red_room_options[5]:
        green_room()

def orange_room():
    orange_room_options = ["1", "2", "3"]
    user_choice = ""
    while user_choice not in orange_room_options:
        print("\n" * 10)
        str="--> You have entered the Orange Room"
        print(str)
        print("Teleporting into the room with the orange glow, the room is a kitchenette.")
        print("The walls of the room seem to be a little closer than you observed a moment ago.")
        print("You feel the kitchen table bump your hip")
        print("The voice asks What color is your blood when it’s inside your body?")
        print("We'll find out soon when you're squeezed like an orange!")
        print("1: Blue")
        print("2: White")
        print("3: Red")
        if user_choice == red_room_options[3]:
            blue_room()
        elif user_choice == red_room_options[4]:
            orange_room()
        elif user_choice == red_room_options[5]:
            red_room()

def violet_room():
    violet_room_options = ["1", "2", "3"]
    user_choice = ""
    while user_choice not in violet_room_options:
        print("\n" * 10)
        str="--> You have entered the Violet Room"
        print(str)
        print("As you enter the room the floor begins to shake, dishes fall out of the china cabinet")
        print("The Shake, Shake, Shake Senora song begins to play, the floor rumbles harder and faster.")
        print('What is the name of which the name of the animal means river horse?')
        print("1: Wildebeast")
        print("2: Hippopotamus")
        print("3: Zebra")
        if user_choice == red_room_options[3]:
            red_room: object
            red_room()
        elif user_choice == red_room_options[4]:
            yellow_room()
        elif user_choice == red_room_options[5]:
            green_room()

# Main Program
start_room()

## Define how a player can win
if user_choice == 3> points
    Correct = 1 point
print("Congratulations! You Win!")

## Define how a player can lose
if user_choice == 4> points, then exit
    Wrong: object = - 1 point
print("Sorry! You Lose!")
