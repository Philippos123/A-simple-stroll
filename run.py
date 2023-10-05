def main():
    introduction()
    start_game()
    start_stroll()
    forest_tail()
    city_tail()
    home()
    death()


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
    username=""

def start_game():
    username = input("Enter Your Name:")
    if username.isalpha():
        print("______________________________\n")
        print(f"Welcome {username}, you are about to enter go out on a new adventure! I wish you all the luck!.... You probobly need it")
        start_stroll()
    else:
        print("\nIm sorry, you need to use only letters in your username, try again")
        

def start_stroll():
    print("You just woke up, the clock is 11:00 am, you woke up a bit late becuse you were talking to a friend the entire night.")
    print("The sun is shining and you decide that you want to take a stroll, so you jump in to the shower, put some cloths on and walks out from your house")
    print("You close the dorr behind you (You just left your safe heaven)\n")
    print("Now you have two choices")
    print("1: Go to the right, into the big and exciting city ")
    print("2: Go to the left, into the adventure full forest")
    user_choice=input("Wich path are you taking. 1 or 2? ")
    if user_choice =="1":
        city_tail()

    elif user_choice =="2":
        forest_tail()

    else:
        print("You need to enter 1 or 2 to start your adventure")
        start_stroll()

def city_tail():
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
            print("You succesfully hide the boy!")
            hide_boy()
        elif user_choice =="2":
            print("Oh no!! These three guys were criminalls and shoot you!")
            print("You are now bleeding out in the middle of the day")
            print("Better luck next time i guess!")
            death()
        elif user_choice =="3":
            print("Pff coward....")
            keep_stroll()


    


main()





