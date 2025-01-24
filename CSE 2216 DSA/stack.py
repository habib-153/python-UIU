class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def insert_at_bottom(self, item):
        if self.is_empty():
            self.push(item)
        else:
            temp = self.pop()
            self.insert_at_bottom(item)
            self.push(temp)
    def reverse(self):
        if not self.is_empty():
            temp = self.pop()
            self.reverse()
            self.insert_at_bottom(temp)
    def print_stack(self):
        for i in self.items:
            print(i, end=" ")
        print()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack2:
    def __init__(self):
        self.top     = None
    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top 
            self.top = new_node
    def pop(self):
        if self.top is None:
            return f"Stack Underflow"
        else:
            item = self.top.data
            self.top = self.top.next
            return item
    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None


def palindrome(string):
    stack = Stack()
    filtered = "".join(filter(lambda y: y.isalpha() and y != "x", string)).lower()
    print(filtered)
    for char in filtered:
        stack.push(char)
    for char in filtered:
        if char != stack.pop():
            return "Not a Palindrome"
    return "Palindrome"
# input_string = "radxar"
# print(palindrome(input_string))

def isValid(string):
    stack = Stack()
    brackets = {')': '(', '}': '{', ']': '['}

    for char in string:
        if char in brackets.values():
            stack.push(char)
        elif char in brackets.keys():
            if stack.is_empty() or brackets[char] != stack.pop():
                return False
        else:
            return False
    return stack.is_empty()
# input_string = "{[()]})"
# print(isValid(input_string)) 

def evaluatePrefix(exp):
    stack = Stack()
    for i in exp:
        if i.isdigit():
            stack.push(i)
        else:
            a = stack.pop()
            b = stack.pop() 
            stack.push(str(eval(b + i + a)))
    return stack.pop()
exp = "231*+9-"
# print(evaluatePrefix(exp))
     
stack_for_reverse = Stack()
stack_for_reverse.push(1)
stack_for_reverse.push(2)
stack_for_reverse.push(3)
stack_for_reverse.push(4)
# stack_for_reverse.print_stack()
# stack_for_reverse.reverse()
# stack_for_reverse.print_stack()

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        return None

# Demonstration
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
print(queue.dequeue())  # Output: 3
print(queue.dequeue())  # Output: None