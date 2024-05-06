person_c = ""
person_c_g = ""
pronoun = ""

"""
The main() function is defined, which serves as the entry point for the game. 
It calls various other functions to progress through the game's story.
"""

def main():
    introduction()
    start_game()
    start_stroll(username)
    forest_tail()
    city_tail()
    home()
    death()
    hide_boy()
    coffeplace()


"""
The death() function is called when the player dies in the game.
It allows the player to choose whether to play again or quit the game.
"""
def death():
    print("Welcome to the afterlife!")
    user_choice=input("would you like to play again? press y or press n for leaving:")
    while True:
        if user_choice =="y":
            main()
        elif user_choice =="n":
            quit()


"""
The introduction() function provides an introductory message about the game's premise.
"""

def introduction():
    """
    Introduction about the game and what will happen 
    """

    print("Welcome my fellow friend to the 'A Simple Stroll game' where you will be playing.\n")
    print("____________________________________________________________________________________")
    print("\nYou will leave your safe heaven to take a stroll in the big and scary world.")
    print("Are you going to make new friends? Enjoy the stroll? Or never come home again?!")
    print("Every outcome will depend on your choices while you take your stroll.")
    
"""
The start_game() function prompts the player to enter their username and validates it to ensure it contains only letters.
If the username is valid, it proceeds with the game.
"""
def start_game():
    username = input("Enter Your Name:")
    while True:
        if username.isalpha():
            print("______________________________\n")
            print(f"Welcome {username}, you are about to enter on a new adventure! I wish you all the luck!.... You probobly need it\n")
            start_stroll(username)
            break
        else:
            print("\nIm sorry, you need to use only letters in your username, try again")
            start_game()
        
"""
The start_stroll(username) function describes the beginning of the game when the player decides to take a stroll.
It presents the player with a choice to go to the city or the forest.
"""
def start_stroll(username):
    print("\nYou just woke up, the clock is 11:00 am, you woke up a bit late becuse you were talking to a friend the entire night.")
    print("The sun is shining and you decide that you want to take a stroll, so you jump in to the shower, put some cloths on and walks out from your house")
    print("You close the dorr behind you (You just left your safe heaven)\n")
    print("Now you have two choices")
    print("1: Go to the right, into the big and exciting city ")
    print("2: Go to the left, into the adventure full forest")
    user_choice=input("Wich path are you taking. 1 or 2?\n")
    if user_choice =="1":
        city_tail(username)

    elif user_choice =="2":
        forest_tail()

    else:
        print("You need to enter 1 or 2 to start your adventure")
        start_stroll(username)

"""
Start City stroll
"""
def city_tail(username):
    print("\nYou took the right turn on your way to the exicting city!\n")
    print("......\n")
    print("\n10 minutes later")
    print("You walk around in the city and notice a young boy is running with a bag in his hands,")
    print("You see three huge guys running after him screaming 'COME BACK HERE BOY!'\n")
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
            print("\nOh no!! These three guys were criminalls and shoot you!")
            print("You are now bleeding out in the middle of the day")
            print("Better luck next time i guess!\n")
            death()
        elif user_choice =="3":
            print("Pff coward....\n")
            home()

        else:
            print("You can only press 1,2,3")
            city_tail(username)
"""
The hide_boy(username) function is called if the player chooses to hide the boy. 
It continues the story and introduces a character named person_c who interacts with the player.
"""
def hide_boy(username):
    print("\nThe boy: Thank you for saving me! What´s your name?")
    print(f"Is that so? My name is {username}")
    print(f"The boy: Thanks {username}! They were going to kill me!")
    print("You take a look at the bag and decide to not ask about it.")
    print("The boy takes of and runs into an allay nearby. Everything was back to normal again.")
    print("But your heroic act didnt go unnotice....\n")
    print("__________________________________________________________")
    print("A very beautifull person comes up to you.")
    print("WOW! You are so brave! You saves that little boy from those thugs!")
    print("You feel a bit embarce but you enjoy the compliments.")
    print("You shake the persons hand and say")
    print(f"Hello my names is {username} what´s yours?\n")
    person_c_g = input("Is this a women or man? ")
    person_c = input(f"What is this {person_c_g}´s name?")
    while True:
        if person_c_g == "man":
            pronoun = "he"
            print(f"\nWell hello {person_c} my name is {username}")
            print("Yeah these guys was scary but i wasn´t afraid..")
            coffe_tail(person_c, person_c_g, username, pronoun)
            
        elif person_c_g == "women":
            pronoun = "she"
            print(f"\nWell hello {person_c} my name is {username}")
            print("Yeah these guys was scary but i wasn´t afraid..")
            coffe_tail(person_c, person_c_g, username, pronoun)
            
            
        else:
            print("Im sorry make a choice between man or women.")
            hide_boy(username)


   
    
    

"""
The coffe_tail() function continues the story from the coffee shop, where the player can choose to follow person_c or not.
"""
def coffe_tail(person_c, person_c_g, username, pronoun):
    print(f"\n{person_c}: Come on {username} let´s go and take a coffee? I know a place?")
    
    while True:
        follow = input(f"would you like to follow {person_c}? y/n\n")
        if follow =="y":
            coffeplace (person_c, person_c_g, username, pronoun)
        elif follow =="n":
            home()
        else:
            print("Im sorry you need to answer with simple y or n to keep playing")

"""
The coffeplace() function describes the coffee shop scenario and the player's choices.
"""    
def coffeplace(person_c, person_c_g, username, pronoun):
    print(f"\n{person_c}: Oh im so glad you want to take a coffe!")
    print(f"{person_c}: I know a place walking distance from the city! let´s go!\n")
    print(".............")
    print("\n20 minutes later")
    print(f"You are tired of walkning but {person_c} told you it was 5 minutes left.")
    print(f"You notice that {pronoun} has scars on the arms and looks paranoid, always looking around.")
    print(f"You dont think much about it, on the other hand you notice that {pronoun} taking you to a bit suspicious place by the forst.\n")
    cabin_tail(person_c, username, pronoun)

"""
The cabin_tail() function is called when the player reaches a cabin and encounters a dangerous situation.
"""
def cabin_tail(person_c, username, pronoun):
    print(f"\n{pronoun} points at a small old red cabin and say. 'We are here! come on {username}'")
    print(f"You feel a bit sceptical to this, beacue you heard of a young girl and an middle age {person_c_g} disapeard arond here somwehere")
    print("All of a sudden, you notice someone standing behind the trees in the woods close by the cabin. ")
    print(f" {person_c} pushes you behind a wall and whispers in your ear. 'Listen to me or die inside this cabin...'")
    print("You are the only one who can save us.")
    print("You fell the goosbumps crawl up to your shoulders.")
    print("You have two choices.\n")
    print(f"1. Ask {person_c} what´s happening")
    print(f"2. Just follow {person_c} and lay low")
    user_choice = input("What are you going to do?")
    while True:
        if user_choice =="1":
            print("Why? What´s going on here?!")
            inside_cabin(person_c, username, pronoun)
        elif user_choice =="2":
            print("Hmm what´s that all about?")
            inside_cabin(person_c, username, pronoun)
        else:
            print("You need to pick 1 or 2")
            cabin_tail(person_c, username, pronoun)

"""
The inside_cabin() function continues the story inside the cabin, revealing more details about the situation.
"""
def inside_cabin(person_c, username, pronoun):
    print(f"\nBoth of you walk inside the cabin and {pronoun} whispers in your ear")
    print(f"{person_c}: Did you notice the person behind the trees?")
    print("Yes? What about it?")
    print(f"{person_c}: You know that two people got kidnapped a couple of weeks ago?")
    print("Yeah?.......\n")
    print(f"{person_c}: That was me and a little girl.")
    print("Why did you bring me here then?!")
    print(f"{person_c}: I saw your heroic act and i hope that you could save us....")
    print(f"{person_c}: The man that kidnapped us is mr.Jansson")
    print("But wait?! That is my neighbour?!")
    print(f"{person_c}: He want´s us to charm people here and kill them... He´s a... eh cannibal")
    print("Wait what?! Is he going to eat me?!")
    print(f"{person_c}: He forces us to eat his 'catch' and i can´t handle it!!\n")
    print("You have three choices now...")
    print(f"1. Tell {person_c} ofcourse im going to help you!")
    print(f"2. Tell {person_c} You have to deal with this yourself!")
    print("3. Run for your life!")
    user_choice = input("What´s your choice?")
    while True:
        if user_choice=="1":
            print(f"{person_c} Oh thank you {username}!")
            final_act(person_c, username, pronoun)
        elif user_choice=="2":
            print(f"{person_c} You have to, you have no other choice!")
            print("Nope, i am going to call the police!")
            final_act2(person_c, username, pronoun)
        elif user_choice=="3":
            print(f"\nGood bye! {person_c} im out of here!")
            print("You slam up the dorr right in the face of Mr.Jansson and escapes")
            print("You feel your legs shut down but you can´t stop!")
            print("You run home and close the dorr")
            print("several hours later.....")
            print("You hear someone that´s ouside your front dorr")
            print("knock knock knock...")
            print("You sit in your couch silent and you hear someone say")
            print(f"Hello {username} it´s Mr.Jansson, I am coming for you....\n")
            death()
        else:
            print("Im sorry you need to answer with 1,2 or 3 to keep playing")
            inside_cabin('person_c', 'username', 'pronoun')



"""
The final_act() function presents the player with choices on how to deal with the situation inside the cabin.
"""
def final_act(person_c, username, pronoun):
    print("\nDOOK DOOK DOOK")
    print(f"{person_c} He is here, go and hide!!")
    print("Now you have three choices!")
    print("1. Hide in the wardrobe")
    print("2. Run for the kitchen knife and defend yourself!")
    print("3. Hide under the bed")
    user_choice =input("What´s your chocie?")
    while True:
        if user_choice=="1":
            print("I will go and hide in the wardrobe!")
            final_act_wardrobe(person_c, username, pronoun)
        elif user_choice=="2":
            print("\nYou start the run for the kitchen knife!")
            print(f"The dorrs open and mr.Jansson says 'Good job {person_c} we are going to eat good tonight'")
            print(f"You start to shake and you see how scared {person_c} looks, you look back at mr.Jansson")
            print("DONK!\n")
            print("You wake up strapped to a bloody kithen table ")
            print(f"Mr.Jansson comes up close to your face and says 'Sleep well {username}'\n")
            death()
        elif user_choice=="3":
            print("\nYou run and slide under the bed")
            print("Mr.jansson enters the house")
            print(f"Mr.Jansson: {person_c}!! Where is {username}?")
            print(f"{person_c} standing there quiet")
            print("Mr.Jansson: {person_c} if you dont tell me in three seconds, you will be served as dinner tonight...")
            print(f"{person_c}: I am so sorry {username}....")
            print(f"{person_c}: He´s under the bed")
            print(f"Mr.Jansson: Well well... Hello there {username}")
            print("DONK!\n")
            print("You wake up strapped to a bloody kithen table ")
            print(f"Mr.Jansson comes up close to your face and says 'Sleep well {username}'\n")
            death()
        else:
            print("Im sorry you need to answer with 1,2 or 3 to keep playing")
            final_act(person_c, username, pronoun)


"""
The final_act_wardrobe function tell the player the story if they choose the wardrobe to hide, and win the game
"""
def final_act_wardrobe(person_c, username, pronoun):
    print(f"\n{person_c}: Oh hello Mr.Jansson...")
    print(f"Mr.Jansson: Hello {person_c}. Where is {username}?")
    print(f"{person_c}: He´s down in the basement! You should go down there!")
    print("You see that mr:jansson walks down to the basement and you notice a shotgun beside you.")
    print("You pick up the shotgun load and walks out of the wardrobe")
    print(f"{person_c} notice the gun and says")
    print(f"{person_c}: Mr.Jansson help me!! ")
    print("Mr.Jansson runs up and boom!")
    print(f"Mr.Jansson falls down and start dying, you chooses to take {person_c}´s hand and find the girl outside, so you decide to take her aswell\n")
    congrat(username)

"""
final_aces(): This function represents the final part of the game where the player faces a life-or-death situation. 
The player is given three choices: hiding in the wardrobe, running for a kitchen knife, or hiding under the bed. 
Depending on their choice, different outcomes occur, leading to either death or survival.
"""
def final_act2(person_c, username, pronoun):
    print(" DOOK DOOK DOOK")
    print(f"{person_c}: He is here, go and hide!!")
    print("Now you have three choices!")
    print("1. Hide in the wardrobe")
    print("2. Run for the kitchen knife and defend yourself!")
    print("3. Hide under the bed")
    user_choice =input("What´s your chocie?")
    while True:
        if user_choice=="1":
            print("\nI will go and hide in the wardrobe!")
            print("Mr.Jansson walks in to the house")
            print(f"Mr.Jansson: Where is {username} hiding?")
            print(f"You notice that {person_c} start to walk towards the wardrobe")
            print(f"{person_c}: Im sorry {username}... But i can´t trust you...")
            print("Mr.Jansson open the wardrobe, you notice the gun but dont have time enough to load it...")
            print(f"Well well well... hello {username}\n")
            print("Donk!")
            death()
        elif user_choice=="2":
            print("\nYou start the run for the kitchen knife!")
            print(f"The dorrs open and mr.Jansson says 'Good job {person_c} we are going to eat good tonight'")
            print(f"You start to shake and you see how scared {person_c} looks, you look back at mr.Jansson")
            print("DONK!\n")
            print("You wake up strapped to a bloody kithen table ")
            print(f"Mr.Jansson comes up close to your face and says 'Sleep well {username}' \n")
            death()
        elif user_choice=="3":
            print("You run and slide under the bed")
            print("Mr.jansson enters the house")
            print(f"Mr.Jansson: {person_c}!! Where is {username}?")
            print(f"{person_c} standing there quiet")
            print(f"Mr.Jansson: {person_c} if you dont tell me in three seconds, you will be served as dinner tonight...")
            print(f"{person_c}: I am so sorry {username}....")
            print(f"{person_c}: He´s under the bed")
            print(f"Mr.Jansson: Well well... Hello there {username}")
            print("DONK!\n")
            print("You wake up strapped to a bloody kithen table ")
            print(f"Mr.Jansson comes up close to your face and says 'Sleep well {username} ' ")
            death()
        else:
            print("Im sorry you need to answer with 1,2 or 3 to keep playing")
            final_act2(person_c, username, pronoun)


"""
congrat(username): This function is called when the player survives the game. 
It congratulates the player and asks if they want to play again. 
If the player chooses to play again, it calls the start_game() function (which is not defined in the provided code).
"""
def congrat(username):
    print(f"Congrats! {username} you survived the stroll!")
    user_choice=input("Would you like to play again? y/n:")
    while True:
        if user_choice=="y":
            start_game()
        elif user_choice=="n":
            quit()
"""
forest_tail(): This function sets up the initial scenario where the player is on a stroll in the woods. 
They hear a child crying and are given the choice to find the child or ignore the sound.
"""
def forest_tail():
    print("\nYou are excited! You are about to go on a excited stroll in the woods")
    print("10 minutes later......")
    print("You are starting to walk deeper and deeper inside the woods")
    print("You start to remember a artical you saw couple of weeks ago about two girls that went missing inside these woods")
    print("You start to hear i child crying")
    print("You have 2 options now...")
    print("1. Find the girl")
    print("2. Ignore the child and move on with your stroll\n")
    user_choice=input("What are you going to do?")
    while True:
        if user_choice=="1":
            print("You start the search for the girl")
            find_girl()
        elif user_choice=="2":
            print("You ignore the sound and walks home")
            home()

"""
find_girl(): This function is called when the player chooses to find the child. 
They encounter a girl named Molly and are given choices that lead to different outcomes.
"""
def find_girl():
    print("\nYou walk around in the woods for 10 minutes untill you find a little girl untill a old tree.")
    print("You ask the girl if she´s one of girls that went missing")
    print("She reply with 'Hihihi, nom nom...'")
    print("You ask the girl what her name is and she reply: Molly")
    print("Okey Molly, let´s take you home?")
    print("Molly:Okey! My father will be so happy to see that i have brought a friend!")
    print("Molly whisper for her self....'Haha my belly to'")
    print(".............")
    print("\n20 minutes later")
    print("You are tired of walkning but Molly told you it was 5 minutes left.")
    print("You notice that she has scars on the arms and looks paranoid, always looking around.")
    print("You dont think much about it, on the other hand you notice that she taking you to a bit suspicious place by the forst.")
    print("You see a shadow following you to a red old cabin outside the forest.")
    print("Molly asks you 'Do you wanna meet my father? My sibling is out working right now so it will be just us'")
    print("You have 2 choices\n")
    print("1. Follow Molly inside")
    print("2. Go home")
    user_choice=input("What are you going to do?")
    while True:
        if user_choice=="1":
            print("You will follow Molly")
            girl_cabin()
        elif user_choice=="2":
            print("You got a creepy feeling and went home")
            home()
        else:
            print("You have to choose 1 or 2")
"""
girl_cabin(): This function is called when the player chooses to follow Molly inside her cabin. 
It presents the player with a choice to drink tea or not, which leads to different outcomes.
"""
def girl_cabin():
    print("You walk inside the cabin and notice a gun and some buther knifes")
    print("Molly: My father will come soon, drink this tea in the meantime.")
    user_choice=input("Are you drinking the tea? y/n ")
    while True:
        if user_choice=="y":
            print("I will have some!")
            soon_death()
        elif user_choice=="n":
            print("No thanks im not thirsty")
            fight_for_life()
        else:
            print("You need to choose y or n to continue playing")

"""
soon_death(): This function is called if the player chooses to drink the tea. 
It leads to a scenario where the player falls unconscious and faces a grim fate.
"""
def soon_death():
    print("\nYou drink up all the tea Molly gave you, after a couple of minutes you feel dizzy and tired..")
    print("Molly: Is everything alright with you?")
    print("I got really dizzy and almost feel like fainting")
    print("Molly goes: Goood... Father will give me a snack hihihi.")
    print("You dont understand what´s happening and falls to the ground\n")
    death()

"""
fight_for_life(): This function is called if the player refuses to drink the tea. 
It involves a confrontation with Molly, and the player must make choices to survive.
"""
def fight_for_life():
    print("\nMolly got upseat that you didnt drink the tea.")
    print("You start to get really weird vibes from her.")
    print("You notice that she´s very thin and pale\n")
    print("Well well Molly i will be going now send your father my regards...")
    print("Molly: NO!!! Dont go! YOU NEED TO STAY! YOU WILL MAKE MY BELLY STOP CRY")
    print("You got scared, you turn around and see Molly standing with a knife")
    print("Are you going for the gun or flee from a little girl?")
    print("1. Take the gun and defend yourself")
    print("2. Run for your life!\n")
    user_choice=input("What´s your decision")
    while True:
        if user_choice=="1":
            print("You are going for the gun!")
            gunfight(username)
        elif user_choice=="2":
            print("Haha are you really running from a little girl?")
            home_safe(username)
        else:
            print("You have to choose 1 or 2")
"""
gunfight(username): This function is called when the player decides to go for the gun. 
The outcome depends on the player's choices during the gunfight.
"""
def gunfight(username):
    print("\nYou run for the gun and loads it.")
    print("Molly starts to scream 'AHHHHHHHH'")
    print("You notice that something is wierd")
    print("The dorr opens up and your neighbour comes in.")
    print("neighbour: What´s going on here! I heard screams!")
    print("Ah Mr.Jansson! Please help me! She´s insane!!")
    user_choice=input("Are you going to trust Mr.Jansson? y/n \n")
    while True:
        if user_choice=="y":
            print("\nMr.Jansson: I will help you! Just walk slowly towards me and aim at the girl...")
            print("DONK")
            print("Mr.Jansson was her father...\n")
            death()
        elif user_choice=="n":
            print("\nWhat where you doing out here Mr:jansson?")
            print("Mr.Jansson: Just taking stroll")
            print("Molly then screams: FATHER I AM HUNGRY!!")
            print("You turn your eyes to Mr.Jansson")
            print("Mr.Jansson: Im sorry my friend but you heard her.... She´s hungry")
            print("You aim your gun at Mr.Jansson and pulls the trigger twice and then turn at Molly and fires once.")
            print("You throw the gun and start´s running home and remember that Molly mention a sister...")
            print("You open your dorr and enters your safe heaven. Calls the cops and tell them about everything")
            print("And the police officer answers: Did you kill my familly?\n")
            congrat(username)
        else:
            print("Im sorry you need to answer with y/n keep playing")
            gunfight()

"""
home_safe(username): This function is called if the player decides to run away from Molly. 
It describes the player's return home and the discovery of disturbing news about Mr. Jansson, the neighbor.
"""
def home_safe(username):
    print("\nYou keep walkning home and walks in to your safe heaven.")
    print("Everything is normal, but you notice in the morning paper that a young man have been missing for 2 days.")
    print("Around the same place as the old cabin.")
    print("Three months later.....")
    print("Newspapper: This morning did the police finally found the girls that went missing four months ago. At a man calld Mr.Jansson summer cabin")
    print("Informations tells us that under these four months they have been kidnapping and eating travelers")
    print("You notice the name 'Mr.Jansson'.... WAIT!")
    print("That´s my neigbour!\n")
    congrat(username)

"""
home(): This function is called if the player chooses to ignore the child's cries at the beginning. 
It offers a simple ending and asks if the player wants to play again.
"""
def home():
    print("\nYou ignore everything.... You are no fun... :( ")
    print("You did on the other hand enjoy a simple stroll")
    user_choice=input("Would you like to play again? y/n\n")
    while True:
        if user_choice=="y":
            main()
        elif user_choice=="n":
            quit
        else:
            break
            print("press y or n")



main()        










