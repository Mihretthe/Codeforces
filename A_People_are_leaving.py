from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n, q = II()

    parent = {i:i for i in range(1, n + 1)}
    parent[-1] = -1
    size = {i:1 for i in range(1, n + 1)}

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        parentX = find(x)
        parentY = find(y)

        parent[parentX] = parentY


    for _ in range(q):
        command, num = SL()
        num = int(num)

        if command == "?":
            print(find(num))
        else:
            if num == n:
                parent[num] = -1
            else:
                union(num, num + 1)
 
 
 
 
T = 1
for _ in range(T):
    solve()



class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = {i:i for i in range(n)}
        self.size = {i:1 for i in range(n)}
    
    def find(self, x):

        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        
        return x

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            if self.size[parent_x] >= self.size[parent_y]:
                self.parent[parent_y] = parent_x
                self.size[parent_x] += self.size[parent_y]
            else:
                self.parent[parent_x] = parent_y
                self.size[parent_y] += self.size[parent_x]


from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    pass
 
 
 
 
T = 1
for _ in range(T):
    solve()