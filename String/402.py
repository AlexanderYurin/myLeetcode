def removeKdigits(num: str, k: int) -> str:
    max_num = num[:k]
    i = 1

    while i + k != len(num) + 1:
        cur_num = num[i:k+i]
        if cur_num == "0" and num.startswith(max_num + "0"):
            max_num =  max_num + "0"
            continue
        if int(cur_num) > int(max_num):
            max_num = cur_num
        i += 1
    result = num.replace(max_num, "")
    return result if result else "0"


if __name__ == '__main__':
    assert removeKdigits("1432219", 3) == "1219"
    assert removeKdigits("123", 3) == "0"
    assert removeKdigits(num = "10200", k = 1) == "200"

