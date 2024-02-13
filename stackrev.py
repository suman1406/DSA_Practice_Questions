# **Question:**
# Consider a stack implementation with elements `[5, 4, 3, 2, 1]`. Describe and implement an algorithm that reverses this stack using 
# an auxiliary stack and a temporary variable. Provide a step-by-step explanation and the corresponding code for the reversal process.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def reverse_stack(original_stack):
    auxiliary_stack = Stack()
    temp_variable = None

    while not original_stack.is_empty():
        if temp_variable is None:
            temp_variable = original_stack.pop()
        else:
            current_element = original_stack.pop()

            while not auxiliary_stack.is_empty() and auxiliary_stack.items[-1] > current_element:
                original_stack.push(auxiliary_stack.pop())

            auxiliary_stack.push(temp_variable)
            temp_variable = None

            while not auxiliary_stack.is_empty():
                original_stack.push(auxiliary_stack.pop())

            temp_variable = current_element

    if temp_variable is not None:
        auxiliary_stack.push(temp_variable)

    while not auxiliary_stack.is_empty():
        original_stack.push(auxiliary_stack.pop())

def reverse_stack1(original_stack):
    if original_stack.is_empty():
        return

    auxiliary_stack = Stack()
    temp_variable = original_stack.pop()

    while not original_stack.is_empty():
        auxiliary_stack.push(original_stack.pop())

    original_stack.push(temp_variable)

    while not auxiliary_stack.is_empty():
        original_stack.push(auxiliary_stack.pop())

original_stack = Stack()
for i in [5, 4, 3, 2, 1]:
    original_stack.push(i)

print("Original Stack:", original_stack.items)
reverse_stack(original_stack)
print("Reversed Stack:", original_stack.items)

original_stack1 = Stack()
for i in range(1, 6):
    original_stack1.push(i)

print("Original Stack:", original_stack1.items)
reverse_stack1(original_stack1)
print("Reversed Stack:", original_stack1.items)
