from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    s = S()

    index_one = s.index("1")
    index_zero = s.index("0")

    new_s = []

    for i in range(len(s)):
        if i == index_one or i == index_zero:
            continue
        new_s.append(s[i])

    print("".join(new_s))

    
 
 
 
T = I()
for _ in range(T):
    solve()