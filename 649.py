from collections import deque, Counter


def predictPartyVictory(senate: str) -> str:
    queue = deque(senate)
    count_senate = Counter(senate)
    while len(count_senate) == 2:
        senator = queue.popleft()
        senator_right = queue.popleft()
        if senator != senator_right:
            queue.append(senator)
            count_senate[senator_right] -= 1
            if count_senate[senator_right] < 1:
                count_senate.pop(senator_right)
        else:
            count = 2
            queue += [senator, senator_right]
            while count != 0:
                if len(count_senate) == 1:
                    break
                senator_right = queue.popleft()
                if senator_right == senator:
                    queue.append(senator)
                    count += 1
                else:
                    count -= 1
                    count_senate[senator_right] -= 1
                    if count_senate[senator_right] < 1:
                        count_senate.pop(senator_right)
    else:
        return "Radiant" if list(count_senate)[0] == "R" else "Dire"


if __name__ == '__main__':
    assert predictPartyVictory(senate="RRDDDDDDDRRDRRDDRRRR") == "Dire"
    assert predictPartyVictory(senate="DDRRR") == "Dire"
    assert predictPartyVictory(senate="RDD") == "Dire"
