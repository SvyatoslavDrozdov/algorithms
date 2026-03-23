def lengthOfLongestSubstring(s: str) -> int:
    first_symbol_idx: int = 0
    last_symbol_idx: int = 0
    current_symbols_set: dict[str, int] = {}
    current_symbols_set[s[last_symbol_idx]] = 1
    need_to_remove_symbol: str | None = None

    longest_substring_len: int = 0

    while last_symbol_idx < len(s) - 1:
        if need_to_remove_symbol:
            current_symbols_set[s[first_symbol_idx]] -= 1
            first_symbol_idx += 1
            if current_symbols_set[need_to_remove_symbol] == 1:
                need_to_remove_symbol = None

        else:
            longest_substring_len = max(longest_substring_len, last_symbol_idx - first_symbol_idx + 1)
            last_symbol_idx += 1
            current_symbols_set[s[last_symbol_idx]] = current_symbols_set.get(s[last_symbol_idx], 0) + 1
            if current_symbols_set[s[last_symbol_idx]] > 1:
                need_to_remove_symbol = s[last_symbol_idx]

    while first_symbol_idx < len(s) - 1 and need_to_remove_symbol:
        current_symbols_set[s[first_symbol_idx]] -= 1
        first_symbol_idx += 1
        if current_symbols_set[need_to_remove_symbol] == 1:
            need_to_remove_symbol = None

    longest_substring_len = max(longest_substring_len, last_symbol_idx - first_symbol_idx + 1)

    return longest_substring_len


print(lengthOfLongestSubstring("pwwkew"))
