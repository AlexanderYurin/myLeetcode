def reverse(x: int) -> int:
	min_32bit, max_32bit = -2147483648, 2147483647
	num = int(str(abs(x))[::-1])
	if num < min_32bit or num > max_32bit:
		return 0
	if x < 0:
		return -1 * num
	return num


if __name__ == '__main__':
	assert reverse(120) == 21
	assert reverse(-120) == -21
	assert reverse(1534236469) == 0
