class Trie:
    head = {}
    
    def insert(self, word):
        cur = self.head
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['*'] = True
    
    def search(self, word):
        cur = self.head
        for char in word:
            if '*' in cur:
                return True
            cur = cur[char]
            


def solution(phone_book):
    trie = Trie()
    
    for i in phone_book:
        trie.insert(i)
        
    for i in phone_book:
        if trie.search(i):
            return False
        
    return True