from collections import deque


class RecentCounter:

    # def __init__(self):
    #     self.queue = []
    #     self.requests = []
    #
    # def ping(self, t: int) -> int:
    #     self.queue.append(t)
    #     ping_range = [t - 3000, t]
    #     ping_range.sort()
    #     count = 0
    #     for i in self.queue:
    #         if ping_range[0] <= i <= ping_range[1]:
    #             count += 1
    #     self.requests.append(count)
    #     return count

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)


if __name__ == '__main__':
    obj = RecentCounter()
    param_1 = obj.ping(1)
    param_2 = obj.ping(100)
    param_3 = obj.ping(3001)
    param_4 = obj.ping(3002)

