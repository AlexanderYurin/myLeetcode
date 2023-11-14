from typing import List


def plusOne(digits: List[int]) -> List[int]:
	# 1 решение
	# count = -1
	# while abs(count) <= len(digits):
	#     digits[count] += 1
	#     if digits[count] == 10:
	#         digits[count] = 0
	#         if abs(count) == len(digits):
	#             digits.insert(0, 1)
	#             return digits
	#         count -= 1
	#     else:
	#
	#         return digits
	# 2 решение
	# for i in range(len(digits) - 1, -1, -1):
	#     if digits[i] == 9:
	#         digits[i] = 0
	#     else:
	#         digits[i] = digits[i] + 1
	#         return digits
	# return [1] + digits
	return list(map(int, (str(int("".join(map(str, digits))) + 1))))


if __name__ == '__main__':
	assert plusOne([9, 9, 9, 9]) == [1, 0, 0, 0, 0]
