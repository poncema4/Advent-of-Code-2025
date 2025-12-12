# Day 11: Reactor

def reactor(lines):
    graph = {}

    for line in lines:
        src, rhs = line.strip().split(":")
        outs = rhs.strip().split()
        graph[src.strip()] = outs

    memo = {}

    def dfs(node, seen_dac, seen_fft):
        key = (node, seen_dac, seen_fft)

        if key in memo:
            return memo[key]

        if node == "out":
            return 1 if seen_dac and seen_fft else 0

        if node not in graph:
            return 0

        if node == "dac":
            seen_dac = True
        if node == "fft":
            seen_fft = True

        total = 0
        for nxt in graph[node]:
            total += dfs(nxt, seen_dac, seen_fft)

        memo[key] = total
        return total

    return dfs("svr", False, False)

if __name__ == "__main__":
    with open("day_11/day_11_input.txt") as f:
        lines = f.readlines()

    answer = reactor(lines)
    print("Total different paths that lead from svr to out: ", answer)