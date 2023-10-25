def countPoints(rings: str) -> int:
	hash_table = {}
	j = 1
	i = 0

	while j <= len(rings):
		hash_table.setdefault(rings[j], set())
		hash_table[rings[j]].add(rings[i])
		j += 2
		i += 2
	result = list(filter(lambda x: len(x) == 3, hash_table.values()))
	return len(result)






if __name__ == '__main__':
	assert countPoints(rings = "B0R0G0R9R0B0G0") == 1
