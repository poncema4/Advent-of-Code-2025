# Day 7: Laboratories

def repair_teleporter(lines):
    grid = [list(line.rstrip("\n")) for line in lines]
    h = len(grid)
    w = len(grid[0])

    for r in range(h):
        for c in range(w):
            if grid[r][c] == 'S':
                start_r, start_c = r, c

    queue = [(start_r + 1, start_c)]
    visited = set()
    splits = 0

    while queue:
        r, c = queue.pop()

        if r < 0 or r >= h or c < 0 or c >= w:
            continue
        if (r, c) in visited:
            continue

        visited.add((r, c))
        cell = grid[r][c]

        if cell == '^':
            splits += 1
            if c - 1 >= 0:
                queue.append((r + 1, c - 1))
            if c + 1 < w:
                queue.append((r + 1, c + 1))
        else:
            queue.append((r + 1, c))

    return splits

if __name__ == "__main__":
    with open("day_7/day_7_input.txt") as f:
        lines = f.readlines()

    answer = repair_teleporter(lines)
    print("Amount of times beam will be split: ", answer)