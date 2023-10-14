from typing import List


def getConcatenation(nums: List[int]) -> List[int]:
	new_nums = nums[:]
	return nums + new_nums


if __name__ == '__main__':
	assert getConcatenation([1, 2]) == [1, 2, 1, 2]
