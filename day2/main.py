import sys

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def is_id_valid_v1(id:str) -> bool:
    if len(id) % 2 == 0:
        if id[:int(len(id)/2)] == id[int(len(id)/2):]: return False
    return True

def is_id_valid_v2(id:str) -> bool:
    id_len = len(id)
    for i in range(id_len-1, 0, -1):
        if id_len % i == 0: 
            groups = list(chunkstring(id, i))
            continue_flag = False
            for g in groups:
                if g != groups[0] : 
                    continue_flag=True
                    break
            if continue_flag: continue
            return False
    return True

def get_puzzle_input(path:str):
    with open(path, "r") as f:
        ranges = f.read().split(',')
    return [[r.split("-")[0],r.split("-")[1]] for r in ranges]

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("no input filename was provided!")
        exit(1)

    input = get_puzzle_input(sys.argv[1])
    
    answer0 = 0
    answer1 = 0
    for r in input:
        for i in range(int(r[0]), int(r[1])+1):
            if not is_id_valid_v1(str(i)): answer0+=i
            if not is_id_valid_v2(str(i)): answer1+=i

    print(f"answer0:{answer0}")
    print(f"answer1:{answer1}")