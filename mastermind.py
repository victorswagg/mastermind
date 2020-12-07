#!/usr/bin/env python3
##
## mastermind
##

import sys
import math
import random
import json

def save_score(pseudo, score):
	with open ("score.json") as file:
		json_data = json.load(file)
	with open ("score.json","w") as file:
		json_data["previous"].append({pseud:score})
		json.dump(json_data, file)

def mega():
    tries = 0;
    all_colors = ["red", "blue","yellow","green","black","white","orange","pink"]
    colors = []

    for i in range(0,5):
       colors.append(random.choice(all_colors))

    print(colors)
    while tries < 12 and tries != 20 :
        guess = input("enter your guess\n")
        guess = guess.split(" ")
    
        if len(guess) == 4 and guess == colors:
            print("congrats, good answer\n")
            score = 10 - tries
            print("your score is:\t", score)
            tries = 20
        else:
            print("wrong answer, try again")
            tries += 1
            
    if tries == 12:
        print("FAILURE, you've used all your attempts")
        score = 0
    return score


def normal():
    tries = 0;
    i = 3;
    all_colors = ["red", "blue","yellow","green","black","white"]
    colors = []

    for i in range(0,4):
       colors.append(random.choice(all_colors))

    print (colors)

    while tries < 10 and tries != 20 :
        guess = input("enter your guess\n")
        guess = guess.split(" ")
    
    if len(guess) == 4 and guess == colors:
        print("congrats, good answer\n")
        score = 10 - tries
        print("your score is:\t", score)
        tries = 20
    else:
        print("wrong answer, try again")
        tries += 1
        
    if tries == 10:
            print("FAILURE, you've used all your attempts")
            score = 0
    return(score)



game = input("please enter normal or mega mode\n")
if game == "normal":
    score = normal()
elif game == "mega" or game == "méga":
    score = mega()
else:
    print("wrong type of game, goodbye")
    sys.exit (84)
    
pseudo = input("save your score by entering your pseudo\n")
print("save\n\n score\t", score,"\npseudo\t", pseudo)
#sauvegarde la game ici
save_score(pseudo, score)
sys.exit (0)
