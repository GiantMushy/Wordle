class Node:
    def __init__(self, username = None, score = None, prev = None, next = None):
        self.username = username
        self.score = score
        self.prev = prev
        self.next = next

class ScoreDLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr = self.tail
        self.size = 0

    def insert(self, username, score): #O(1)
        new_node = Node(username, score, self.curr.prev, self.curr)
        self.curr.prev.next = new_node
        self.curr.prev = new_node
        self.curr = new_node
        self.size += 1

    def remove(self): #O(1)
        if self.curr.next != None and self.curr.prev != None:
            self.curr.prev.next = self.curr.next
            self.curr.next.prev = self.curr.prev
            self.curr = self.curr.next
            self.size -= 1

    def get_curr_data(self): #O(1)
        return {"username" : self.curr.username, "score" : self.curr.score}

    def move_to_next(self): #O(1)
        if self.curr.next != self.tail:
            self.curr = self.curr.next

    def move_to_prev(self): #O(1)
        if self.curr.prev != self.head:
            self.curr = self.curr.prev

    def contains(self, username):
        return self._contains_recur(username, self.head.next)
    
    def _contains_recur(self, username, node):
        if node.next is None:
            return False
        if node.username == username:
            return True
        else:
            return self._contains_recur(username, node.next)
        
    def __setitem__(self, username, score):
        if self.contains(username):
            self._set_item_recur(username, score, self.head.next)
        else:
            self.insert(username, score)

    def _set_item_recur(self, username, score, node):
        if username == node.username:
            if node.score < score:
                node.score = score
        else:
            self._set_item_recur(username, score, node.next)

    def __getitem__(self, username):
        return self._get_item_recur(username, self.head.next)
    
    def _get_item_recur(self, username, node):
        if node.next is None:
            raise KeyError
        if node.username == username:
            return node.score
        else:
            return self._get_item_recur(username, node.next)

    def clear(self): #O(1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr = self.tail
        self.size = 0

    def get_first_node(self): #O(1)
        return self.head.next

    def get_last_node(self): #O(1)
        return self.tail.prev

    def move_node_behind(self, curr, low): #O(1)
        '''creates a new cloned node behind low and removes the the one in front'''
        node = Node(curr.score, low.prev, low)
        node.prev.next = node
        node.next.prev = node
        curr.prev.next = curr.next
        curr.next.prev = curr.prev


    def partition(self, low, high): #O(n)
        curr = low.next
        while curr != high.next:
            if curr.score < low.score:
                self.move_node_behind(curr, low)
            curr = curr.next
        self.curr = low
        
    def sort(self):
        if self.head.next != self.tail:
            self.quicksort(self.get_first_node(), self.get_last_node())
            self.curr = self.head.next

    def quicksort(self, low, high):
        if low == high or high.score == None or low.score == None:
            return
        #print(str(self))
        low_storage = low.prev
        self.partition(low, high)
        self.quicksort(low_storage.next, self.curr)
        self.quicksort(self.curr.next, high)

    def __len__(self):
        return self.size

    def __str__(self):
        ret_str = ""
        node = self.head.next
        while node.next != None:
            ret_str += str(node.username) + ", "
            ret_str += str(node.score) + "\n"
            node = node.next
        return ret_str

if __name__ == "__main__":
    pass
    