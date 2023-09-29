def defangIPaddr(address: str) -> str:
	return address.replace(".", "[.]")


assert defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"
