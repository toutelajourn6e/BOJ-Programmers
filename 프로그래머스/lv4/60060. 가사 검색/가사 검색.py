class Trie:
    head = {}
    r_head = {}
    
    def insert(self, word):
        n = len(word)
        cur = self.head
        for char in word:
            if char not in cur:
                cur[char] = {}
            if 'length' not in cur:
                cur['length'] = []
            cur['length'].append(n)
            cur = cur[char]
        if 'length' not in cur:
            cur['length'] = []
        cur['length'].append(n)
        
            
        
        cur = self.r_head
        for char in word[::-1]:
            if char not in cur:
                cur[char] = {}
            if 'length' not in cur:
                cur['length'] = []
            cur['length'].append(n)
            cur = cur[char]
        if 'length' not in cur:
            cur['length'] = []
        cur['length'].append(n)

    def search(self, query):
        n = len(query)
        cur = self.r_head
        if query == '?' * n:
            return cur['length'].count(n)
        elif query[0] == '?':
            for char in query[::-1]:
                if char == '?':
                    return cur['length'].count(n)
                if char not in cur:
                    return 0
                cur = cur[char]
        else:
            cur = self.head
            for char in query:
                if char == '?':
                    return cur['length'].count(n)
                if char not in cur:
                    return 0
                cur = cur[char]
                       

def solution(words, queries):
    trie = Trie()
    result = []
    for word in words:
        trie.insert(word)
    
    for query in queries:
        result.append(trie.search(query))
    
    return result
        