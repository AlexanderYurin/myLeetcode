def gcdOfStrings(str1: str, str2: str) -> str:
	var_word = (str2[:i] for i in range(1, len(str2)+1))  # O(n)
	words = (word for word in var_word if str1.replace(word, "") == "" and str2.replace(word, "") == "")
	return max(words, default="")


if __name__ == '__main__':
	assert gcdOfStrings(str1="ABCABC", str2="ABC") == "ABC"
	assert gcdOfStrings(str1="ABABAB", str2="ABAB") == "AB"
	assert gcdOfStrings(str1="LEET", str2="CODE") == ""
