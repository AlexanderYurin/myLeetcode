from typing import List


def rearrangeArray(nums: List[int]) -> List[int]:
	def merge_array(nums_1, nums_2):
		i_1 = i_2 = 0
		result = []
		while i_1 < len(nums_1) and i_2 < len(nums_2):
			result.append(nums_1[i_1])
			result.append(nums_2[i_2])
			i_1 += 1
			i_2 += 1
		return result + nums_1[i_1:] + nums_1[i_2:]

	nums_1 = []
	nums_2 = []

	for num in nums:
		if abs(num) == num:
			nums_1.append(num)
		else:
			nums_2.append(num)

	return merge_array(nums_1, nums_2)


if __name__ == '__main__':
	assert rearrangeArray([3, 1, -2, -5, 2, -4]) == [3, -2, 1, -5, 2, -4]
