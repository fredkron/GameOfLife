import random

import numpy as np


def make2DArray(rows, cols):
    arr = np.zeros(shape=(rows, cols))
    for x in range(0, rows):
        for y in range(0, cols):
            arr[x, y] = random.randint(0, 1)
    return arr


def count_neighbors(arr, x, y):
    ncount = 0
    for xn in [x - 1, x, x + 1]:
        for yn in [y - 1, y, y + 1]:
            if (xn < 0 or yn < 0 or 
            xn >= len(arr) or 
            yn >= len(arr)):
                pass
            elif xn == x and yn == y:
                pass
            elif arr[xn][yn] == 1:
                ncount += 1
    return ncount


def play(arr):
    new_arr = np.copy(arr)
    for x in range(0, len(arr)): 
        for y in range(0, len(arr)):
            if arr[x][y] == 0 and count_neighbors(arr, x, y) == 3:
                new_arr[x][y] = 1
            elif arr[x][y] == 1 and count_neighbors(arr, x, y) <= 2:
                new_arr[x][y] = 0
            elif arr[x][y] == 1 and count_neighbors(arr, x, y) > 3:
                new_arr[x][y] = 0
            else:
                pass
    return new_arr


def life():
    game = make2DArray(3, 3)
    for _ in range(10):
        print(game)
        game = play(game)


def main():
    life()


if __name__ == '__main__':
    main()