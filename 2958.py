from collections import defaultdict, deque
from typing import List


def maxSubarrayLength(nums: List[int], k: int) -> int:
	count_nun_in_nums = defaultdict(int)
	good_subarray = deque()
	max_good_subarray = 0
	i = 0
	while i < len(nums):
		count_nun_in_nums[nums[i]] += 1
		if count_nun_in_nums[nums[i]] > k:
			max_good_subarray = max(max_good_subarray, len(good_subarray))
			while 1:
				num = good_subarray.popleft()
				count_nun_in_nums[num] -= 1
				if nums[i] == num:
					break
		good_subarray.append(nums[i])
		i += 1
	return max(max_good_subarray, len(good_subarray))


if __name__ == '__main__':
	assert maxSubarrayLength([1, 2, 2, 1, 3], 1) == 3
	assert maxSubarrayLength([1, 2, 1, 2], 1) == 2
	assert maxSubarrayLength(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2) == 6
	assert maxSubarrayLength(nums=[1, 2, 1, 2, 1, 2, 1, 2], k=1) == 2
	assert maxSubarrayLength([1, 2, 1, 2], 2) == 4
