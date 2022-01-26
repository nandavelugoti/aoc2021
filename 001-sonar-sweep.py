def part1(data):
    count = 0
    prev = data[0]
    for x in data:
        if x > prev:
            count += 1
        prev = x
    print('Part 1 Answer:', count)


def part2(data):
    count = 0
    prev = sum(data[:3])
    for i in range(len(data)):
        s = sum(data[i:i+3])
        if s > prev:
            count += 1
        prev = s
    print('Part 2 Answer:', count)


def main():
    data = []
    with open('input/001-sonar-sweep.txt') as f:
        data = [int(x) for x in f.readlines()]

    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
