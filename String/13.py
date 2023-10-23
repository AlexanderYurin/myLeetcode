def romanToInt(s: str) -> int:
	roman = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000}
	result = 0
	for i in range(len(s)):
		if roman.get(s[i]) >= roman.get(s[i+1:i+2], 0):
			result += roman.get(s[i])
		else:
			result -= roman.get(s[i])
	return result


if __name__ == '__main__':
	assert romanToInt(s="LVIII") == 58
	assert romanToInt(s="MCMXCIV") == 1994
