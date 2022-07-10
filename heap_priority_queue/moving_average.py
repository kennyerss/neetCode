from collections import deque


class MovingAverage:

    def __init__(self, window_size):
        self.queue = deque()
        self.window_size = window_size
        self.total = 0

    def next(self, val):
        self.queue.append(val)
        self.total += val

        if len(self.queue) > self.window_size:
            self.total -= self.queue.pop(0)
        # round average to two digits
        avg = round(self.total / len(self.queue), 2)
        # print(avg)
        return avg


def main():
    ma2 = MovingAverage(2)
    print('Test 1:',
          [ma2.next(4), ma2.next(6)] ==
          [4.0, 5.0])

    ma2 = MovingAverage(2)
    print('Test 2:',
          [ma2.next(4), ma2.next(6), ma2.next(5)] ==
          [4.0, 5.0, 5.5])

    ma1 = MovingAverage(1)
    print('Test 3:',
          [ma1.next(1), ma1.next(0), ma1.next(1), ma1.next(0)] ==
          [1.0, 0.0, 1.0, 0.0])


main()
