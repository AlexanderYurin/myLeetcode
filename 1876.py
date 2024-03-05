def countGoodSubstrings(s: str) -> int:
	return len([1 for i in range(0, len(s)) if len(set(s[i:i + 3])) == 3])


if __name__ == '__main__':
	assert countGoodSubstrings(s="xyzzaz") == 1
	assert countGoodSubstrings(s="aababcabc") == 4
