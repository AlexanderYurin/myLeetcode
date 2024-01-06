from typing import List


def longestOnes(nums: List[int], k: int) -> int:
	i = j = 0
	max_cur = 0
	count = k
	while j <= len(nums):
		if nums[j] == 0:
			count -= 1
		if count < 0:
			max_cur = max(j - i, max_cur)
			i += 1
			if nums[i] == 0:
				count += 1
		j += 1
	return max_cur


if __name__ == '__main__':
	assert longestOnes(nums=[0, 0, 1, 0, 0, 1], k=2) == 4
