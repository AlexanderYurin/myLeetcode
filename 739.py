from collections import defaultdict
from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
	i, j, day = 0, 1, 1
	days = []
	cache = {}
	while i != len(temperatures) - 1:
		if temperatures[i] in cache and cache[temperatures[i]] > i:
			days.append(cache[temperatures[i]] - i)
		else:
			if temperatures[i] < temperatures[j]:
				days.append(day)
				cache[temperatures[i]] = j
				i += 1
				day = 1
				j = i + 1

			elif j == len(temperatures) - 1:
				days.append(0)
				i += 1
				j = i + 1
				day = 1
			else:
				j += 1
				day += 1
	return days + [0]


if __name__ == '__main__':
	# assert dailyTemperatures([100, 74, 75, 71, 69, 72, 76, 73]) == [0, 1, 4, 2, 1, 1, 0, 0]
	assert dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
