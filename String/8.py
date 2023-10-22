def myAtoi(s: str) -> int:
	min_32bit, max_32bit = -2147483648, 2147483647
	result = ""
	sign = 1
	if len(s) == 0:
		return 0
	s = s.lstrip().split()[0]
	if s.startswith("-"):
		sign = -1
		s = s[1:]
	elif s.startswith("+"):
		s = s[1:]
	for elem in s:
		if elem.isdigit():
			result += elem
		else:
			break
	if len(result) != 0:
		result = int(result) * sign
	else:
		return 0

	if min_32bit > result:
		return min_32bit
	elif result > max_32bit:
		return max_32bit
	return result


assert myAtoi(s="42") == 42
assert myAtoi(s="   -42") == -42
assert myAtoi(s="-4193 with words") == -4193
assert myAtoi(s="-2147483649") == -2147483648
assert myAtoi(s="lkjlk") == 0
assert myAtoi(s="-91283472332") == -2147483648
assert myAtoi(s="-9.1283472332") == -9

