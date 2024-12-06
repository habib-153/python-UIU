class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_after(self, prev, data):
        if prev is None:
            return f"The given previous node must inLinkedList."
        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node
    def insert_end(self, data):
        new_node = Node(data)
        last = self.head
        while last.next != None:
            last = last.next
        new_node.next = None
        last.next = new_node
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
    def delete_node(self, key):
        if self.head is None:
            return
        if self.head.data == key:
            self.head = self.head.next
        prev = self.head
        while prev.next.data != key:
            prev = prev.next
        prev.next = prev.next.next
    def sort_list(self):
        current = self.head
        index = Node(None)
        if self.head is None:
            return
        else:
            while current.next != None:
                index = current.next
                while index != None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data
                    index = index.next
                current = current.next
    def search(self, key):
        current = self.head
        while current != None:
            if key == current.data:
                return True
            current = current.next
        return False
        

linked1 = LinkedList()
element1 = Node(40)
element2 = Node(50)
element3 = Node(30)
element4 = Node(20)
linked1.head = element1
element1.next = element2
element2.next = element3
element3.next = element4

# linked1.delete_node(30)
linked1.insert_after(element2, 28)
linked1.sort_list()
print("Found") if linked1.search(None) else print("Not Found")
linked1.traverse()