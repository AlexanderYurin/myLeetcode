from typing import List


def sortByBits(arr: List[int]) -> List[int]:
	return sorted(arr, key=lambda x: (bin(x).count("1"), x))


if __name__ == '__main__':
	assert sortByBits(arr=[0, 1, 2, 3, 4, 5, 6, 7, 8]) == [0, 1, 2, 4, 8, 3, 5, 6, 7]
	assert sortByBits(arr=[1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == \
		   [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
