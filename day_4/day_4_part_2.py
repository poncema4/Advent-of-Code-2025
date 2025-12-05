# Day 4: Printing Department

def total_removable(lines):
    grid = [list(line.rstrip("\n")) for line in lines]
    h = len(grid)
    w = len(grid[0])

    neighbors = [(-1,-1), (-1,0), (-1,1), (0,-1),         
                 (0,1), (1,-1), (1,0), (1,1)]

    removed_total = 0

    while True:
        to_remove = []

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
                    to_remove.append((r, c))

        if not to_remove:
            break

        for (r, c) in to_remove:
            grid[r][c] = '.'

        removed_total += len(to_remove)

    return removed_total

if __name__ == "__main__":
    with open("day_4/day_4_input.txt") as f:
        lines = f.readlines()

    answer = total_removable(lines)
    print("Accessible rolls: ", answer)