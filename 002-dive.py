def part1(data):
    pos = 0
    depth = 0
    for step in data:
        inst, val = step.split()
        val = int(val)
        if (inst == 'forward'):
            pos += val
        elif (inst == 'up'):
            depth -= val
        elif(inst == 'down'):
            depth += val
        else:
            print('Invalid instruction in data!')
            exit(1)
    print("Part 1 Answer:", pos*depth)


def part2(data):
    pos = 0
    depth = 0
    aim = 0
    for step in data:
        inst, val = step.split()
        val = int(val)
        if (inst == 'forward'):
            pos += val
            depth += aim*val
        elif (inst == 'up'):
            aim -= val
        elif(inst == 'down'):
            aim += val
        else:
            print('Invalid instruction in data!')
            exit(1)
    print("Part 2 Answer:", pos*depth)


def main():
    data = []
    with open('input/002-dive.txt') as f:
        data = [x for x in f.readlines()]

    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
