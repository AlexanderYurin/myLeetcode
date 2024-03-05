from typing import List


def minimumOperations(nums: List[int]) -> int:
	# hash_num = set()
	# count = 0
	# curr_sum = 1
	# nums.sort()
	# for num in nums:
	# 	if num > 0 and num not in hash_num:
	# 		count += 1
	# 		curr_sum += num - curr_sum
	# 		hash_num.add(num)
	# return count
	data = set(nums)
	return len(data) if 0 not in data else len(data) - 1


if __name__ == '__main__':
	assert minimumOperations(nums=[1, 5, 0, 3, 5]) == 3
