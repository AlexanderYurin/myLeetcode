def longestPalindrome(s: str) -> str:
	length_s = len(s)
	if length_s == 0:
		return s
	palindrome = s[0]
	for i in range(length_s):
		for j in range(i + 1, length_s):
			new_s = s[i:j + 1]
			if new_s == new_s[::-1] and len(palindrome) < len(new_s):
				palindrome = new_s

	return palindrome


assert longestPalindrome("") == ""
assert longestPalindrome("a") == "a"
assert longestPalindrome("babad") == "bab"
assert longestPalindrome("cbbd") == "bb"
