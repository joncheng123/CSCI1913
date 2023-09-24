# CSCI 1913
# Project 1: Wordle
# Code by Jonathan Cheng

import random
from display_utility import *
from words import *

def check_word(secret, guess):
    """This function check the word input (guess) and return a length 5 list containing the color"""
    output = []
    secret = list(secret)
    guess = guess.upper()
    guess = list(guess)
    # checks for grey letter, make sure there are no letters that matches guess with the secret
    for i in range(5):
        output.append("grey")
    
    # checks for any green letter, make sure if the letter matches and output green
    # replaces the 5 letters with . so to cater for the double letter function later
    for i in range(5):
        if guess[i] == secret[i]:
            output[i] = "green"
            secret[i] = "."

    # checks for yellow letter if the one of the guess letter exist in secret
    # checks for double letter 
    for i in range(5):
        if guess[i] in secret and output[i] == "grey":
            output[i] = "yellow"
            index = secret.index(guess[i])
            secret[index] = "."

    return output
    
def known_word(clues):
    """This fuction takes in a list of record of guesses and the clues received
    The output will be the list of letters which is the right guess when the letters are in place"""
    output = ["_", "_", "_", "_", "_"]
    for guess, clue in clues: #access tuples directly
        guess = guess.upper()
        for j in range(5): #guess is always 5 letter word
            if clue[j] == "green":
                output[j] = guess[j]
    output =  "".join(output) # converts list into a string
    return output

def no_letters(clues):
    """This fuction takes in input as a list of containing the guesses taken and clues received so-far
    And the output of this function will be the grey letters string """
    
    output = []
    for guess, clue in clues:
        guess = guess.upper()
        for j in range(5): #check letter
            flag = True
            for i in range(5): #check letter with the other letter
                if (guess[i] == guess[j]) and (clue[i] != "grey") and i != j:  # if is duplicate letter and geen or yellow
                    flag = False
            if (clue[j] == "grey") and flag:
                output.append(guess[j]) # add the grey letter into the output
                # output.sort() # sort alphabetically
    
    output = list(set(output)) # remove duplicate grey letters by turning into a set because set can't contain a duplicate element
    output.sort() # sort alphabetically
    output = "".join(output) # converts list into a string
    return output

def yes_letters(clues):
    """This function takes in input as a list of containing the guesses taken and clues received so-far
    And the output of this function will be the Green/Yellow letter string """

    output = []
    for guess, clue in clues:
        guess = guess.upper()
        for j in range(5): #check letter
            for i in range(5): #check letter with the other letter
                if (clue[i] == ("yellow") or clue[i] == "green") and i == j: # check if is yellow or green
                    output.append(guess[j]) # add the yellow or green letter into the output
                
    output = list(set(output)) # remove duplicate grey letters by turning into a set because set can't contain a duplicate element
    output.sort() # sort alphabetically
    output = "".join(output) # converts list into a string
    return output

def printcolor(guess, clue):
    "This function prints color of the letter"
    for guess, clue in clue:
        for j in range(5):
            if (clue[j] == "grey"):
                    grey(guess[j])
            elif (clue[j] == "yellow"):
                    yellow(guess[j])
            else:
                green(guess[j])
        print("")

if __name__ == "__main__":
    
    pastguesses = ""
    storegreenyellow = ""
    storegrey = ""
    clue = []
    guessTrack = ["_", "_","_", "_", "_"]
    
    secret = random.choice(words)
    print("Known: ", "".join(guessTrack))
    print("Green/Yellow Letters:")
    print("Grey Letters:")

    for i in range(6): # 6 guesses count
        
        guess = input()
        guess = guess.upper()
        clue.append((guess, check_word(secret, guess))) # appending tuples of color
        pastguesses = pastguesses + guess + "\n"
        printcolor(pastguesses, clue)

        if guess == secret:
            secret = secret.upper()
            print("Answer:", secret)
            exit()
        else:
            check = 0
            storeknown = ""
            for j in range(5): # iterate every letter
                if (guess[j] != secret[j]): # checks if letter matches secret letter
                    check = 1
                else:    
                    if guessTrack[j] == "_": # if guess letter is same as secret letter
                        guessTrack[j] = guess[j]

            if check == 1: # to avoid printing 5 times
                storeknown = storeknown + known_word([(guess, check_word(secret, guess))])
                print("Known: ", storeknown)
                
                storegreenyellow = storegreenyellow + yes_letters([(guess, check_word(secret, guess))])
                storegreenyellow = list(set(storegreenyellow)) # remove duplicates by converting to a set
                storegreenyellow.sort()
                storegreenyellow = "".join(storegreenyellow)
                print("Green/Yellow Letters:", storegreenyellow)
                
                storegrey = storegrey + no_letters([(guess, check_word(secret, guess))])
                storegrey = list(set(storegrey)) # remove duplicates by converting to a set
                storegrey.sort()
                storegrey = "".join(storegrey)
                print("Grey Letters:", storegrey)
                
                check = 0
    secret = secret.upper()
    print("Answer:", secret)