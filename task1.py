#!python3
'''
sort all of the values of x into 2 lists.
1 list should contain all of the float values and the other list should contain all the integer values'''


def main():
    INTEGERS = []
    DECIMALS = []

    x = [7.7, 1, 3.3, 4.2, 11.0, 1, 1, 2.8, 2, 8, 3, 4, 5, 7, 9.2, 3.1, 9, 6, 4, 8, 5, 1.9, 2, 4, 4, 5.2, 2, 5.4, 2, 3.4, 7, 9.2, 3.7, 10, 8, 7, 6, 2, 2.2, 1]

    for NUMBERS in x:
        #Check if float
        CHECK = isinstance(NUMBERS, int) 
        #Add to INT if true
        if CHECK == True:
            INTEGERS.append(NUMBERS)
        #Add to DEC if true
        else:
            DECIMALS.append(NUMBERS)

    print(INTEGERS)
    print(DECIMALS)

#DONE












if __name__ == "__main__":
    main()