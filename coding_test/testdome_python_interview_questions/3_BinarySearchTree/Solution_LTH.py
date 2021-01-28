import collections
from queue import deque

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    if not root:
        return False
    elif root[2] == value:
        return True
    else:
        return contains(root[0] if value <= root[2] else root[1], value)
    
        
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
print(contains(n2, 3))