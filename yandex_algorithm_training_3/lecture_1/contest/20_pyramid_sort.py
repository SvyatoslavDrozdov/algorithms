class Heap:
    def __init__(self) -> None:
        self.heap: list[int] = []

    def add(self, new_value: int) -> None:
        self.heap.append(new_value)
        new_element_idx: int = len(self.heap) - 1

        while new_element_idx >= 1:
            father_idx: int = (new_element_idx - 1) // 2
            if self.heap[father_idx] < self.heap[new_element_idx]:
                self.heap[father_idx], self.heap[new_element_idx] = self.heap[new_element_idx], self.heap[father_idx]
                new_element_idx, father_idx = father_idx, new_element_idx
            else:
                break

    def get_max_element(self) -> int:
        max_value: int = self.heap[0]
        if len(self.heap) == 1:
            self.heap.pop()
            return max_value

        self.heap[0] = self.heap.pop()
        father_idx: int = 0
        first_son_idx: int = 1
        second_son_idx: int = 2

        while second_son_idx < len(self.heap):
            if self.heap[father_idx] >= max(self.heap[first_son_idx], self.heap[second_son_idx]):
                break

            if self.heap[first_son_idx] < self.heap[second_son_idx]:
                if self.heap[father_idx] < self.heap[second_son_idx]:
                    self.heap[father_idx], self.heap[second_son_idx] = self.heap[second_son_idx], self.heap[father_idx]
                    father_idx = second_son_idx
            else:
                if self.heap[father_idx] < self.heap[first_son_idx]:
                    self.heap[father_idx], self.heap[first_son_idx] = self.heap[first_son_idx], self.heap[father_idx]
                    father_idx = first_son_idx

            first_son_idx = 2 * father_idx + 1
            second_son_idx = 2 * father_idx + 2

        if first_son_idx < len(self.heap):
            if self.heap[father_idx] < self.heap[first_son_idx]:
                self.heap[father_idx], self.heap[first_son_idx] = self.heap[first_son_idx], self.heap[father_idx]

        return max_value


number_count: int = int(input())
numbers: list[int] = list(map(int, input().split()))
heap: Heap = Heap()
for number in numbers:
    heap.add(number)

sorted_numbers: list[int] = []
while heap.heap:
    sorted_numbers.append(heap.get_max_element())

print(*sorted_numbers[::-1])
