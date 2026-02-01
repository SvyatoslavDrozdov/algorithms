from collections import deque

CLOSING_BRACKETS: set[str] = {")", "]", "}"}
CORRESPONDING_BRACKETS: dict[str, str] = {")": "(", "]": "[", "}": "{"}


def is_sequence_correct(bracket_sequence: str) -> bool:
    stack: deque[str] = deque()

    for current_bracket in bracket_sequence:
        if current_bracket in CLOSING_BRACKETS:
            if not stack:
                return False
            last_bracket_in_queue: str = stack.pop()
            if last_bracket_in_queue != CORRESPONDING_BRACKETS[current_bracket]:
                return False
        else:
            stack.append(current_bracket)

    return not stack


bracket_sequence_example: str = input()
bracket_sequence_is_correct: bool = is_sequence_correct(bracket_sequence_example)
if bracket_sequence_is_correct:
    print(f"Bracket sequence is correct.")
else:
    print(f"Bracket sequence isn't correct.")
