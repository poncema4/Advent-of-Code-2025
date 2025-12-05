# Day 3: Lobby

def total_output_joltage(lines, k=12):
    total = 0

    for bank in lines:
        digits = bank.strip()
        n = len(digits)

        to_pick = k
        result = []

        start = 0
        while to_pick > 0:
            end = n - to_pick

            window = digits[start:end+1]
            max_digit = max(window)
            idx = window.index(max_digit) + start

            result.append(max_digit)

            start = idx + 1
            to_pick -= 1

        total += int("".join(result))

    return total

if __name__ == "__main__":
    with open("day_3/day_3_input.txt") as f:
        lines = f.readlines()

    answer = total_output_joltage(lines)
    print("Total Output Joltage: ", answer)