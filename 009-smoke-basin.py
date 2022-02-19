def explore_basin(basin, pos, data, bitmap):
    row = pos[0]
    col = pos[1]
    if row < 0 or row > len(data)-1 or \
       col < 0 or col > len(data[0])-1 or \
       data[row][col] == 9 or \
       bitmap[row][col] == 1:
        return
    else:
        basin.append(data[row][col])
        bitmap[row][col] = 1
    explore_basin(basin, [row-1, col], data, bitmap)
    explore_basin(basin, [row, col-1], data, bitmap)
    explore_basin(basin, [row, col+1], data, bitmap)
    explore_basin(basin, [row+1, col], data, bitmap)


def compute_low_points(data):
    low_points = []
    for row in range(len(data)):
        for col in range(len(data[0])):
            # STENCIL LAYOUT:
            #                ___________
            #               | row-1,col |
            #  _____________|           |_____________
            # | row,col-1      row,col      row,col+1 |
            # |_____________             _____________|
            #               | row+1,col |
            #               |___________|
            #
            if not (row-1 >= 0 and data[row-1][col] <= data[row][col] or
                    col-1 >= 0 and data[row][col-1] <= data[row][col] or
                    col+1 < len(data[0]) and data[row][col+1] <= data[row][col] or
                    row+1 < len(data) and data[row+1][col] <= data[row][col]):
                low_points.append([row, col])
    return low_points


def part1(data):
    sum = 0
    low_points = compute_low_points(data)
    for lp in low_points:
        sum += data[lp[0]][lp[1]] + 1
    print('Part 1 answer:', sum)


def part2(data):
    basins = []
    low_points = compute_low_points(data)
    bitmap = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]

    for lp in low_points:
        basin = []
        explore_basin(basin, lp, data, bitmap)
        basins.append(basin)

    basin_sizes = sorted([len(x) for x in basins], reverse=True)
    print('Part 2 answer:', basin_sizes[0] * basin_sizes[1] * basin_sizes[2])


def main():
    data = []
    with open('input/009-smoke-basin.txt') as f:
        for line in f.readlines():
            row = [int(x) for x in list(line.strip())]
            data.append(row)
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
