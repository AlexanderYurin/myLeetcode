def customSortString(order: str, s: str) -> str:
	new_s = ""
	for elem in order:
		if elem in s:
			new_s += elem * s.count(elem)
			s = s.replace(elem, "")
	return new_s + s


assert customSortString(order="cbafg", s="abcd") == "cbad"
