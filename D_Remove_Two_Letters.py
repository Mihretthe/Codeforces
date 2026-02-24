from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()
    s = S()
    
    # check if i and i + 2 are different 
    answer = 0

    for i in range(n - 2):
        if s[i] != s[i + 2]:            
            answer += 1
    
    print(answer + 1)
 
 
T = I()
for _ in range(T):
    solve()