from typing import List


def equalPairs(grid: List[List[int]]) -> int:
    columns = [[row[i] for row in grid] for i in range(len(grid))]
    return 1




if __name__ == '__main__':
    assert equalPairs(grid=[[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]) == 3
