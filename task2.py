from typing import TypeVar, Generic
from timeit import timeit

T = TypeVar('T')


def main():
    a1 = CycleBuffer1[int](65536)
    a2 = CycleBuffer2[int](65536)

    print(timeit(lambda: [a1.add(i) for i in range(65536)], number=1))  # 0.05662680009845644
    print(timeit(lambda: [a2.add(i) for i in range(65536)], number=1))  # 0.03702400007750839

    print(timeit(lambda: [a1.pop() for _ in range(65536)], number=1))  # 0.05778559995815158
    print(timeit(lambda: [a2.pop() for _ in range(65536)], number=1))  # 0.03662629995960742


class CycleBuffer1(Generic[T]):
    def __init__(self, size: int):
        self.size = size
        self.buffer = [None] * size
        self.head = -1
        self.tail = -1

    def add(self, value: T) -> None:
        if self.is_full():
            raise Exception("Buffer is full")

        if self.head == -1:
            self.head = 0
            self.tail = 0
            self.buffer[self.tail] = value
        elif self.tail < self.size - 1:
            self.tail += 1
            self.buffer[self.tail] = value
        else:
            self.buffer[0] = value
            self.tail = 0

    def pop(self) -> T:
        if self.is_empty():
            raise Exception("Buffer is empty")

        ret = self.buffer[self.head]
        self.buffer[self.head] = None

        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        elif self.head < self.size - 1:
            self.head += 1
        else:
            self.head = 0

        return ret

    def is_full(self) -> bool:
        return self.__len__() == self.size

    def is_empty(self) -> bool:
        return self.__len__() == 0

    def __len__(self) -> int:
        if self.head == -1:
            return 0
        elif self.tail > self.head:
            return self.tail - self.head + 1
        else:
            return self.size - (self.head - self.tail - 1)

    def __str__(self) -> str:
        return f"CycleBuffer1({self.buffer.__str__()})"


class CycleBuffer2(Generic[T]):
    def __init__(self, size: int):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.len = 0

    def add(self, value: T) -> None:
        if self.is_full():
            raise Exception("Buffer is full")

        self.buffer[(self.head + self.len) % self.size] = value
        self.len += 1

    def pop(self) -> T:
        if self.is_empty():
            raise Exception("Buffer is empty")

        ret = self.buffer[self.head]
        self.buffer[self.head] = None
        self.len -= 1
        self.head = (self.head + 1) % self.size

        return ret

    def is_full(self) -> bool:
        return self.len == self.size

    def is_empty(self) -> bool:
        return self.len == 0

    def __len__(self) -> int:
        return self.len

    def __str__(self) -> str:
        return f"CycleBuffer2({self.buffer.__str__()})"


if __name__ == "__main__":
    main()
