favorite_word: str = input()
favorite_word_len: int = len(favorite_word)
symbols_counter: dict[str, int] = {}
for current_idx, current_symbol in enumerate(favorite_word):
    symbols_counter[current_symbol] = (
            symbols_counter.get(current_symbol, 0) + (current_idx + 1) * (favorite_word_len - current_idx)
    )

favorite_word_symbols_set: set[str] = set(favorite_word)
favorite_word_symbols_list: list[str] = list(favorite_word_symbols_set)
favorite_word_symbols_list.sort()
for symbol in favorite_word_symbols_list:
    print(f"{symbol}: {symbols_counter[symbol]}")
