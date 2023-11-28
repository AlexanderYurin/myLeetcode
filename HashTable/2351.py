def repeatedCharacter(s: str) -> str:
	hash_set = set()

	for i in s:
		if i not in hash_set:
			hash_set.add(i)
		else:
			return i


if __name__ == '__main__':
	assert repeatedCharacter(s="abccbaacz") == "c"
	assert repeatedCharacter(s="abcdd") == "d"
