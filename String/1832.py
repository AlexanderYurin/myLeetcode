def checkIfPangram(sentence: str) -> bool:
	from string import ascii_lowercase as al
	return set(sentence) == set(al)





assert checkIfPangram(sentence = "thequickbrownfoxjumpsoverthelazydog") is True