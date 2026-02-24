from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

class DSU:

    def __init__(self, n):
        self.parent = {i:i for i in range(n)}
        self.size = {i:1 for i in range(n)}

    
    def find(self, x):

        while self.parent[x] != x:
            x = self.parent[self.parent[x]]

        return x

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX != parentY:
            if self.size[parentX] >= self.size[parentY]:
                self.parent[parentY] = parentX
                self.size[parentX] += self.size[parentY]
            else:
                self.parent[parentX] = parentY
                self.size[parentY] += self.size[parentX]
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

from collections import defaultdict

def solve():
    n, k = II()
    s = S()
    t = S()

    dsu = DSU(n)

    for i in range(n):
        if i + k < n:
            dsu.union(i, i + k)
        if i + k + 1 < n:
            dsu.union(i, i + k + 1)

    hashmap = defaultdict(set)

    for i in range(n):
        hashmap[s[i]].add(i)
    
    for i in range(n):
        me = s[i]
        them = t[i]

        for index in hashmap[them]:
            if dsu.isConnected(i, index):
                hashmap[them].remove(index)
                break
        
        else:
            print("NO")
            return 

        
    
    print("YES")


 
 
 
 
T = I()
for _ in range(T):
    solve()