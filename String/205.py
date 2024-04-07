from collections import Counter


def isIsomorphic(s: str, t: str) -> bool:
    return all(j[1] == i[1] for i, j, in zip(Counter(s).items(), Counter(t).items()))


if __name__ == '__main__':
    assert isIsomorphic("egg", "vpp") is True
    assert isIsomorphic("bbbaaaba", "aaabbbba") is False
    assert isIsomorphic("paper", "title") is True