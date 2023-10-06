def decodeMessage(key: str, message: str) -> str:
	from string import ascii_lowercase as al
	decode = {}
	count = 0
	for letter in key:
		if letter.isalpha() and decode.get(letter) is None:
			decode.setdefault(letter, al[count])
			count += 1
	code = ""
	for i in message:
		if not i.isalpha():
			code += i
		else:
			code += decode[i]
	return code


assert decodeMessage(key="the quick brown fox jumps over the lazy dog",
					 message="vkbs bs t suepuv") == "this is a secret"

assert decodeMessage(key="eljuxhpwnyrdgtqkviszcfmabo",
					 message="zwx hnfx lqantp mnoeius ycgk vcnjrdb") == "the five boxing wizards jump quickly"
