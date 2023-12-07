import numpy as np


def box_(r, c):
    start_row = r - r % 3
    start_col = c - c % 3
    return np.s_[start_row: start_row + 3, start_col: start_col + 3]


def to_set(arr):
    return set(arr.flatten())


def solve(sudoku):
    if (sudoku > 0).all():
        print(f'Finished!')
        print(sudoku)
        return True

    r, c = np.argwhere(sudoku == 0)[0]
    row = to_set(sudoku[r]) - {0}
    col = to_set(sudoku[:, c]) - {0}
    box = to_set(sudoku[box_(r, c)]) - {0}
    possible = sorted(digits - row - col - box)
    #print(r, c, possible)

    if not possible:
        return False

    for i in possible:
        sudoku[r, c] = i
        #print(f'Filling {i} in {r} {c}!')
        if solve(sudoku):
            return True
        else:
            #print(f'Backtracking {r} {c}')
            sudoku[r, c] = 0


sudokus = np.zeros(shape=(50, 9, 9), dtype=int)

with open("p096_sudoku.txt", 'r') as f:
    lines = f.readlines()
    for index, line in enumerate(lines):
        if index % 10:
            sudokus[index // 10, (index % 10) - 1] = [int(x)
                                                      for x in line.strip()]

digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}

for sudoku in sudokus:
    solve(sudoku)

print(sum(np.apply_along_axis(lambda x: x @
                              [100, 10, 1], 1, sudokus[:, 0, :3])))
