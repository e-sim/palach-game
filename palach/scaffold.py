
def scaffold():
    #scaff_mat = np.empty((14,9))
    # ^^ might be better to fill it with blanks instead so printing isn't so hard
    scaff_mat = np.full((14,9), " ", dtype=str)

    # add the actual scaffold (is that what it's even called?)
    scaff_mat[13,0] = "___"
    scaff_mat[13,1] = "|__"
    # scaff_mat[:, 1] = ["|" for i in 
    # ^^ that's a bit hacky, not sure if it will work
    #TODO this is where i was 1/17 4pm 
    print(scaff_mat)
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
    print bad_guesses