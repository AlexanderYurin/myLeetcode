def isValid(s: str) -> bool:
	pairs = {"()", "{}", "[]"}
	stack = []
	for elem in s:
		if elem in "({[" or not stack:
			stack.append(elem)
		else:
			pair_elem = stack.pop() + elem
			if pair_elem not in pairs:
				return False
	else:
		return len(stack) == 0









if __name__ == '__main__':
	assert isValid(s="()") is True
	assert isValid(s="()[]{}") is True
	assert isValid(s="()[{}]") is True
