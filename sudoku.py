import collections
import random
import copy as copy_module

Location = collections.namedtuple('Location', 'row column')

class Sudoku:

    def _find_random_occupied_location(self):
        r = random.randint(0,8)
        c = random.randint(0,8)
        while self.board[r][c] == 0:
            r = random.randint(0,8)
            c = random.randint(0,8)
        return Location(row=r, column=c)

    def _generate(self):
        self.solve(shuffle_candidates=True)

        counter = 5
        while counter > 0:
            location = self._find_random_occupied_location()
            number = self.remove_number(location)
            x = self.copy()
            
            solutions = self._solutions()
            self = x
            if solutions != 1:
                self.add_number(number, location)
                counter += 1
        print(self)


    def __init__(self):
        self.board = [[0] * 9 for _ in range(9)]
        self.rows = [[True] * 9 for _ in range(9)]
        self.columns =[[True] * 9 for _ in range(9)]
        self.boxes = [[[True] * 9 for _ in range(3)] for _ in range(3)]
        self._generate()
        print(self)
    
    def is_valid(self, number, location):
        return self.board[location.row][location.column] == 0 and \
               self.rows[location.row][number - 1] and \
               self.columns[location.column][number - 1] and \
               self.boxes[location.row // 3][location.column // 3][number - 1]
    
    def add_number(self, number, location):
        if self.is_valid(number, location):
            self.board[location.row][location.column] = number
            self.rows[location.row][number - 1] = False
            self.columns[location.column][number - 1] = False
            self.boxes[location.row // 3][location.column // 3][number - 1] = False
        else:
            raise ValueError
    
    def remove_number(self, location):
        number = self.board[location.row][location.column]
        if number != 0:
            self.board[location.row][location.column] = 0
            self.rows[location.row][number - 1] = True
            self.columns[location.column][number - 1] = True
            self.boxes[location.row // 3][location.column // 3][number - 1] = True
            return number
        else:
            raise ValueError
    
    def __str__(self):
        s = ''
        for row in self.board:
            s += str(row)
            s += '\n'
        return s
    
    def _find_empty(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    return Location(row = r, column = c)
        return None
    
    def _find_candidates(self, location):
        candidates = []
        for i in range(1, 10):
            if self.is_valid(i, location):
                candidates.append(i)
        return candidates
    
    def solve(self, shuffle_candidates=False):
        location = self._find_empty()
        if not location:
            return True
        candidates = self._find_candidates(location)

        if shuffle_candidates:
            random.shuffle(candidates)

        for candidate in candidates:
            self.add_number(candidate, location)
            if self.solve(shuffle_candidates=shuffle_candidates):
                return True
            self.remove_number(location)

        return False
    
    def _solutions(self):
        solutions = 0
        location = self._find_empty()
        if not location:
            return 1
        candidates = self._find_candidates(location)

        for candidate in candidates:
            self.add_number(candidate, location)
            solutions += self._solutions()
            if solutions > 1:
                return 2
            self.remove_number(location)

        return solutions
    
    def copy(self):
        return copy_module.deepcopy(self)



    





