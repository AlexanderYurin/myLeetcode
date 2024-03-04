from typing import List


def findLeastNumOfUniqueInts(arr: List[int], k: int) -> int:
	nums = []
	c, i, j = 0, 0, 1

	while j < len(nums):
		if arr[i] == arr[j]:
			c += 1
			j += 1
			while arr[i] == arr[j]:
				j += 1
			else:
				i = j + 1
				j = i + 1
	return c


if __name__ == '__main__':
	assert findLeastNumOfUniqueInts(arr=[4, 3, 1, 1, 3, 3, 2], k=3) == 2
