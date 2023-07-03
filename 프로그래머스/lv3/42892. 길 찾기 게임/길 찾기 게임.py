import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, num, x):
        self.num = num
        self.x = x
        self.left = None
        self.right = None
        
def insert(num, x, root):
    if x < root.x:
        if not root.left: root.left = Node(num, x)
        else: insert(num, x, root.left)
    else:
        if not root.right: root.right = Node(num, x)
        else: insert(num, x, root.right)
        
def preorder(root, result):
    if not root: return
    result.append(root.num)
    preorder(root.left, result)
    preorder(root.right, result)
    
def postorder(root, result):
    if not root: return
    postorder(root.left, result)
    postorder(root.right, result)
    result.append(root.num)

def solution(nodeinfo):
    nodeinfo = [(index+1, info) for index, info in enumerate(nodeinfo)]
    nodeinfo.sort(key=lambda x: x[1][1], reverse=True)
    
    root = Node(nodeinfo[0][0], nodeinfo[0][1][0])
    
    for num, info in nodeinfo[1:]:
        insert(num, info[0], root)
        
    pre_result = []
    preorder(root, pre_result)
    
    post_result = []
    postorder(root, post_result)
    
    return [pre_result, post_result]