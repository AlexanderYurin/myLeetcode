from functools import reduce


def xorOperation(n: int, start: int) -> int:
	return reduce(lambda x, y: x ^ y, [start + 2 * i for i in range(n)])


if __name__ == '__main__':
	assert xorOperation(n=5, start=0) == 8
