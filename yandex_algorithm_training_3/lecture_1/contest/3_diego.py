from typing import Callable

all_diego_sticker_count: int = int(input())
all_diego_stickers: list[int] = list(map(int, input().split()))

diego_stickers: list[int] = []
for sticker in set(all_diego_stickers):
    diego_stickers.append(sticker)
diego_stickers.sort()

collector_count: int = int(input())
min_not_valuable_sticker: list[int] = list(map(int, input().split()))


def binary_search(numbers: list[int], predicate: Callable[[int], bool]) -> int:
    left: int = 0
    right: int = len(numbers)
    while left < right:
        middle: int = (left + right) // 2
        if predicate(numbers[middle]):
            right = middle
        else:
            left = middle + 1
    return left


def get_comparison_function(comparison_value: int) -> Callable[[int], bool]:
    def is_greater(value: int) -> bool:
        return value >= comparison_value

    return is_greater


for min_not_valuable_sticker_number in min_not_valuable_sticker:
    critical_diego_idx: int = binary_search(diego_stickers, get_comparison_function(min_not_valuable_sticker_number))
    print(critical_diego_idx)
