from typing import List


def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    keys = rooms[0]
    rooms = {i: rooms[i] for i in range(1, len(rooms))}

    for key in keys:
        if key in rooms:
            keys.extend(rooms[key])
            rooms.pop(key)

    return len(rooms) == 0




if __name__ == '__main__':
    assert canVisitAllRooms([[1,3],[3,0,1],[2],[0]]) is False
