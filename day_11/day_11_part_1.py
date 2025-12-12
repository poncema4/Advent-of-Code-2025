# Day 11: Reactor

def reactor(lines):
    graph = {}

    for line in lines:
        src, rhs = line.strip().split(":")
        outs = rhs.strip().split()
        graph[src.strip()] = outs

    def dfs(node):
        if node == "out":
            return 1
        if node not in graph:
            return 0
        total = 0
        for nxt in graph[node]:
            total += dfs(nxt)
        return total

    return dfs("you")

if __name__ == "__main__":
    with open("day_11/day_11_input.txt") as f:
        lines = f.readlines()

    answer = reactor(lines)
    print("Total different paths that lead from you to out: ", answer)