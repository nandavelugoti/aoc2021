def main():
    data = []
    with open('input/007-the-treachery-of-whales.txt') as f:
        line = f.readline()
        data = [int(x) for x in line.strip().split(',')]

    # Part 1
    costs = []
    for align in range(max(data)):
        fuel = 0
        for pos in data:
            delta = abs(align - pos)
            fuel += delta
        costs.append(fuel)
    print("Part 1 Answer: ", min(costs))

    # Part 2
    costs = []
    for align in range(max(data)):
        fuel = 0
        for pos in data:
            delta = abs(align - pos)
            fuel += (delta*(delta+1))//2  # n natural numbers sum
        costs.append(fuel)
    print("Part 2 Answer: ", min(costs))


if __name__ == '__main__':
    main()
