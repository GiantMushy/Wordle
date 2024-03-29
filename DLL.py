

class Node:
    def __init__(self, word = None, code = None, next = None, prev = None):
        self.word = word
        self.code = code
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self):
        self.front = Node()
        self.back = Node()
        self.front.next = self.back
        self.back.prev = self.front
        self.size = 0
    

    def append(self, word, code): #O(1)
        '''Adds an item to the list after the last item'''
        new_node = Node(word, code, self.back.prev, self.back)
        self.back.prev.next = new_node
        self.back.prev = new_node
        self.size += 1
    
    def empty(self): #O(1)
        self.front.next = self.back
        self.back.prev = self.front
        self.size = 0
