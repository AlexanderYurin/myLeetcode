from typing import List


def longestOnes(nums: List[int], k: int) -> int:
	# i, j = 0, 0
	# max_cur = 0
	# cur = 0
	# count = k
	# while j < len(nums):
	# 	if nums[j] == 0:
	# 		count -= 1
	# 	if count == -1:
	# 		max_cur = max(cur, max_cur)
	# 		while 1:
	# 			i += 1
	# 			cur -= 1
	# 			if nums[i - 1] == 0:
	# 				count += 1
	# 				break
	# 	j += 1
	# 	cur += 1
	# return max(cur, max_cur)
	left = right = 0

	for right in range(len(nums)):
		# если мы встретим 0, мы уменьшим K
		if nums[right] == 0:
			k -= 1
		# иначе никакого влияния на K

		# если K < 0, то нам нужно переместить левую часть окна вперед
		# чтобы попытаться удалить лишние 0
		if k < 0:
			# если левый был нулем, то корректируем K
			if nums[left] == 0:
				k += 1
			# независимо от того, была ли у нас 1 или 0, мы можем сдвинуться влево на 1
            # если мы продолжаем видеть 1, окно продолжает двигаться как есть

			left += 1

	return right - left + 1


if __name__ == '__main__':
	assert longestOnes(nums=[1, 1, 1, 0, 0, 1], k=2) == 6
	assert longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2) == 6
	assert longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3) == 10
