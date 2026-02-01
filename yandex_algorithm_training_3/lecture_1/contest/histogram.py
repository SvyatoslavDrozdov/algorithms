"""
Вовочка ломает систему безопасности Пентагона. Для этого ему понадобилось узнать, какие символы в секретных
зашифрованных посланиях употребляются чаще других. Для удобства изучения Вовочка хочет получить графическое
представление встречаемости символов. Поэтому он хочет построить гистограмму количества символов в сообщении.
Гистограмма — это график, в котором каждому символу, встречающемуся в сообщении хотя бы один раз, соответствует столбик,
высота которого пропорциональна количеству этих символов в сообщении.
"""
import sys


def plot_histogram(text: str) -> None:
    symbols_counter = {}
    for string in text:
        for symbol in string:
            if symbol == " " or symbol == "\n":
                continue
            symbols_counter[symbol] = symbols_counter.get(symbol, 0) + 1
    all_symbols = list(symbols_counter.keys())
    all_symbols.sort()

    max_high: int = 0
    for symbol in all_symbols:
        symbol_high: int = symbols_counter[symbol]
        if max_high < symbol_high:
            max_high = symbol_high

    for symbol_high in range(max_high, 0, -1):
        output_string_list: list[str] = []
        for symbol in all_symbols:
            if symbols_counter[symbol] >= symbol_high:
                output_string_list.append("#")
            else:
                output_string_list.append(" ")
        output_string: str = "".join(output_string_list)
        print(output_string)
    print("".join(all_symbols), end="")


text_example: str = sys.stdin.read()
plot_histogram(text_example)
