
def removeOuterParentheses(s: str) -> str:
    # res = ""
    # count = 0
    # while count != len(s):
    #     for i in range(count+1, len(s)):
    #         if s[count] == "(" and s[i] == ")" and s[i+1] == "(" :
    #             res += s[count+1:i]
    #             count = i +1
    #             break
    res, opened = [], 0
    for c in s:
        if c == '(' and opened > 0: res.append(c)
        if c == ')' and opened > 1: res.append(c)
        opened += 1 if c == '(' else -1
        sorted()
    return "".join(res)







if __name__ == '__main__':
    assert removeOuterParentheses(s="(()())(())") == "()()()"
    assert removeOuterParentheses(s="(()())(())(()(()))") == "()()()()(())"
