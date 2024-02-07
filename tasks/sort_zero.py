from collections import deque


def sort_zero(array):
	result = deque()
	for i in range(len(array)-1, -1, -1):
		if array[i] == 0:
			result.append(array[i])
		else:
			result.appendleft(array[i])
	return list(result)


if __name__ == '__main__':
	assert sort_zero([0, 0, 1, 2, 3]) == [1, 2, 3, 0, 0]