class Node(object):
    def __init__(self, key, terminated = False):
        self.key = key
        self.terminated = terminated
        self.children = {}

class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur = self.head

        for c in string:
            if c not in cur.children:
                cur.children[c] = Node(c)
            cur = cur.children[c]
        cur.terminated = True

    def search(self, string):
        cur = self.head
        idx = 0

        while cur:
            if idx >= len(string):
                return False
            if cur.terminated:
                return True
            cur = cur.children[string[idx]]
            idx += 1
                    

def solution(phone_book):
    root = Trie()
    for num in phone_book:
        root.insert(num)
    for num in phone_book:
        if root.search(num):
            return False
    return True
