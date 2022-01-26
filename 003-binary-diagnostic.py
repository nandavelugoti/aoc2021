def part1(data):
    sz = len(data[0].strip())
    zeros = [0]*sz
    ones = [0]*sz
    for b in data:
        for i in range(sz):
            if b[i] == '0':
                zeros[i] += 1
            else:
                ones[i] += 1
    gamma_rate = int(
        ''.join(
            [('0' if zeros[i] > ones[i] else '1')
             for i in range(sz)]
        ),
        2
    )
    epsilon_rate = int(
        ''.join(
            [('0' if zeros[i] < ones[i] else '1')
             for i in range(sz)]
        ),
        2
    )
    print('Part 1 Answer:', gamma_rate*epsilon_rate)


def part2(data):
    sz = len(data[0].strip())
    O2_data = data[:]
    CO2_data = data[:]

    i = 0
    while len(O2_data) > 1 and i < sz:
        zero_count = 0
        one_count = 0
        for b in O2_data:
            if b[i] == '0':
                zero_count += 1
            else:
                one_count += 1
        O2_data = [x for x in O2_data
                   if x[i] == ('0' if zero_count > one_count else '1')]
        i += 1

    i = 0
    while len(CO2_data) > 1 and i < sz:
        zero_count = 0
        one_count = 0
        for b in CO2_data:
            if b[i] == '0':
                zero_count += 1
            else:
                one_count += 1
        CO2_data = [x for x in CO2_data
                    if x[i] == ('1' if one_count < zero_count else '0')]
        i += 1

    O2_gen_rating = int(O2_data[0].strip(), 2)
    CO2_scrub_rating = int(CO2_data[0].strip(), 2)

    print('Part 2 Answer:', O2_gen_rating*CO2_scrub_rating)


def main():
    data = []
    with open('input/003-binary-diagnostic.txt') as f:
        data = [x for x in f.readlines()]

    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
