# Day 2: Gift Shop

def sum_invalid_ids(ids): 
    def is_invalid_id(n):
        s = str(n)
        length = len(s)

        for sub_len in range(1, length // 2 + 1):
            if length % sub_len != 0:
                continue

            repeats = length // sub_len
            if repeats < 2:
                continue

            chunk = s[:sub_len]
            if chunk * repeats == s:
                return True
            
        return False
    
    total = 0
    ranges = ids.strip().split(",")

    for r in ranges:
        if not r:
            continue
        starting, ending = r.split("-")
        start = int(starting)
        end = int(ending)

        for n in range(start, end+1):
            if is_invalid_id(n):
                total += n

    return total

if __name__ == "__main__":
    with open("day_2/day_2_input.txt") as f:
        line = f.readline()

    answer = sum_invalid_ids(line)
    print("Total Invalid Ids: ", answer)