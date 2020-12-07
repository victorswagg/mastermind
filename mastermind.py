#!/usr/bin/env python3
##
## mastermind
##

import sys
import math
import random

def mega():
    tries = 0;
    colors = [random.randint(1, 8), random.randint(1, 8), random.randint(1, 8), random.randint(1, 8), random.randint(1, 8)]
################
    for i in range(len(colors)):
        if colors[i] == 1:
            colors[i] = "red"
        elif colors[i] == 2:
            colors[i] = "blue"
        elif colors[i] == 3:
            colors[i] = "yellow"
        elif colors[i] == 4:
            colors[i] = "green"
        elif colors[i] == 5:
            colors[i] = "black"
        elif colors[i] == 6:
            colors[i] = "white"
        elif colors[i] == 7:
            colors[i] = "orange"
        elif colors[i] == 8:
            colors[i] = "pink"
        print(i)
##################
        print (colors)

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
        pseudo = input("save your score by entering your pseudo\n")

def normal():
    tries = 0;
    i = 3;
    colors = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
################
    while i >= 0:
        if colors[i] == 1:
            colors[i] = "rouge"
        elif colors[i] == 2:
            colors[i] = "bleu"
        elif colors[i] == 3:
            colors[i] = "jaune"
        elif colors[i] == 4:
            colors[i] = "vert"
        elif colors[i] == 5:
            colors[i] = "noir"
        elif colors[i] == 6:
            colors[i] = "blanc"
        print(i)
        i -= 1
##################
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
sys.exit (0)
