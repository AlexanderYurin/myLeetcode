import re


def strStr(text: str, pattern: str) -> int:
	# pattern = fr"({needle})"
	# index = re.search(pattern=pattern, string=haystack)
	# return index.start() if index is not None else -1
	pattern_hash = hash(pattern)
	window_hash = hash(text[:len(pattern)])
	for i in range(len(text) - len(pattern) + 1):
		if pattern_hash == window_hash and text[i:i + len(pattern)] == pattern:
			return i
		window_hash = hash(text[i + 1:i + len(pattern) + 1])

	return -1





if __name__ == '__main__':
	assert strStr("ssadbutsad", "sad") == 1
	assert strStr("leetcode", "leeto") == -1
