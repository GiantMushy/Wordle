class Node:
    def __init__(self, username = None, score = None, left = None, right = None):
        self.username = username
        self.score = score
        self.left = left
        self.right = right

class ScoreBST:
    def __init__(self) -> None:
        self.root = None


    def insert(self, username, score):
        self.root = self._insert_recur(username, int(score), self.root)

    def _insert_recur(self, username, score, root):
        if root == None:
            return Node(username, score)
        if score < int(root.score):
            root.left = self._insert_recur(username, score, root.left)
        elif score >= int(root.score):
            root.right = self._insert_recur(username, score, root.right)
        return root


    def get_node(self, username, score):
        return self._get_node_recur(username, score, self.root)
    def _get_node_recur(self, username, score, node): #O(log n)
        if node is None:
            return None
        if username == node.username:
            return node
        if int(node.score) > score:
            return self._get_node_recur(username, score, node.left)
        elif int(node.score) <= score:
            return self._get_node_recur(username, score, node.right)


    def contains_node(self, username, score):
        return self.get_node(username, score) is not None

    def contains_username(self, username):
        return self.get_score_by_username(username) is not None

    def get_score_by_username(self, username):
        return self._score_by_username_recur(username, self.root)
    def _score_by_username_recur(self, username, node):
        if node is None:
            return None
        if username == node.username:
            return node.score
        ret = self._score_by_username_recur(username, node.left)
        if ret is None:
            ret = self._score_by_username_recur(username, node.right)
        return ret


    def __len__(self):
        return self._len_recur(self.root)
    def _len_recur(self, root):
        if root is None:
            return 0
        return 1 + self._len_recur(root.left) + self._len_recur(root.right)

    def __setitem__(self, username, score):
        old_score = self.get_score_by_username(username)
        if old_score is None:
            self.insert(username, score)
        elif int(old_score) < score:
            self.remove(username, old_score)
            self.insert(username, score)

    def __getitem__(self, username):
        return self.get_score_by_username(username)
        
    def update(self, username, score):
        '''updates the users score if it is greater than his current score'''
        self[username] = score
    
    def remove(self, username, score):
        self.root = self._remove_recur(username, score, self.root)

    def _remove_recur(self, username, score, root):
        if root is None:
            return None
        if root.username == username:
            root = self._remove_node(root)
        elif score >= int(root.score):
            root.right = self._remove_recur(username, score, root.right)
        elif score < int(root.score):
            root.left = self._remove_recur(username, score, root.left)
        return root

    def _remove_node(self, node):
        if node.left is None and node.right is None:
            return None
        elif node.right is None:
            return node.left
        elif node.left is None:
            return node.right
        else: #2 children -> go to right
            node.right = self._goleft_recur(node.right, node)
            return node

    def _goleft_recur(self, node, org_root):
        if node.left is None:
            org_root.value = node.value
            return self._remove_node(node)
        node.left = self._goleft_recur(node.left, org_root)
        return node
    
    def clear(self):
        self.root = None

    def get_highscore(self):
        return self._get_highscore_recur(self.root)
    
    def _get_highscore_recur(self, node):
        if node.right is None:
            return node
        else:
            return self._get_highscore_recur(node.right)
        
    def _str_inorder(self, root):
        ret_string = ""
        if root is None:
            return ret_string
        ret_string += self._str_inorder(root.right)
        ret_string += str(root.username) + ", " + str(root.score) + "\n"
        ret_string += self._str_inorder(root.left)
        return ret_string
    
    def __str__(self):
        return self._str_inorder(self.root).strip()

if __name__ == "__main__":
    score = ScoreBST()
    score["TOR"] = 500
    score["ADJ"] = 450
    score["SAE"] = 450
    score["TOR"] = 300
    score["ADJ"] = 600
    print(score)
    print(score["ADJ"])
    