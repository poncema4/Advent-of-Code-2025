# Day 9: Movie Theater

def largest_area(lines):
    red_tiles = []
    for line in lines:
        x, y = map(int, line.strip().split(','))
        red_tiles.append((x, y))

    n = len(red_tiles)

    edges = []
    for i in range(n):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[(i + 1) % n]
        edges.append(((x1, y1), (x2, y2)))
    
    def point_in_polygon(x, y):
        crossings = 0
        for (x1, y1), (x2, y2) in edges:
            if y1 == y2:
                continue
            if min(y1, y2) <= y < max(y1, y2):
                x_intersect = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                if x < x_intersect:
                    crossings += 1
        return crossings % 2 == 1
    
    def is_on_boundary(x, y):
        for (x1, y1), (x2, y2) in edges:
            if x1 == x2:
                if x == x1 and min(y1, y2) <= y <= max(y1, y2):
                    return True
            elif y1 == y2:
                if y == y1 and min(x1, x2) <= x <= max(x1, x2):
                    return True
        return False
    
    def is_allowed(x, y):
        return is_on_boundary(x, y) or point_in_polygon(x, y)
    
    max_area = 0
    
    for i in range(n):
        x1, y1 = red_tiles[i]
        for j in range(i + 1, n):
            x2, y2 = red_tiles[j]
            
            if x1 == x2 or y1 == y2:
                continue

            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)
            area = (max_x - min_x + 1) * (max_y - min_y + 1)
            
            if area <= max_area:
                continue

            if not all(is_allowed(x, y) for x, y in 
                      [(min_x, min_y), (max_x, min_y), (min_x, max_y), (max_x, max_y)]):
                continue

            valid = True
            sample_points = 10

            for k in range(sample_points + 1):
                x = min_x + k * (max_x - min_x) // sample_points
                if not is_allowed(x, min_y) or not is_allowed(x, max_y):
                    valid = False
                    break
            
            if not valid:
                continue

            for k in range(sample_points + 1):
                y = min_y + k * (max_y - min_y) // sample_points
                if not is_allowed(min_x, y) or not is_allowed(max_x, y):
                    valid = False
                    break
            
            if not valid:
                continue

            interior_samples = min(20, (max_x - min_x) * (max_y - min_y) // 100)
            for k in range(interior_samples):
                x = min_x + (k * 7919) % (max_x - min_x + 1)
                y = min_y + (k * 7907) % (max_y - min_y + 1)
                if not is_allowed(x, y):
                    valid = False
                    break
            
            if not valid:
                continue

            check_interval = max(1, (max_y - min_y) // 50)
            for y in range(min_y, max_y + 1, check_interval):
                for x in [min_x, max_x, (min_x + max_x) // 2]:
                    if not is_allowed(x, y):
                        valid = False
                        break
                if not valid:
                    break
            
            if valid:
                for y in range(min_y, max_y + 1, max(1, (max_y - min_y) // 10)):
                    for x in range(min_x, max_x + 1, max(1, (max_x - min_x) // 10)):
                        if not is_allowed(x, y):
                            valid = False
                            break
                    if not valid:
                        break
            
            if valid:
                max_area = area

    return max_area

if __name__ == "__main__":
    with open("day_9/day_9_input.txt") as f:
        lines = f.readlines()

    answer = largest_area(lines)
    print("Largest area of any rectangle with only red and green tiles: ", answer)