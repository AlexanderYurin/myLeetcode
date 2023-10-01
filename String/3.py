def lengthOfLongestSubstring(s: str) -> int:
	length_s = len(s)
	if length_s < 1:
		return 0
	result = s[0]
	for i in range(length_s):
		new_s = s[i]
		for j in range(i + 1, length_s):
			if s[j] in new_s:
				break
			else:
				new_s += s[j]
		if len(result) < len(new_s):
			result = new_s
	return len(result)


assert lengthOfLongestSubstring("") == 0
assert lengthOfLongestSubstring(" ") == 1
assert lengthOfLongestSubstring("au") == 2
assert lengthOfLongestSubstring("abbabc") == 3
