from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
	max_candies = max(candies)
	for i, candy in enumerate(candies):
		if max_candies <= candy + extraCandies:
			candies[i] = True
		else:
			candies[i] = False
	return candies


if __name__ == '__main__':
	assert kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3) == [True, True, True, False, True]
	assert kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1) == [True, False, False, False, False]
