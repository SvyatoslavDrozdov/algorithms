"""
Красотой строки назовем максимальное число идущих подряд одинаковых букв. Сделайте данную вам строку как можно более
красивой, если вы можете сделать не более k операций замены символа.
"""
import sys


def get_max_beauty_of_string(string: str, max_substitutions_number: int) -> int:
    max_beauty: int = 0
    for letter in set(string):
        wrong_letters: int = 0
        left_idx: int = 0
        for right_idx, symbol in enumerate(string):
            if symbol != letter:
                wrong_letters += 1
            while wrong_letters > max_substitutions_number:
                left_idx += 1
                if string[left_idx - 1] != letter:
                    wrong_letters -= 1
            interval_size: int = right_idx - left_idx + 1
            if max_beauty < interval_size:
                max_beauty = interval_size
    return max_beauty


max_substitutions_number_example: int = int(sys.stdin.readline())
string_example: str = sys.stdin.readline().strip()
print(get_max_beauty_of_string(string_example, max_substitutions_number_example))
