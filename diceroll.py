import sys, re, random

class Die:
    def __init__(self, num: str):
        self.name = num
        self.sides = int(num)

    def roll(self):
        return(random.randint(1,self.sides))

def main():
    #test = Die("8")
    #print(test.sides)
    #dice_str = sys.argv[1]
    dice_patt = re.compile(r"d?([0-9]+)x?([0-9]*)", re.I)
    bag = []
    for d in sys.argv[1:]:
        match = dice_patt.match(d)
        bag.append(Die(match.group(1)))
        if match.group(2):
            dice_left = int(match.group(2)) -1
            for copy in range(dice_left):
                bag.append(Die(match.group(1)))

    for die in bag:
        print("d{0}\t\t{1}".format(die.name, die.roll()))


if __name__ == "__main__":
    main()