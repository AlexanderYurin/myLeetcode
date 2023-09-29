def numJewelsInStones(jewels: str, stones: str) -> int:
	return sum((stones.count(i) for i in jewels))


assert numJewelsInStones("A", "aa") == 0
assert numJewelsInStones("a", "aa") == 2
