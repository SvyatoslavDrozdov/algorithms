from collections import deque


def is_correct(brackets_sequence: str) -> bool:
    stack: deque[str] = deque([])
    open_brackets: set[str] = {"(", "[", "{"}
    for bracket in brackets_sequence:
        if bracket in open_brackets:
            stack.append(bracket)
        else:
            if stack:
                last_bracket: str = stack.pop()
                new_bracket_is_correct: bool = last_bracket == "(" and bracket == ")"
                new_bracket_is_correct += last_bracket == "[" and bracket == "]"
                new_bracket_is_correct += last_bracket == "{" and bracket == "}"
                if not new_bracket_is_correct:
                    return False
            else:
                return False

    if stack:
        return False
    return True


brackets_sequence_example: str = input()
if is_correct(brackets_sequence_example):
    print("yes")
else:
    print("no")
