import sys

def turn_dial(answer0:int, answer1:int, current_value:int, rotation:str) -> int:
    direction:int = -1 if rotation[0] == "L" else 1
    clicks:int = int(rotation[1:])
    
    for i in range(clicks):
        current_value += direction
        if current_value >= 100: current_value = 0
        if current_value <= -1: current_value = 99
        if current_value == 0: answer1 += 1
    if current_value == 0: answer0 += 1
    return (current_value, answer0, answer1)

def get_puzzle_input(path:str):
    with open(path, "r") as f:
        lines = f.read().split('\n')
    return [l for l in lines if len(l)>0]

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("no input filename was provided!")
        exit(1)

    input = get_puzzle_input(sys.argv[1])

    dial = 50
    answer0 = 0
    answer1 = 0
    
    for i in input:
        res = turn_dial(answer0, answer1, dial, i)
        dial = res[0]
        answer0 = res[1]
        answer1 = res[2]
        
    print(f"First part:{answer0}")
    print(f"Second part:{answer1}")