def longestPalindrome(s: str) -> str:
    max_palindromic_substring_len: int = 1
    best_left_idx: int = 0
    best_right_idx: int = 0

    for integer_center_position in range(len(s)):
        left: int = integer_center_position
        right: int = integer_center_position
        while left > 0 and right < len(s) - 1:
            if s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
            else:
                break
        if right - left + 1 > max_palindromic_substring_len:
            best_left_idx = left
            best_right_idx = right
            max_palindromic_substring_len = right - left + 1

    for between_numbers_center_position in range(len(s) - 1):
        left: int = between_numbers_center_position
        right: int = between_numbers_center_position + 1
        if s[left] == s[right]:
            while left > 0 and right < len(s) - 1:
                if s[left - 1] == s[right + 1]:
                    left -= 1
                    right += 1
                else:
                    break

            if right - left + 1 > max_palindromic_substring_len:
                best_left_idx = left
                best_right_idx = right
                max_palindromic_substring_len = right - left + 1

    max_palindromic_substring = s[best_left_idx: best_right_idx + 1]
    return max_palindromic_substring

print(longestPalindrome("cbbd"))
