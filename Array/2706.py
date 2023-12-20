from typing import List


def buyChoco(prices: List[int], money: int) -> int:
	prices.sort()
	result = money - (prices[0] + prices[1])
	if result < 0:
		return money
	return result


if __name__ == '__main__':
	assert buyChoco(prices=[1, 2, 2], money=3) == 0
	assert buyChoco(prices=[3, 2, 3], money=3) == 3
