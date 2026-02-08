class Stack:
    def __init__(self) -> None:
        self.stack: list[int] = []

    def push(self, new_value: int) -> None:
        self.stack.append(new_value)
        print("ok")

    def pop(self) -> None:
        if self.stack:
            print(self.stack.pop())
        else:
            print("error")

    def back(self) -> None:
        if self.stack:
            print(self.stack[-1])
        else:
            print("error")

    def size(self) -> None:
        print(len(self.stack))

    def clear(self) -> None:
        self.stack = []
        print("ok")


stack: Stack = Stack()
while True:
    input_command: list[str] = input().split()
    value: int | None = None
    if len(input_command) == 2:
        value: int | None = int(input_command[1])
    command: str = input_command[0]
    if command == "push":
        stack.push(value)
    elif command == "pop":
        stack.pop()
    elif command == "back":
        stack.back()
    elif command == "size":
        stack.size()
    elif command == "clear":
        stack.clear()
    elif command == "exit":
        print("bye")
        break
    else:
        raise ValueError