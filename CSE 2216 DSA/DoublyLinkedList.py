class Node:
    def __init__(self, data):
        self.prev = None
        self.data =  data
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def insert_after(self, prev, data):
        new_node = Node(data)
        prev_element =  self.head
        while prev_element.data != prev:
            prev_element = prev_element.next
        new_node.next =  prev_element.next
        prev_element.next.prev = new_node
        prev_element.next = new_node
        new_node.prev = prev_element
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
    def insert_end(self, data):
        new_node = Node(data)
        last = self.head
        while last.next is not None:
            last = last.next
        new_node.prev = last
        last.next = new_node
    def delete_node(self, key):
        current = self.head
        if self.head.data == key:
            self.head = self.head.next
            self.head.prev = None
            return
        while current.data != key:
            current = current.next
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
    def sort_list(self):
        current = self.head
        index = None
        while current.next is not None:
            index = current.next
            while index is not None:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next
    def search(self, key):
        if self.head is None:
            return f"there in no item in the list"
        if self.head.data == key:
            return f"item founded in 1st element"
        current = self.head
        while current.next is not None:
            if current.data == key:
                return f"item funded in the list"
            current = current.next
        return f"not found"

linked1 = DoublyLinkedList()
element1 = Node(40)
element2 = Node(50)
element3 = Node(30)
element4 = Node(20)
linked1.head = element1
element1.next = element2
element2.prev = element1
element2.next = element3
element3.prev = element2
element3.next = element4
element4.prev = element3

linked1.insert_beginning(10)
linked1.insert_after(30, 35)
linked1.insert_end(37)
linked1.delete_node(20)
linked1.sort_list()
print(linked1.search(10))
linked1.traverse()   