class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = pre

        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        temp = self.head
        if self.length <= 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.head = self.head.next
            temp.next = None
            self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value =value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif self.length == index:
            return self.append(value)

        temp = Node(value)
        temp.next = self.get(index)

        for i in range(self.length):
            if i.next == self.get(index):
                i.next = temp

        


        
    


mls = LinkedList(4)
mls.append(3)
mls.append(5)
mls.prepend(1)
mls.print_list()
