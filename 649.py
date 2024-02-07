from collections import deque, Counter


def predictPartyVictory(senate: str) -> str:
    queue = list(senate)
    quantity_senators = Counter(senate)
    while len(quantity_senators) == 2:
        round_senate = deque(queue)
        queue.clear()
        while round_senate:
            left_senator = round_senate.popleft()
            right_senator = round_senate.popleft()
            if left_senator != right_senator:
                queue.append(left_senator)
                quantity_senators[right_senator] -= 1
                if quantity_senators[right_senator] < 1:
                    quantity_senators.pop(right_senator)
            else:
                queue.append(left_senator)
                round_senate.appendleft(right_senator)
    else:
        return "Radiant" if list(quantity_senators)[0] == "R" else "Dire"


if __name__ == '__main__':
    # assert predictPartyVictory(senate="RD") == "Radiant"
    assert predictPartyVictory(senate="DDRRR") == "Dire"
