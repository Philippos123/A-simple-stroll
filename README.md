# Welcome to A Simple Stroll Game!

![AMIRESPONSIV](images/jag%20responsiv.png)

## What is a simple stroll?
A Simple stroll is a game for both females and male with tha age between 16-22 years. The goal with game is to give the player an exciting and goosbump feeling. It´s a horror game where you are going for a simple stroll and things turn south very fast. There is a old cabin by the woods with a child crying. What could go wrong?


## How do you play? 
You will follow the story of "A Simple Stroll" where your come to a point when you need to make a decision. Depening on your answer will you have a simple stroll or being hunted by a cannibal? 

The player will be able to give the characters they meet in the story names and gender.
There will be between 2-3 diffrent paths for the player. 

The player will be able to pick 1,2 or 3 and y/n depening on the situation.


# Project goal

### For the user
- To play a puzzle game where the goal is to survive the stroll.
- To understand the instructions and understand how to play. 

### For the admin
- To provide the players with instructions. 
- To make a game where there are no errors.


## Why would you want to play this game? 

A simpel stroll is a game where you as a player controll the storyline. You controll the choices you make and the people you meet along the way. The game is nerve tickling wich makes it the perfect "late before bed game" when you sit alone a saturday night infront of your computer. 


## Functions
### Input
The player will be able to input there characters name, wich will follow throught out the entire story. 
The player will also be able to put in gender and name on characters they meet when they stroll. 
Depending on if it is a women the player meet the entire story will give her the pronoun of she, and is it a man it will be he.
- Person_c stands for the persons name 
- Person_c_g stands for gender
- Pronun stands for pronunce 
- Username stands for the player´s name
### Events
There is alot of events when the player picks the exciting path, the player will almways have a choice to go home. Beacuse that´s reality. Who would like to go for a stroll when you have no option on turning back for like 5 hours?? 
### Variables 
The people the player's meet isn't static inside the game. Wich makes it important to past the variables further through the game. For exampel the variable "person_c_g" wich will change a person they meet in the game from women to man depending on what the player choose to pick in the early stages of the game and there prounances ofcourse wich lays in the "pronoun" variable. 

# Testing 

## PEP8 
A simpel stroll passed the PEP8 with no errors, look at img belov. 
The game had alot of PEP8 errors wich is handeld now. 
![PEP8](images/PEP8.png)

## Manual testing 
### Start Game 
1. Start the game by enter your name: I used an Isalpah function so the user is only able to use letters. If you use a number the system will make a loop back.
### Choose path 
1. The user is able to pick 1 or 2 depening on if the user want an city stroll or forest stroll
2. IF the user input A or 3 nothing will happen, but they wont be able to progess in the story untill they pick 1 or 2. 
### Death
1. When the player dies they have 2 options 
2. They can pick y and they will play again 
3. They can also pick n to leave. 
4. IF they pick y they will go back to start game function
### Congratulation 
1. When the player survives the stroll they will come to the congrats function
2. When they come to that function they have 2 choices. 
3. Press y to play again and they will come back to start game function 
4. OR press n to leave the game. 
### Persons in the story
1. Inside Hide boy function the user is able to pick women or man for the person they meet.
2. If the player choose women, the story changes for the pronunciation to she. 
3. We pass the prounce, person_c, person_c_g through the functions. 
4. The player is only able to enter women or man but for the name they are able to pick a number. 
5. If they enter 2 on women or man they will come back to "women or man"? 
## Depoloyment

I deployd this project to Heroku 

1. I logged in to Heroku
2. Created new app
3. Named my app and picked my region 
4. Then i linked the heroku app to my repo in github and loaded it. 


## Bugs 
 I found a couple bugs where the player would put in 3 when there only was 1 or 2 as an option wich would create an infinite loop. 
 The other bug i found was when i created else statments but didn't pass in the variable from the function wich made it crash.

## Images 

On this picture the user have the power to create it's own story by controlling who them will meet. Is it a a girl or man? Friend or foe? 
![Simpel_stroll](images/simpel_stroll.JPG)

Here is another picture of the hole application. I tried to structure the text with _________ lines and \n
![Another_picture_of_simpel_stroll](images/Skärmbild%20(97).png)

## To the Game 
Here is the link to the game <https://a-simple-stroll-c4fc7eb42776.herokuapp.com/>


