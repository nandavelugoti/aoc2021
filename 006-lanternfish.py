# My first approch was to naively maintain
# all the states in an array which is not
# an optimized solution.

# But an interesting observation in the simulating
# all fishes with increasing no. of days is that,
# a pattern repeats itself after every 7 days (a week)!

# Finally, I refered to this for my solution:
# https://tinyurl.com/aoc2021day6.
# So, the idea is to just maintain count of fish
# based their state

class FishState:
    def __init__(self, fishes):
        # self.state holds the no. of fish
        # in i'th state for a given day
        self.state = [0 for _ in range(9)]
        for fish in fishes:
            self.state[fish] += 1

    def _advance_day(self):
        new_fish = self.state[0]
        for i in range(1, 9):
            self.state[i-1] = self.state[i]
        self.state[6] += new_fish
        self.state[8] = new_fish

    def advance_days(self, n):
        for i in range(n):
            self._advance_day()

    def count(self):
        return sum(self.state)

    def __str__(self):
        out = 'Count: '+str(self.count())+'\n'
        out += str(self.state)
        return out


def simulate(data, days):
    fstate = FishState(data)
    fstate.advance_days(days)
    print('After', days, 'days no. of fish is', fstate.count())


def main():
    data = []
    with open('input/006-lanternfish.txt') as f:
        line = f.readline()
        data = [int(x) for x in line.strip().split(',')]
    # Part 1:
    simulate(data, 80)
    # Part 2:
    simulate(data, 256)


if __name__ == '__main__':
    main()
