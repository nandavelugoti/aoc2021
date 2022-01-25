sq_tranpose = lambda m : [[row[i] for row in m] for i in range(len(m[0]))]

class Board:
    def __init__(self, rawdata):
        self.marked = [[0 for _ in range(5)] for _ in range(5)]
        self.data = []
        for line in rawdata:
            row = [int(x) for x in line.split()]
            self.data.append(row)

    def mark(self, number):
        for row in range(5):
            for col in range(5):
                if self.data[row][col] == number:
                    self.marked[row][col] = 1
                    return
    
    def _validate_board(self):
        # validate rows
        for row in self.marked:
            if sum(row) == 5:
                return True
        # validate columns
        for col in sq_tranpose(self.marked):
            if sum(col) == 5:
                return True
        return False

    def is_winner(self):
        return self._validate_board();
    
    def get_score(self, winning_number):
        unmarked = 0
        for row in range(5):
            for col in range(5):
                if self.marked[row][col] == 0:
                    unmarked += self.data[row][col]
        return unmarked*winning_number

def part1(data):
    seq = [int(x) for x in data['sequence'].split(',')]
    boards = [Board(x) for x in data['boards']]

    for num in seq:
        for board in boards:
            board.mark(num)
            if board.is_winner():
                print('Part 1 Answer:', board.get_score(num))
                return

def part2(data):
    seq = [int(x) for x in data['sequence'].split(',')]
    boards = [Board(x) for x in data['boards']]
    scores = []
    for num in seq:
        for board in boards:
            board.mark(num)
        
        for board in boards:
            if board.is_winner():
                scores.append(board.get_score(num))
                boards.remove(board)                
    print('Part 2 Answer:', scores[-1])

def main():
    data = {
        'sequence': '',
        'boards': []
    }
    with open('input/004-giant-squid.txt') as f:
        lines = [x for x in f.readlines()]
        data['sequence'] = lines[0].strip()

        count = 0
        board = []
        for line in lines[1:]:
            if line == '\n':
                continue
            if count == 5:
                data['boards'].append(board)
                #reset
                count = 0
                board = []
            board.append(line.strip())
            count += 1
        
    part1(data)
    part2(data)
       
if __name__ == '__main__':
    main()