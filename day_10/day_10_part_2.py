# Day 10: Factory

import re
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, PULP_CBC_CMD

def parse_machine(line):
    buttons = []
    for btn in re.findall(r'\(([^)]*)\)', line):
        if btn.strip():
            buttons.append(tuple(int(x) for x in btn.split(',')))
        else:
            buttons.append(tuple())
    
    target_match = re.search(r'\{([^}]*)\}', line)
    target = tuple(int(v) for v in target_match.group(1).split(','))
    
    return buttons, target

def min_button_presses(target, buttons):
    prob = LpProblem("MinButtonPresses", LpMinimize)

    x_vars = {
        i: LpVariable(f"x_{i}", lowBound=0, cat="Integer") 
        for i in range(len(buttons))
    }
    
    prob += lpSum(x_vars[i] for i in x_vars)

    for j in range(len(target)):
        prob += (
            lpSum(x_vars[i] for i, button in enumerate(buttons) if j in button) == target[j],
            f"counter_{j}",
        )

    prob.solve(PULP_CBC_CMD(msg=False))

    return int(sum(var.varValue for var in x_vars.values()))

def button_presses(lines):
    total = 0
    for line in lines:
        if line.strip() and '{' in line:
            buttons, target = parse_machine(line)
            presses = min_button_presses(target, buttons)
            total += presses
    return total

if __name__ == "__main__":
    with open("day_10/day_10_input.txt") as f:
        lines = f.readlines()

    answer = button_presses(lines)
    print("Fewest button presses required: ", answer)