
def replaceDigits(s: str) -> str:
    answer = ""
    for i in range(len(s)):
        if s[i].isalpha():
            answer += s[i]
        else:
            answer += chr(ord(s[i-1]) + int(s[i]))
    return answer


if __name__ == '__main__':
    assert replaceDigits("a1c1e1") == "abcdef"
    assert replaceDigits("a1b2c3d4e") == "abbdcfdhe"
