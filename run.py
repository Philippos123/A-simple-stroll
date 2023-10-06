username = ""
person_c = ""
person_c_g = ""

def main():
    introduction()
    start_game()
    start_stroll()
    forest_tail()
    city_tail()
    home()
    death()
    hide_boy()


def death():
    print("Welcome to the afterlife!")
    user_choice=input("would you like to play again? press y or press n for leaving:")
    while True:
        if user_choice =="y":
            main()
        elif user_choice =="n":
            quit()


def introduction():
    """
    Introduction about the game and what will happen 
    """

    print("Welcome my fellow friend to the 'A Simple Stroll game' where you will be playing.\n")
    print("____________________________________________________________________________________")
    print("\nYou will leave your safe heaven to take a stroll in the big and scary world.")
    print("Are you going to make new friends? Enjoy the stoll? Or never come home again?!")
    print("Every outcome will depend on your choices while you take your stroll.")
    

def start_game():
    username = input("Enter Your Name:")
    if username.isalpha():
        print("______________________________\n")
        print(f"Welcome {username}, you are about to enter go out on a new adventure! I wish you all the luck!.... You probobly need it")
        start_stroll(username)
    else:
        print("\nIm sorry, you need to use only letters in your username, try again")
        

def start_stroll(username):
    print("You just woke up, the clock is 11:00 am, you woke up a bit late becuse you were talking to a friend the entire night.")
    print("The sun is shining and you decide that you want to take a stroll, so you jump in to the shower, put some cloths on and walks out from your house")
    print("You close the dorr behind you (You just left your safe heaven)\n")
    print("Now you have two choices")
    print("1: Go to the right, into the big and exciting city ")
    print("2: Go to the left, into the adventure full forest")
    user_choice=input("Wich path are you taking. 1 or 2? ")
    if user_choice =="1":
        city_tail(username)

    elif user_choice =="2":
        forest_tail()

    else:
        print("You need to enter 1 or 2 to start your adventure")
        start_stroll(username)

def city_tail(username):
    print("You took the right turn and on your way to the exicting city!\n")
    print("......\n")
    print("\n10 minutes later")
    print("You walk around in the city and notice a young boy is running with a bag in his hands,")
    print("You see three huge guys running after him screaming 'COME BACK HERE BOY!'")
    print("You have three choices now")
    print("1: Hide the boy behind you")
    print("2: Fight of the guys")
    print("3: Ignore everyting and fake an importent phone call?")
    while True:
        user_choice =input("What´s your choice? 1, 2, 3?")
        if user_choice =="1":
            print("You succesfully hide the boy\n")
            hide_boy(username)
        elif user_choice =="2":
            print("Oh no!! These three guys were criminalls and shoot you!")
            print("You are now bleeding out in the middle of the day")
            print("Better luck next time i guess!")
            death()
        elif user_choice =="3":
            print("Pff coward....")
            home()

def hide_boy(username):
    print("The boy: Thank you for saving me! What´s your name?")
    print(f"Is that so? My name is {username}")
    print(f"The boy: Thanks {username}! They were going to kill me!")
    print("You take a look at the bag and decide to not ask about it.")
    print("The boy takes of and runs into an allay nearby. Everything was back to normal again.")
    print("But your heroic act didnt go unnotice....\n")
    print("A very beautifull person comes up to you.")
    print("WOW! You are so brave! You saves that little boy from those thugs!")
    print("You feel a bit embarce but you enjoy the compliments.")
    print("You shake the persons hand and say")
    print(f"Hello my names is {username} what´s yours?")
    person_c_g = input("Is this a women or man? man or woman ")
    person_c = input (f"What is the {person_c_g}s name?")
    while True:
        if person_c_g == "man":
            pronoun = "he"
            print(f"Well hello {person_c} my name is {username}")
            print("Yeah these guys was scary but i wasn´t afraid..")
            coffe_tail(person_c, person_c_g, username)
        elif person_c_g == "woman":
            print(f"Hello {person_c} my name is {username}")
            print("Yeah these guys was scary but i had to save the boy!")
            pronoun = "she"
            coffe_tail(person_c, person_c_g, username)
        else:
            print("Im sorry make a choice between man or women.")


def coffe_tail(person_c, person_c_g, username):
    print(f"{person_c}: Come on {username} let´s go and take a coffee? I know a place?")
    follow = input(f"would you like to follow {person_c}? y/n")
    while True:
        if follow =="y":
            coffeplace(person_c, person_c_g, username)
        elif follow =="n":
            home()
        else:
            print("Im sorry you need to answer with simple y or n to keep playing")
    
def coffeplace(person_c, person_c_g, username):
    print(f"{person_c}: Oh im so glad you want to take a coffe!")
    print(f"{person_c}: I know a place walking distance from the city! let´s go!\n")
    print(".............")
    print("\n20 minutes later")
    print(f"You are tired of walkning but {person_c} told you it was 5 minutes left.")
    print(f"You notice that {person_c_g} has scars on the arms and looks paranoid, always looking around.")
    print("You dont think much about it, on the other hand you notice that she´s taking you to a bit suspicious place by the forst.")
    
coffeplace(person_c, person_c_g, username)
        


    








