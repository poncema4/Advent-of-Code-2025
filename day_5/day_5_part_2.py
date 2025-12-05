# Day 5: Cafeteria

def total_fresh_ids(lines):
    ranges = []
    for line in lines:
        line = line.strip()
        if "-" in line:
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
    
    ranges.sort()
    merged = []
    for start, end in ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    
    return sum(end - start + 1 for start, end in merged)

if __name__ == "__main__":
    with open("day_5/day_5_input.txt") as f:
        lines = f.readlines()

    answer = total_fresh_ids(lines)
    print("Ingredients considered fresh in the ID ranges: ", answer)