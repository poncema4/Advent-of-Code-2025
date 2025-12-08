# Day 8: Playground

from collections import Counter

def playground(lines):
    pts = [tuple(map(int, l.split(","))) for l in lines if l.strip()]
    n = len(pts)

    edges = []
    for i in range(n):
        x1,y1,z1 = pts[i]
        for j in range(i+1, n):
            x2,y2,z2 = pts[j]
            edges.append(((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2, i, j))
    edges.sort()

    p = list(range(n))
    s = [1] * n
    comp = n

    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    attempts = 0

    for _, a, b in edges:
        ra, rb = find(a), find(b)
        merged = ra != rb
        if merged:
            if s[ra] < s[rb]:
                ra, rb = rb, ra
            p[rb] = ra
            s[ra] += s[rb]
            comp -= 1

        attempts += 1

        if merged and comp == 1:
            return pts[a][0] * pts[b][0]

if __name__ == "__main__":
    with open("day_8/day_8_input.txt") as f:
        lines = f.readlines()

    answer = playground(lines)
    print("Product of the last X coordinates: ", answer)