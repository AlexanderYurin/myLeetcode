from typing import List


def largestAltitude(gain: List[int]) -> int:
	for i in range(1, len(gain)):
		gain[i] = gain[i] + gain[i - 1]
	return max(0, *gain)


if __name__ == '__main__':
	assert largestAltitude(gain=[-5, 1, 5, 0, -7]) == 1
	assert largestAltitude(gain=[-4, -3, -2, -1, 4, 3, 2]) == 0
