def detectCapitalUse(word: str) -> bool:
	if word == word.upper() or word == word.lower() or word == word.capitalize():
		return True
	else:
		return False


if __name__ == '__main__':
	assert detectCapitalUse(word="UsA") is False
	assert detectCapitalUse(word="USA") is True
	assert detectCapitalUse(word="Usa") is True
	assert detectCapitalUse(word="usa") is True
