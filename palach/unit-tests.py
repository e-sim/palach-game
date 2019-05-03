
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
print_scaff(scaffold)