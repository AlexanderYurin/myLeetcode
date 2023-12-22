def maxScore(s: str) -> int:
    max_score = 0
    left = [0 for _ in range(len(s)+1)]
    right = [0 for _ in range(len(s)+1)]
    for i in range(len(s)-1):
        if s[i] == "0":
            left[i] += left[i-1] + 1
        else:
            left[i] += left[i - 1]


    for i in range(len(s)-1, -1, -1):
        if s[i] == "1":
            right[i] += right[i+1] + 1
        else:
            right[i] += right[i + 1]



    return max_score


if __name__ == '__main__':
    assert maxScore(s="011101") == 5
