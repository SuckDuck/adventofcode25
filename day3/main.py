import sys

def get_puzzle_input(path:str):
    with open(path, "r") as f:
        banks = f.read().split('\n')
    banks = [[int(o) for o in i] for i in banks]
    return banks

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("no input filename was provided!")
        exit(1)

    input = get_puzzle_input(sys.argv[1])
    
    for bank in input:
        first_digit = -1
        second_digit = -1
        highest = 0
        for i in range(len(bank)):
            if (bank[i]>highest):
                highest = bank[i]
                first_digit = i

        highest = 0
        for i in range(len(bank)):
            if i == first_digit: continue
            if (bank[i]>highest):
                highest = bank[i]
                second_digit = i

        print(f"{str(bank[first_digit])}{str(bank[second_digit])}")