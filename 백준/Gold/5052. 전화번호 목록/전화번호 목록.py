import sys
input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.head = {}
    
    def add(self, word):
        cur = self.head
        
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True
        
    def search(self, word):
        cur = self.head
        
        for ch in word:
            if '*' in cur and len(cur) > 1:
                return False
            cur = cur[ch]
            
        return True
    
    def __del__(self):
        return
        
t = int(input())

for _ in range(t):
    dic = Trie()
    n = int(input())
    nums = [input().rstrip() for _ in range(n)]
    
    for i in nums:
        dic.add(i)
        
    for i in nums:
        if not dic.search(i):
            print('NO')
            break
    else:
        print('YES')
        
    del dic