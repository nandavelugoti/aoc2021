import re
from sre_parse import DIGITS


def part1(data):
    unique_patterns_len = {1: 2, 4: 4, 7: 3, 8: 7}
    counts = {1: 0, 4: 0, 7: 0, 8: 0}

    for entry in data:
        digits = entry.split('|')[1].strip().split(' ')
        for digit in digits:
            for key in unique_patterns_len.keys():
                if len(digit) == unique_patterns_len[key]:
                    counts[key] += 1

    print('Part 1 Answer:', sum(counts.values()))


def part2(data):
    """
    Reference mappings:
             aaaa  
            b    c
            b    c
             dddd 
            e    f
            e    f
             gggg
    """

    non_unique_patterns = {
        0: 'abcefg',
        2: 'acdeg',
        3: 'acdfg',
        5: 'abdfg',
        6: 'abdefg',
        9: 'abcdfg'
    }
    unique_patterns_len = {1: 2, 4: 4, 7: 3, 8: 7}
    unique_patterns = {1: '', 4: '', 7: '', 8: ''}
    results = []

    for entry in data:
        mappings = {
            'a': '',
            'b': '',
            'c': '',
            'd': '',
            'e': '',
            'f': '',
            'g': '',
        }

        signals = entry.split('|')[0].strip().split(' ')
        digits = entry.split('|')[1].strip().split(' ')

        for signal in signals:
            if len(signal) in unique_patterns_len.values():
                unique_patterns[list(unique_patterns_len.keys())[list(
                    unique_patterns_len.values()).index(len(signal))]] = signal
        five_segment_patterns = [x for x in signals if len(x) == 5]
        six_segment_patterns = [x for x in signals if len(x) == 6]

        # segments related to digit 1
        mappings['c'] = unique_patterns[1][0]
        mappings['f'] = unique_patterns[1][1]

        # segments related to digit 7
        mappings['a'] = unique_patterns[7].replace(
            unique_patterns[1][0], '').replace(unique_patterns[1][1], '')

        # segments related to digit 4
        choices = unique_patterns[4].replace(
            unique_patterns[1][0], '').replace(unique_patterns[1][1], '')

        # segments related to digits 2, 3, 5
        for ch in choices:
            if (ch in five_segment_patterns[0] and
                ch in five_segment_patterns[1] and
                    ch in five_segment_patterns[2]):
                mappings['d'] = ch
            else:
                mappings['b'] = ch

        remaining = [
            x for x in 'abcdefg' if x not in ''.join(mappings.values())]

        # segments related to digits 0, 6, 9
        for ch in remaining:
            if (ch not in six_segment_patterns[0] or
                ch not in six_segment_patterns[1] or
                    ch not in six_segment_patterns[2]):
                mappings['e'] = ch
            else:
                mappings['g'] = ch

        inverted_mappings = dict((v, k) for k, v in mappings.items())

        output = []
        for digit in digits:
            if len(digit) in unique_patterns_len.values():
                output.append(list(unique_patterns_len.keys())[
                              list(unique_patterns_len.values()).index(len(digit))])
            else:
                success = False
                while not success:
                    remapped_digit = ''
                    for c in digit:
                        remapped_digit += inverted_mappings[c]
                    for key in non_unique_patterns.keys():
                        if len(remapped_digit) == len(non_unique_patterns[key]) and\
                                sorted(remapped_digit) == sorted(non_unique_patterns[key]):
                            output.append(key)
                            success = True
                            break
                    if not success:
                        # The initial assumptions for segments c, f (for digit 1)
                        # is found to be wrong. So swap them.
                        # This is done only once
                        tmp = mappings['c']
                        mappings['c'] = mappings['f']
                        mappings['f'] = tmp
                        inverted_mappings = dict((v, k)
                                                 for k, v in mappings.items())
        results.append(int(''.join([str(x) for x in output])))
    print('Part 2 Answer:', sum(results))


def main():
    data = []

    with open('input/008-seven-segment-search.txt') as f:
        data = f.readlines()

    part1(data)
    part2(data)


if __name__ == '__main__':
    main()
