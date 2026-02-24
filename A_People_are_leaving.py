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

