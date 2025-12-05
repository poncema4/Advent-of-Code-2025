# Day 3: Lobby

def total_output_joltage(lines):
    total = 0
    for bank in lines:
        bank = bank.strip()
        digits = list(bank)
        n = len(digits)

        suffix_max = ['0'] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(digits[i], suffix_max[i+1])

        best = 0
        for i in range(n - 1):
            num = int(digits[i] + suffix_max[i+1])
            if num > best:
                best = num

        total += best

    return total

if __name__ == "__main__":
    with open("day_3/day_3_input.txt") as f:
        lines = f.readlines()

    answer = total_output_joltage(lines)
    print("Total Output Joltage: ", answer)