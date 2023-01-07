# Hermoine's Starter Code for Deathly Hallows Game (Stone, Cloak, Wand)

# Import the randint function from random
from random import randint

# Introduction
print("Welcome to the Stone, Cloak, Wand Game!")
user = input("What's your name? ")
player = input("Who in the Harry Potter world do you want to be your opponent? ")
print("Cool! " + player + " will be your opponent & you will be entering your selection of stone, cloak, or wand. :)")
print("Ready set go!")

# Declare variables
userChoice = ""
playerChoice = ""
gameResults = ""
player_cnt = 0
opponent_cnt = 0

# Generate the player's choice
playerValue = randint(1, 3)
if (playerValue == 1):
    playerChoice = "stone"
elif (playerValue == 2):
    playerChoice = "cloak"
elif (playerValue == 3):
    playerChoice = "wand"

# Get user's choice 
userChoice = input("Enter Stone, Cloak, or Wand: ")
userChoice = userChoice.lower()

# Validate user's input
while(userChoice != 'stone' and userChoice != 'cloak' and userChoice != 'wand'):
  userChoice = input("Enter Stone, Cloak, or Wand: ")
  userChoice = userChoice.lower()

# Show the user the selections
print(player + " chose: " + playerChoice)
print("You chose: " + userChoice)

# There will be a tie
if ((playerChoice == "stone" and userChoice == "stone") or (playerChoice == "cloak" and userChoice == "cloak") or (playerChoice == "wand" and userChoice == "wand")):
  gameResults = "It's a tie!"   	

# User will win
elif ((playerChoice == "stone" and userChoice == "cloak") or (playerChoice == "cloak" and userChoice == "wand") or (playerChoice == "wand" and userChoice == "stone")):
  gameResults = "You win!"
  player_cnt += 1

# Player will win
elif ((playerChoice == "stone" and userChoice == "wand") or (playerChoice == "cloak" and userChoice == "stone") or (playerChoice == "wand" and userChoice == "cloak")):
  gameResults = player + " wins!"
  opponent_cnt += 1

# Display the results to the user
print(gameResults)
