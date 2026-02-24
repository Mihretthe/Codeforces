from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from heapq import heappop, heappush

def solve():
    n = I()
    a = IL()  


    # max heap
    heap = []

    # add to numbers to the heap
    # when a[i] is 0, add the maximum from the heap

    power = 0

    for i in range(n):
        if a[i] == 0:
            if heap:
                power += -heappop(heap)
        else:
            heappush(heap, -a[i])
    
    print(power)


 
 
 
 
T = I()
for _ in range(T):
    solve()