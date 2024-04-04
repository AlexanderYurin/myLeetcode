def lengthOfLastWord(s: str) -> int:
	return len(s.strip().split()[-1])


if __name__ == '__main__':
	assert lengthOfLastWord("Hello World") == 5
