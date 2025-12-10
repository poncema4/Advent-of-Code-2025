# Day 10: Factory

import re

def parse(line):
    pattern = re.search(r'\[([.#]+)\]', line).group(1)
    target = 0
    for i,ch in enumerate(pattern):
        if ch == '#':
            target |= 1 << i

    buttons = []
    for btn in re.findall(r'\(([^)]*)\)', line):
        mask = 0
        if btn.strip():
            for x in btn.split(','):
                mask |= 1 << int(x)
        buttons.append(mask)

    return target, buttons

def fewest_presses(target, buttons):
    m = len(buttons)
    best = float('inf')

    for mask in range(1 << m):
        toggled = 0
        presses = mask.bit_count()

        if presses >= best: 
            continue

        for i in range(m):
            if (mask >> i) & 1:
                toggled ^= buttons[i]

        if toggled == target:
            best = presses

    return best

def button_presses(lines):
    total = 0
    for line in lines:
        if line.strip():
            target, buttons = parse(line)
            total += fewest_presses(target, buttons)
    return total

if __name__ == "__main__":
    with open("day_10/day_10_input.txt") as f:
        lines = f.readlines()

    answer = button_presses(lines)
    print("Fewest button presses required: ", answer)