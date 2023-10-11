def capitalizeTitle(title: str) -> str:
	return " ".join((i.capitalize() if len(i) > 2 else i.lower() for i in title.split()))


if __name__ == '__main__':
	assert capitalizeTitle(title="First leTTeR of EACH Word") == "First Letter of Each Word"
