from typing import List


def numIdenticalPairs(nums: List[int]) -> int:
	return len([(i, j)
				for i in range(len(nums))
				for j in range(i, len(nums))
				if nums[i] == nums[j] and i < j])


if __name__ == '__main__':
	assert numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]) == 4
	assert numIdenticalPairs(nums=[1, 1, 1, 1]) == 6
