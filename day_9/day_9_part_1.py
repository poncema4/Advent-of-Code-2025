# Day 9: Movie Theater

def largest_area(lines):
    red_tiles = set()
    for line in lines:
        x, y = map(int, line.strip().split(','))
        red_tiles.add((x, y))
    
    max_area = 0
    red_list = list(red_tiles)

    for i in range(len(red_list)):
        for j in range(i + 1, len(red_list)):
            x1, y1 = red_list[i]
            x2, y2 = red_list[j]

            if x1 != x2 and y1 != y2:
                width = abs(x2 - x1) + 1
                height = abs(y2 - y1) + 1
                area = width * height
                if area > max_area:
                    max_area = area

    return max_area

if __name__ == "__main__":
    with open("day_9/day_9_input.txt") as f:
        lines = f.readlines()

    answer = largest_area(lines)
    print("Largest area of any rectangle that can be made:", answer)