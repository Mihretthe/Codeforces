from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n, x, y = II()
    a = IL()
    
    parent = {i:i for i in range(n + 1)}
    size = {i:1 for i in range(n + 1)}

    visited = set()

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]

        return x

    def union(x, y):
        parentX = find(x)
        parentY = find(y)

        if parentX != parentY:
            if size[parentX] >= size[parentY]:
                parent[parentY] = parentX
                size[parentX] += size[parentY]
            else:
                parent[parentX] = parentY
                size[parentY] += size[parentX]

    
    for i in range(n):

        if i not in visited:
            forx = i 

            while forx < n:
                visited.add(forx)
                union(i, forx)
                forx += x

            fory = i 
            while fory < n:
                visited.add(fory)
                union(i, fory)
                fory += y

    for i in range(n):
        num = a[i] - 1
        belong = i

        parentNum = find(num)
        parentReal = find(belong)

        if parentNum != parentReal:
            print("NO")
            return

    print("YES")


T = I()
for _ in range(T):
    solve()