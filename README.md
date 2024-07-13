# Welcome to A Simple Stroll Game!

![AMIRESPONSIV](images/jag%20responsiv.png)

## What is a simple stroll?
A Simple Stroll is a game for both females and males aged between 16-22 years. The goal of the game is to give the player an exciting and goosebump-inducing experience. It’s a horror game where you go for a simple stroll, and things turn south very quickly. There is an old cabin by the woods with a child crying. What could go wrong?


## How do you play? 
You will follow the story of "A Simple Stroll" and reach points where you need to make decisions. Depending on your answers, you will either have a simple stroll or be hunted by a cannibal.

The player will be able to give names and genders to the characters they meet in the story. There will be 2-3 different paths for the player to choose from.

The player will be able to pick 1, 2, or 3, and y/n depending on the situation.


# Project goal

### For the user
- To play a puzzle game where the goal is to survive the stroll.
- To understand the instructions and know how to play.

### For the admin
- To provide players with clear instructions.
- To create a game without errors.

## User Experience

### Target audience
There are no specific users for the site, but the game would suit young users who are in search for a thrill. 
It can alose be played by older users, it all depends on there personal intrest. 


### User requirements
* A game that is understandable and works as expected.
* A game that passes all the variables and functions works as expected. 
* User can quit the game when they want.
* User can continue playing even if they win. 


### User Manual
Click the dropdown to view the user manual:
<details>
<summary>User Manual</summary>

### Main menu
The user will be prompted to enter a player name, and will then be directed to the main menu.
There are 2 options in the menu:
1. Go right into the big and exciting city
2. Go to the left into the adventure full forest. 


### Reading instructions
The user is able to see the instructions to the game in beginning of every new round. 
 <details><summary>HOW TO PLAY </summary>
You will start the game by entering your name and then
you will get choices to make on your stroll by
pressing y,n,1,2 or 3 depening on the situation"</details>

### Quitting the game
If x is selected in the main menu (or at any time during the levels):
* User will be asked if they're sure they want to quit (type y or n, press enter).
* User prompted for feedback (type y or n, press enter).
* User thanked for playing and reminded how to restart the game.

### Playing the game
Once the game is started, the user must complete 10 levels, and successfully answer maths questions between each level. If the user makes 3 mistakes, the game ends and the user must restart or quit.

#### Level navigation
The player must move the character (represented by the letter 'A') to the exit of each level/maze.

In order to navigate through levels of the dungeon, the user must type their moves in the format:
DIRECTION,STEPS where:
* DIRECTION is U, D, L, R (up, down, left, right).
* STEPS is a whole number between 1 and 9.
#### Examples
* Entering U,3 in the terminal would move the character up by 3 steps.
* Entering R,1 in the terminal would move the character right by 1 step.

#### Beware
* If the user navigates into a level wall, the character will lose 1 life.
* If the user tries to navigate out of bounds (i.e. enters a number that would move the character outside the level), the character will lose 1 life AND the level will be reset!
* If the user completes a level, but fails to answer the subsequent maths question correctly, the character will lose 1 life and the player will miss out on bonus points. 

</details><br>


## Why would you want to play this game? 

A Simple Stroll is a game where you, as the player, control the storyline. You control the choices you make and the people you meet along the way. The game is nerve-wracking, making it the perfect "late-night game" when you are alone on a Saturday night in front of your computer.


# Functions
### Input
The player will be able to input their character's name, which will follow throughout the entire story. The player will also be able to input the gender and name of characters they meet during the stroll. If the player meets a woman, the story will use the pronoun "she," and if it's a man, it will use "he."

## Attributes 
- Person_c stands for the person's name.
- Person_c_g stands for gender.
- Pronun stands for pronouns. 
- Username stands for the player´s name.

### Events
There are a lot of events when the player picks the exciting path. The player will always have the option to go home because that’s reality. Who would like to go for a stroll with no option to turn back for like 5 hours?
### Variables 
The people the player meets aren’t static in the game. This makes it important to pass variables further through the game. For example, the variable person_c_g will change a person the player meets from a woman to a man depending on the player's early choices, and their pronouns, of course, are stored in the pronoun variable.

# Testing 

## PEP8 
A Simple Stroll passed the PEP8 checks with no errors, as shown in the image below. The game initially had a lot of PEP8 errors, which have been resolved now. 
![PEP8](images/PEP8.png)

## Manual testing 
### Start Game 
1. Start the game by entering your name. I used an isalpha function so the user can only use letters. If you use a number, the system will loop back.
### Choose path 
1. The user can pick 1 or 2 depending on whether they want a city stroll or a forest stroll.

2. If the user inputs A or 3, nothing will happen, and they won’t be able to progress in the story until they pick 1 or 2.
### Death
1. When the player dies, they have 2 options.
2. They can pick y to play again.
3. They can also pick n to leave. 
4. If they pick y, they will go back to the start game function.
### Congratulation 
1. When the player survives the stroll, they will reach the congrats function.
2. At this point, they have 2 choices:
- Press y to play again, returning to the start game function.
- Press n to leave the game.
### Persons in the story
1. Inside the Hide Boy function, the user can choose the gender (woman or man) of the person they meet.
2. If the player chooses a woman, the story changes to use the pronoun "she."
3. We pass the pronoun, person_c, and person_c_g through the functions.
4. The player can only enter "woman" or "man," but for the name, they can choose any string.
5. If they enter an invalid value for "woman or man," they will iterate back to the choice.
## Depoloyment

I deployd this project to Heroku 

1. I logged in to Heroku
2. Created new app
3. Named my app and picked my region 
4. Then i linked the heroku app to my repo in github and loaded it. 


## Bugs 
 I found a couple of bugs where the player would input 3 when there were only 1 or 2 as options, which would create an infinite loop. Another bug was when I created else statements but didn't pass in the variable from the function, causing a crash.

## Images 

In this picture, the user has the power to create their own story by controlling who they will meet. Is it a girl or a man? Friend or foe?
![Simpel_stroll](images/simpel_stroll.JPG)

Here is another picture of the whole application. I tried to structure the text with lines and \n.
![Another_picture_of_simpel_stroll](images/Skärmbild%20(97).png)

## To the Game 
Here is the link to the game <https://a-simple-stroll-c4fc7eb42776.herokuapp.com/>


