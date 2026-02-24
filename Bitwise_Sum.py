from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict

# solution
# counting how many numbers have the last two bits the same

def solve():
    n = I()
    a = IL()

    count = 0
    

    for num in a:
        if num % 2 == 0:
            count += 1
    
    print(count * (count - 1) // 2)

 
 
 
 
T = I()
for _ in range(T):
    solve()