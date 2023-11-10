def freqAlphabets(s: str) -> str:
	i, j = 0, 3
	result = ""
	while i != len(s):
		if (s[i:j]).endswith("#"):
			result += chr(96 +int(s[i:j - 1]))
			i, j = j, j + 3
		else:
			result += chr(96 + int(s[i]))
			i += 1
			j += 1

	return result


if __name__ == '__main__':
	assert freqAlphabets(s="10#11#12") == "jkab"
	assert freqAlphabets(s="1326#") == "acz"
