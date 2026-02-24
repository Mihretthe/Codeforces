from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n, q = II()
    # accept queries and act upon it

    parent = {i:i for i in range(1, n + 1)}
  
    
    value = {i:0 for i in range(1, n + 1)}

    def find(x):
        
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        parentX = find(x)
        parentY = find(y)

        if parentX != parentY:
            if value[parentX] > value[parentY]:
                
                parent[parentY] = parentX
                
            else:
                parent[parentX] = parentY
                



    for _ in range(q):
        command = SL()

        if command[0] == "add":
            parentX = find(int(command[1]))
            value[parentX] += int(command[2])
        elif command[0] == "join":
            
            union(int(command[1]), int(command[2]))
            
        else:
            x = int(command[1])
            parentX = find(x)
            print(value[parentX] + value[x])

 
 
 
 
T = 1
for _ in range(T):
    solve()