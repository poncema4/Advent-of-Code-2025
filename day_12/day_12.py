# Day 12: Christmas Tree Farm

def christmas_tree(lines):
    shapes = []
    regions = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if line.endswith(":") and line[:-1].isdigit():
            i += 1
            shape = []
            while i < len(lines) and lines[i].strip() and ":" not in lines[i]:
                shape.append(lines[i].rstrip("\n"))
                i += 1
            shapes.append(shape)

        elif "x" in line:
            size, nums = line.split(":")
            w, h = map(int, size.split("x"))
            counts = list(map(int, nums.split()))
            regions.append((w, h, counts))
            i += 1

        else:
            i += 1

    areas = [sum(row.count("#") for row in shape) for shape in shapes]

    total = 0
    for w, h, counts in regions:
        region_area = w * h
        presents_area = sum(areas[i] * counts[i] for i in range(len(areas)))
        if presents_area <= region_area:
            total += 1

    return total

if __name__ == "__main__":
    with open("day_12/day_12_input.txt") as f:
        lines = f.readlines()

    answer = christmas_tree(lines)
    print("Total regions that can fit all of the presents: ", answer)