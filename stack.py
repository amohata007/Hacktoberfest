class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack."""
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        """Return the top item from the stack without removing it."""
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

# Example usage:
stack = Stack()
stack.push(5)
stack.push(10)
print(f"Top item: {stack.peek()}")
print(f"Stack size: {stack.size()}")
print(f"Popped item: {stack.pop()}")
print(f"Stack size after pop: {stack.size()}")
