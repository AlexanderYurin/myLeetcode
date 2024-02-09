import itertools
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
	if len(nums) < 3:
		return []
	if len(nums) == 3:
		result = sum(nums)
		if result == 0:
			return [nums]
		return []
	result = set()
	nums.sort()
	arrays = filter(lambda x: x[0]+x[1]+x[2] == 0, itertools.combinations(nums, 3))
	for array in arrays:
		if array not in result:
			result.add(array)

	return result


if __name__ == '__main__':
	assert threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]) == [[-1, 0, 1], [-1, 2, -1]]
