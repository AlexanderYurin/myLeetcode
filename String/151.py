def reverseWords(s: str) -> str:
    return " ".join([word.strip() for word in s.split()[::-1]])


if __name__ == '__main__':
    assert reverseWords(s="the sky is blue") == "blue is sky the"
    assert reverseWords(s = "  hello world  ") == "world hello"
    assert reverseWords(s = "a good   example") == "example good a"
