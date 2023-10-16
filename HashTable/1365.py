from typing import List


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
	n = {}
	res = []
	for i in range(len(nums)):
		if n.get(nums[i]) is None:
			n[nums[i]] = 0
			for j in range(len(nums)):
				if nums[j] < nums[i]:
					n[nums[i]] += 1
		res.append(n[nums[i]])
	return res


if __name__ == '__main__':
	assert smallerNumbersThanCurrent(nums=[8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]
