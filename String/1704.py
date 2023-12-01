def halvesAreAlike(s: str) -> bool:
	vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
	a = [1 for sym in s[:len(s) // 2] if sym in vowels]
	b = [1 for sym in s[len(s) // 2:] if sym in vowels]
	return len(a) == len(b)


if __name__ == '__main__':
	assert halvesAreAlike(s="book") is True
