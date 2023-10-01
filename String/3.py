def lengthOfLongestSubstring(s: str) -> int:
	lenght_s = len(s)
	result = s[0]
	for i in range(1, lenght_s):
		new_s = s[i]
		for j in range(i + 1, lenght_s):
			if s[j] in new_s:
				break
			new_s += s[j]
			if len(result) < len(s[i:j + 1]):
				result = new_s

	return len(result)


assert lengthOfLongestSubstring("bbbbbb") == 1
assert lengthOfLongestSubstring("abbabc") == 3
