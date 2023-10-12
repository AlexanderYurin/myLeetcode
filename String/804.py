from typing import List


def uniqueMorseRepresentations(words: List[str]) -> int:
	from string import ascii_lowercase as al

	code_morze = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
				  "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
	res = []
	for i in range(len(words)):
		res.append("")
		for j in words[i]:
			elem = al.index(j)
			res[i] += code_morze[elem]
	return len(set(res))

if __name__ == '__main__':
	assert uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"]) == 2
	assert uniqueMorseRepresentations(words = ["a"]) == 1