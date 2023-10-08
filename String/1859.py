def sort_sentence(s: str) -> str:
	sort_text = list(map(lambda x: x[:len(x)-1], sorted(s.split(), key=lambda x: x[-1])))
	return " ".join(sort_text)


assert sortSentence(s="is2 sentence4 This1 a3") == "This is a sentence"
