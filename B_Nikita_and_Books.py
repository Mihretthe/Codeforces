from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()
    a = IL()


    carry = 0

    for i in range(n):
        index = i + 1
        if a[i] < index:
            need = index - a[i] 
            if carry < need:
                print("NO")
                return 
            carry -= need
        else:
            remain = a[i] - index
            carry += remain

    print("YES")
        

 
 
T = I()
for _ in range(T):
    solve()