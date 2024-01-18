def climbStairs(n: int) -> int:
	return n if n == 2 and n == 3 else n % 2 + n // 2 * 2 + n % 3 + n // 3 * 3


if __name__ == '__main__':
	assert climbStairs(5) == 10
