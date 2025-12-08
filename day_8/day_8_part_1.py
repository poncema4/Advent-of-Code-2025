# Day 8: Playground

from collections import defaultdict

def playground(lines):
    points = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        x, y, z = map(int, line.split(","))
        points.append((x, y, z))

    n = len(points)

    parent = list(range(n))
    size = [1] * n

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    dists = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i+1, n):
            x2, y2, z2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            dist2 = dx*dx + dy*dy + dz*dz
            dists.append((dist2, i, j))

    dists.sort(key=lambda x: x[0])

    for k in range(1000):
        _, i, j = dists[k]
        union(i, j)

    comp_count = defaultdict(int)
    for i in range(n):
        comp_count[find(i)] += 1

    sizes = sorted(comp_count.values(), reverse=True)

    return sizes[0] * sizes[1] * sizes[2]

if __name__ == "__main__":
    with open("day_8/day_8_input.txt") as f:
        lines = f.readlines()

    answer = playground(lines)
    print("Product of the three largest circuits: ", answer)