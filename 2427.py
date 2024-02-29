def commonFactors(a: int, b: int) -> int:
	return len([1 for num in list(range(2, min(a, b) + 1)) if a % num == 0 and b % num == 0]) + 1
