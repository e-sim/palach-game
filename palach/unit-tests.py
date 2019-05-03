
import numpy as np
# tests to do:
# create/print empty matrix CHECK
# print matrix correctly
# print individual body parts
# print everything together

def scaffold():

    scaff_mat = np.full((10,20), ".", dtype=str)

    # add the actual scaffold (is that what it's even called?)
    scaff_mat[9,0] = "a"
    scaff_mat[9,1] = "b"
    scaff_mat[:, 1] = ("c" for i in scaff_mat)

    # print(np.array2string(x, precision=2, separator=','
    # print(np.array2string(scaff_mat, separator=' ').strip("'"))
    return scaff_mat

def print_scaff(scaff):
    for i in scaff:
       # print(i)
        for j in i:
            print(j, end='')
        print("\n")


scaffold = scaffold()
#print_scaff(scaffold)

# Palach.py
# Russian hangman program
# eventually can also be used for other languages
#
# command: palach.py language level
# language wordlist files must be named as [languagename].txt

#!/usr/bin/env python3

import sys, random, re, logging
import numpy as np

''' this prints the game blanks/letters to the screen'''
def game_print(letters):
    output = ""
    for l in letters:
        output = "{0} {1}".format(output, l)
    print(output)



def main():
    logger = logging.getLogger("palach_log")
    logger.setLevel(logging.DEBUG)

    #lang = sys.argv[1]
    lang = "test"  #this is for debuggingpurposes
    dict_file = lang + ".txt"   # later will use .csv

    with open(dict_file, "r") as d:
        # VV this will need to change once i use the csv file
        wordlist = d.readlines()
    
    play_word = random.choice(wordlist).strip()
    letter_set = set()
    
    for char in play_word:
            letter_set.add(char)      

    #TODO: either don't allow two-word items or deal with them somehow-- make blank not appear?  

    guessed_letters = set()
    wrong_letters = set()
    print(letter_set)
    # TODO: ideally i'll have either another list or part of the same csv file that 
    # translates all the text for different languages
    print("hi erica!")
    player_sees = ["_" for x in range(len(play_word))]
    game_print(player_sees)
    blanks_left = len(play_word)

    # makes the matrix to form the hangman & scaffold

    #TODO fix loop structure
    while blanks_left: #and hangman isn't finished
        guess = input("угадай букву: ")
        if len(guess) > 1:
            print("только одна буква")
            continue
         
        if guess in guessed_letters:
            print("уже угадал!") #prob should put it in passive
            continue

        if guess in letter_set:
            #cleanup
            guessed_letters.add(guess)
            blanks_left -= 1
            letter_set.discard(guess)
            # add to player_sees in correct place
            indeces = [match.start() for match in re.finditer(guess, play_word)]
            for i in indeces:
                player_sees[i] = guess
            #print(player_sees)   <--- i'm just testing turning this off
            # also print wrong guesses, plus the hangman

        else:
            print("угадай еще раз")

            # yes i'm testing using print :(
            #print(guess + "/t" + guessed_letters) <--- won't print set fyi
            
            # TODO add to wrong guesses & print that
            guessed_letters.add(guess)
            wrong_letters.add(guess)

            #update hangman
            #continue

        num_letters = len(guessed_letters)
        game_print(player_sees)
        #scaffold()



if __name__ == "__main__":
    main()
