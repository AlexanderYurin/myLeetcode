from typing import List
import itertools


def arithmeticTriplets(nums: List[int], diff: int) -> int:
	seen = set()
	cnt = 0
	for num in nums:
		if num - diff in seen and num - diff * 2 in seen:
			cnt += 1
		seen.add(num)
	return cnt


if __name__ == '__main__':
	assert arithmeticTriplets(nums=[0, 1, 4, 6, 7, 10], diff=3) == 2
