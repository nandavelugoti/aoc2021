sq_tranpose = lambda m : [[row[i] for row in m] for i in range(len(m[0]))]

def part1(data):
    sz = max(sum([list(x.values()) for x in data], []))+1
    grid = [[0 for _ in range(sz)] for _ in range(sz)]
    for line in data:
        x1, y1, x2, y2 = list(line.values())
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2)+1):
                grid[x1][i] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)+1):
                grid[i][y1] += 1
    # optional: transpose cuz origin has to be at top left
    final_grid = sq_tranpose(grid)
    count =0
    for row in range(sz):
        for col in range(sz):
            if final_grid[row][col] >= 2:
                count += 1
    print('Part 1 Answer:', count)

def part2(data):
    sz = max(sum([list(x.values()) for x in data], []))+1
    grid = [[0 for _ in range(sz)] for _ in range(sz)]
    for line in data:
        x1, y1, x2, y2 = list(line.values())
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2)+1):
                grid[x1][i] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)+1):
                grid[i][y1] += 1
        else:
            dx = x2-x1
            dy = y2-y1
            sx = dx // abs(dx)
            sy = dy // abs(dy)
            while x1!=x2 and y1!=y2:
                grid[x1][y1] += 1
                x1 += sx
                y1 += sy
            grid[x2][y2] += 1
    # optional: transpose cuz origin has to be at top left
    final_grid = sq_tranpose(grid)
    count = 0
    for row in range(sz):
        for col in range(sz):
            if final_grid[row][col] >= 2:
                count += 1
    print('Part 2 Answer:', count)

def main():
    data = []
    with open('input/005-hydrothermal-venture.txt') as f:
        lines = [x for x in f.readlines()]
        for line in lines:
            segment = {}
            points = line.strip().split('->')
            x1, y1 = points[0].split(',')
            x2, y2 = points[1].split(',')
            segment['x1'] = int(x1)
            segment['y1'] = int(y1)
            segment['x2'] = int(x2)
            segment['y2'] = int(y2)
            data.append(segment)  
    part1(data)
    part2(data)
       
if __name__ == '__main__':
    main()