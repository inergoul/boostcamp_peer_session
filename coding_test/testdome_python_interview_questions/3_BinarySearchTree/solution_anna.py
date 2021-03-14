import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    dq = collections.deque([root])
    while dq:
        cur = dq.popleft()
        if not cur:
            continue
        if cur.value == value:
            return True
        if cur.value > value:
            dq.append(cur.left)
        else:
            dq.append(cur.right)
    return False
