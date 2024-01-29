def decodeString(s: str) -> str:
    stack = [s[0]]
    for i in range(1, len(s)):
        if s[i] == "]":
            chars = ""
            while 1:
                el = stack.pop()
                if el.isalpha():
                    chars = el + chars
                else:
                    stack.append(int(stack.pop()) * chars)
                    break
        else:
            if s[i].isdigit() and stack[-1].isdigit():
                stack.append(stack.pop() + s[i])
            elif s[i].isalpha() and stack[-1].isalpha():
                stack.append(stack.pop() + s[i])
            else:
                stack.append(s[i])

    return "".join(stack)


if __name__ == "__main__":
    assert decodeString("3[a2[c]]") == "accaccacc"
    assert decodeString("100[lee]") == 100 * "lee"
    assert decodeString("2[dc]3[bc]") == "dcdcbcbcbc"

    assert decodeString("2[dc]") == "dcdc"
