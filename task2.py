#!python3

'''
use a for loop to iterate through all possible integers to find the factors of 24
'''
def main():
    factors = []
    myNumber = 24
    
#factor finder
    for NUMBERS in range(1, myNumber + 1):
        if myNumber % NUMBERS == 0:
            factors.append(NUMBERS)
    print(factors)

#DONE

if __name__ == "__main__":
    main()