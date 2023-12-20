def isValid(s: str) -> bool:
	i, j = 0, len(s)

	while i != len(s):
		if s[i] == "(":
			i_e = s[:j].index(")")
			if i_e <= j:
				j = i_e
			if i+1 == j:
				i, j = j, len(s)









if __name__ == '__main__':
	assert isValid(s="()") is True
	assert isValid(s="()[]{}") is True
	assert isValid(s="()[{}]") is True
