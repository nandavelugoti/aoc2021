legal = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


class Stack():
    def __init__(self):
        self._stack = []
    
    def push(self, val):
        self._stack.append(val)
    
    def pop(self):
        return self._stack.pop()
    
    def size(self):
        return len(self._stack)

    def __str__(self):
        return str(self._stack)


def part1(data):
    rubrick_corrupted = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    count = {
        ')': 0,
        ']': 0,
        '}': 0,
        '>': 0
    }
    for line in data:
        stack = Stack()
        for ch in line:
            if ch in legal.keys():
                stack.push(legal[ch])
            else:
                if stack.size() <= 0 or ch != stack.pop():
                    count[ch] += 1
                    break
    score = sum([rubrick_corrupted[k]*count[k] for k in rubrick_corrupted.keys()])
    print('Part 1 Answer:', score)


def part2(data):
    rubrick_incomplete = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    scores = []
    for line in data:
        stack = Stack()
        corrupted = False
        for ch in line:
            if ch in legal.keys():
                stack.push(legal[ch])
            else:
                if stack.size() <= 0 or ch != stack.pop():
                    corrupted = True
                    break
        if not corrupted and stack.size() > 0:
            score = 0
            while stack.size() > 0:
                score *= 5
                score += rubrick_incomplete[stack.pop()]
            scores.append(score)
    scores.sort()
    print("Part 2 Answer:", scores[len(scores)//2])


def main():
    data = []
    with open('input/010-syntax-scoring.txt') as f:
        data = [x.strip() for x in f.readlines()]
    part1(data)
    part2(data)


if __name__ == '__main__':
    main()