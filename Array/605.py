from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
	left = 0
	mid = 0
	right = 1
	count = 0

	while mid < len(flowerbed):
		if right >= len(flowerbed):
			right = mid
		if flowerbed[left] == 0 and \
			flowerbed[mid] == 0 and \
			flowerbed[right] == 0:
			flowerbed[mid] = 1
			count += 1
		left = mid
		mid = left + 1
		right = mid + 1

	return count >= n


if __name__ == '__main__':
	assert canPlaceFlowers(flowerbed=[0, 1, 0, 1, 0, 1, 0, 0], n=1) is True
	assert canPlaceFlowers(flowerbed=[0, 1, 0], n=1) is False
	assert canPlaceFlowers(flowerbed=[1, 0, 1], n=1) is False
	assert canPlaceFlowers(flowerbed=[1, 0, 0], n=1) is True
	assert canPlaceFlowers(flowerbed=[1, 0, 0, 1, 0], n=2) is False
