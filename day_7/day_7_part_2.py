# Day 7: Laboratories

def repair_teleporter(lines):
    grid = [list(line.rstrip("\n")) for line in lines]
    h = len(grid)
    w = len(grid[0])

    for r in range(h):
        for c in range(w):
            if grid[r][c] == 'S':
                start_r, start_c = r, c
                break

    dp = [[0] * w for _ in range(h)]

    for r in range(h-1, -1, -1):
        for c in range(w):
            cell = grid[r][c]

            if r+1 >= h:
                down = 1
            else:
                down = dp[r+1][c]

            if cell == '^':
                if c-1 < 0:
                    left = 1
                else:
                    left = dp[r+1][c-1]
                    
                if c+1 >= w:
                    right = 1
                else:
                    right = dp[r+1][c+1]

                dp[r][c] = left + right

            else:
                dp[r][c] = down

    sr = start_r + 1
    sc = start_c
    if sr >= h:
        return 1
    return dp[sr][sc]

if __name__ == "__main__":
    with open("day_7/day_7_input.txt") as f:
        lines = f.readlines()

    answer = repair_teleporter(lines)
    print("Amount of different timelines: ", answer)