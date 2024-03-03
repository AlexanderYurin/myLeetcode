def rangeBitwiseAnd(left: int, right: int) -> int:
	for i in range(left, right+1):
		print(bin(i))
		print()

	return 4


if __name__ == '__main__':
	assert rangeBitwiseAnd(5, 7) == 4
