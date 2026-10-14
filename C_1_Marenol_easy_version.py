
from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()
    a = list(S())
    b = list(S())

    evensa = [0,0]
    oddsa = [0,0]

    evensb = [0,0]
    oddsb = [0,0]

    for i in range(n):
        if i % 2:
            indexa = int(a[i])
            indexb = int(b[i])

            oddsa[indexa] += 1
            oddsb[indexb] += 1

        else:
            indexa = int(a[i])
            indexb = int(b[i])

            evensa[indexa] += 1
            evensb[indexb] += 1

    if oddsa != oddsb or evensa != evensb:
        print("NO")
    else:
        print("YES")   

            
                
T = I()
for _ in range(T):
    # print(_)
    solve()