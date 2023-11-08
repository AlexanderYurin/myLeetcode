def reversePrefix(word: str, ch: str) -> str:
	if ch not in set(word):
		return word
	index_ch = word.index(ch)
	result = word[index_ch::-1] + word[index_ch + 1:]
	return result


if __name__ == '__main__':
	assert reversePrefix(word="abcdefd", ch="d") == "dcbaefd"
	assert reversePrefix(word="xyxzxe", ch="z") == "zxyxxe"
	assert reversePrefix(word="abcd", ch="z") == "abcd"
