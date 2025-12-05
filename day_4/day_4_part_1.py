# Day 4: Printing Department

def count_accessible(lines, return_map):
    grid = [list(line.rstrip("\n")) for line in lines]
    h = len(grid)
    w = len(grid[0])

    neighbors = [(-1,-1), (-1,0), (-1,1), (0,-1), 
                 (0,1), (1,-1), (1,0), (1,1)]

    accessible_count = 0
    visual = [row[:] for row in grid]

    for r in range(h):
        for c in range(w):
            if grid[r][c] != '@':
                continue
            adj_at = 0
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == '@':
                    adj_at += 1
            if adj_at < 4:
                accessible_count += 1
                visual[r][c] = 'x'

    if return_map:
        return accessible_count, ["".join(row) for row in visual]
    else:
        return accessible_count, []

if __name__ == "__main__":
    with open("day_4/day_4_input.txt") as f:
        lines = f.readlines()

    answer = count_accessible(lines, return_map=False)[0]
    print("Accessible rolls: ", answer)