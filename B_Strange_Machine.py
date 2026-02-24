from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n, q = II()
    s = S()
    a = IL()

    
    for query in a:

        index = 0
        while query > 0:
            i = index % n
            if s[i] == 'B':
                query //= 2
            else:
                query -= 1
            index += 1
        
        print(index)
            





 
T = I()
for _ in range(T):
    solve()