from collections import Counter


def minSteps(s: str, t: str) -> int:
    count = 0
    letters_s = Counter(s)
    letters_t = Counter(t)

    letters = letters_s - letters_t + (letters_t - letters_s)

    return sum(letters.values())

    # for letter in letters_s:
    #     if letter in letters_t:
    #         if letters_s[letter] < letters_t[letter]:
    #             count += letters_t[letter] - letters_s[letter]
    #     else:
    #         count += letters_s[letter]
    #
    # for letter in letters_t:
    #     if letter in letters_s:
    #         if letters_t[letter] < letters_s[letter]:
    #             count += letters_s[letter] - letters_t[letter]
    #     else:
    #         count += letters_t[letter]
    #
    # return count


if __name__ == '__main__':
    assert minSteps(s="leetcode", t="coats") == 7
    assert minSteps(s="leetcode", t="leetcode") == 0
    assert minSteps(s="leet", t="leetcode") == 4
    assert minSteps(s="lee", t="l") == 2
