# Day 6: Trash Compactor

def trash_compactor(lines):
    L = [l.rstrip("\n") for l in lines]
    if not L: return 0
    w = max(map(len, L))
    L = [l.ljust(w) for l in L]
    ops, nums = L[-1], L[:-1]

    blocks, s = [], None
    for i, u in enumerate([any(r[c] != " " for r in L) for c in range(w)] + [0]):
        if u and s is None: s = i
        elif not u and s is not None: 
            blocks.append((s, i))
            s = None

    total = 0
    for a, b in blocks:
        op = ops[a:b].strip()
        if op not in "+*": continue
        xs = [int(r[a:b]) for r in nums if r[a:b].strip()]
        if op == "+": total += sum(xs)
        else:
            p = 1
            for x in xs: p *= x
            total += p
    return total

if __name__ == "__main__":
    with open("day_6/day_6_input.txt") as f:
        lines = f.readlines()

    answer = trash_compactor(lines)
    print("Grand total found: ", answer)