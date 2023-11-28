from collections import Counter


def firstUniqChar(s: str) -> int:
    chars = Counter(s)
    for char in s:
        if chars[char] == 1:
            return chars[char]
    else:
        return -1


if __name__ == '__main__':
    assert firstUniqChar(s="leetcode") == 0
    assert firstUniqChar(s="loveleetcode") == 2
    assert firstUniqChar(s="aabb") == -1
