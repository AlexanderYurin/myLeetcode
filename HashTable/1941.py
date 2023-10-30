def areOccurrencesEqual(s: str) -> bool:
    hash_set = set(s)
    count = s.count(s[0])
    for letter in hash_set:
        if count != s.count(letter):
            return False
    return True







if __name__ == '__main__':
    assert areOccurrencesEqual(s="abacbc") is True
    assert areOccurrencesEqual(s="fhojjkontbncdhwxbnexplclvjyexzsvqyyhpfpnvhdskuhkuoihiqgalklqketjikdlgrawhfo") is False
