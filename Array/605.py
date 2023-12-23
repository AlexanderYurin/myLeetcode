from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
	left = None
	mid = 0
	right = flowerbed[1]
	count = 0

	while mid < len(flowerbed):
		if left is None and flowerbed[mid] == 0 and right == 0:
			count += 1
			left = flowerbed[right]
			mid = right + 1
			right = mid + 1
			if right >= len(flowerbed):
				right = None






if __name__ == '__main__':
	assert canPlaceFlowers(flowerbed=[0, 0, 1, 0, 1], n=1) is True
	assert canPlaceFlowers(flowerbed=[0, 1, 0], n=1) is False
	assert canPlaceFlowers(flowerbed=[1, 0, 1], n=1) is False
	assert canPlaceFlowers(flowerbed=[1, 0, 0], n=1) is True
	assert canPlaceFlowers(flowerbed=[1, 0, 0, 1, 0], n=2) is True
