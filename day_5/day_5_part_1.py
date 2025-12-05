# Day 5: Cafeteria

def count_fresh_ids(lines):
    clean = [line.strip() for line in lines if line.strip()]

    ranges = []
    ids = []

    for line in clean:
        if "-" in line:
            a, b = map(int, line.split("-"))
            ranges.append((a, b))
        else:
            ids.append(int(line))

    fresh = 0
    for x in ids:
        for (a, b) in ranges:
            if a <= x <= b:
                fresh += 1
                break

    return fresh

if __name__ == "__main__":
    with open("day_5/day_5_input.txt") as f:
        lines = f.readlines()

    answer = count_fresh_ids(lines)
    print("Available ingredient IDs that are fresh: ", answer)