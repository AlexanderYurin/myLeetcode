from typing import List
from collections import Counter


def equalPairs(grid: List[List[int]]) -> int:
	rows = Counter(map(tuple, grid))
	columns = ((row[i] for row in grid) for i in range(len(grid)))
	count = 0
	for col in columns:
		count += rows[tuple(col)]
	return count


if __name__ == '__main__':
	assert equalPairs(grid=[[13, 13], [13, 13]]) == 4
	assert equalPairs(grid=[[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]) == 3
