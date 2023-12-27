from typing import List


def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
	return sorted(range(len(mat)), key=lambda x: mat[x].count(1))[:k]


if __name__ == '__main__':
	assert kWeakestRows(mat=[[1, 1, 0, 0, 0],
							 [1, 1, 1, 1, 0],
							 [1, 0, 0, 0, 0],
							 [1, 1, 0, 0, 0],
							 [1, 1, 1, 1, 1]],
						k=3) == [2, 0, 3]
