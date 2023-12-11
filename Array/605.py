from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
	row = [bed for bed in flowerbed[::2]]
	if len(flowerbed) % 2 != 0:
		return row.count(0) == n
	return row.count(0) - 1 == n










if __name__ == '__main__':
	assert canPlaceFlowers(flowerbed=[0, 0, 1, 0, 1], n=1) is True
	assert canPlaceFlowers(flowerbed=[1, 0, 0, 0, 0, 1], n=2) is False
