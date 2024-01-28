# def climbStairs(n: int) -> int:
# 	return 4
#
#
# if __name__ == '__main__':
# 	assert climbStairs(5) == 10
def move_zeros(array):
	for i in range(len(array)):
		for j in range(1, len(array) - i):
			if array[j-1] == 0:
				array[j], array[j - 1] = array[j - 1], array[j]
	return [num for num in array if num != 0] + [0 for _ in range(array.count(0))]


print(move_zeros([1, 1, 2, 1, 3, 0, 0]))
