import numpy as np

def scaffold():
    #scaff_mat = np.empty((14,9))
    # ^^ might be better to fill it with blanks instead so printing isn't so hard
    scaff_mat = np.full((14,9), " ", dtype=str)  # might be unreasonably tall

    # add the actual scaffold (is that what it's even called?)
    # TODO this vvv would be better if i made it into a string and used iteration
    # CAREFUL WITH THE INDECES
    scaff_mat[13,0] = "_"
    scaff_mat[13,1] = "_"
    scaff_mat[13,2] = "|"
    scaff_mat[13,3] = "_"
    scaff_mat[13,4] = "_"
    scaff_mat[12,2] = "|"
    scaff_mat[11,2] = "|"
    scaff_mat[10,2] = "|"  #<--- oh man i definitely need to use iteration for the pole

    #vvv new 5/3
    # goal: get matrix to print without the damn apostrophes -- IT WORKS
    # it's a 2d matrix so we have to go through all items in all lists in the 2d list
    #vvv i is a list
    for i in scaff_mat:
        # vvv j is each item within the 'horizontal' list
        line = ""
        for j in i:
            line = line + j
        print(line) #+ "\n") <-- added extra do not want

    #print(scaff_mat)
    return scaff_mat

def add2man(num_guesses, man_mat):
    if num_guesses >= 1:
        build_head()
    if num_guesses >= 2: 
        build_body()
    return man_mat


def build_head():
    #stuff
    return

def test_vals(bad_guesses):
    print (bad_guesses)

scaffold()