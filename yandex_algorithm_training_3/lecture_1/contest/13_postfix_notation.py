from collections import deque


def calculate_expression(postfix_expression: str) -> int:
    postfix_expression = postfix_expression.split()
    operations_set: set[str] = {"+", "-", "*", "/"}
    stack: deque[str | int] = deque([])
    for symbol in postfix_expression:
        if symbol in operations_set:
            second_value: int = stack.pop()
            first_value: int = stack.pop()
            if symbol == "+":
                result: int = first_value + second_value
            elif symbol == "-":
                result: int = first_value - second_value
            elif symbol == "*":
                result: int = first_value * second_value
            else:
                result: int | None = None
            stack.append(result)

        else:
            stack.append(int(symbol))

    return stack.pop()


postfix_expression_example: str = input()
print(calculate_expression(postfix_expression_example))
