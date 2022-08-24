# Implement stck with python list and oops


class Stack:
    def __init__(self, maxsize) -> None:
        self.max = maxsize
        self.stack = []

    def push(self, item):
        if self.max > len(self.stack):
            self.stack.append(item)
            return
        else:
            return print(f"Stack is full . Not append {item}")

    def pop(self):
        item = self.stack.pop()
        print(item)

    def peak(self):
        if len(self.stack) == 0:
            return print("Stack is empty")
        else:
            return print(self.stack[-1])

    def length(self):
        return print(len(self.stack))

    def is_empty(self):
        if len(self.stack) == 0:
            return print("Stack is empty")
        else:
            space = self.max - len(self.stack)
            return print(f'stack max sixe is {self.max}  and empty space is {space}') 





if __name__ == "__main__":
    s1 = Stack(6)
    s1.push(10)
    s1.push(10)
    s1.push(10)
    s1.push(10)
    s1.push(10)
    s1.push(10)
    s1.push(77)
    s1.length()
    s1.is_empty()
    
   