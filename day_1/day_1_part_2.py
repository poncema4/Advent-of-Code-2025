# Day 1: Secret Entrance

def find_secret_entrance(rotations):
    dial = 50
    zero_count = 0

    for line in rotations:
        s = line.strip()
        if not s:
            continue

        direction = s[0].upper()
        step = int(s[1:])
        
        move = -1 if direction == "L" else 1

        for _ in range(step):
            dial = (dial + move) % 100
            if dial == 0:
                zero_count += 1

    return zero_count

if __name__ == "__main__":
    with open("day_1/day_1_input.txt") as f:
        lines = f.readlines()

    answer = find_secret_entrance(lines)
    print("Password: ", answer)