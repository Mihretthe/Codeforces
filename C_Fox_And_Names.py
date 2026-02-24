from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict, deque

def solve():
    
    n = I()
    npc = set("abcdefghijklmnopqrstuvwxyz")

    words = []

    for _ in range(n):
        words.append(S())


    graph = defaultdict(list)
    indegree = defaultdict(int)


    i = 0
    j = 1

    while j < n:

        first = words[i]
        second = words[j]

        if first == second:
            j += 1
            continue

        i += 1
        j += 1

        index = 0

        while index < len(first) and index < len(second):

            if first[index] != second[index]:
                graph[first[index]].append(second[index])
                indegree[second[index]] += 1
            
                npc.discard(first[index])
                npc.discard(second[index])

                break
            index += 1

        else:
            if index == len(second) and  (index != len(first)):
                print("Impossible")
                return
            
        
    answer = []
    deck = deque()

    for key in graph:
        if indegree[key] == 0:
            deck.append(key)

    
   
    
    while deck:
        node = deck.popleft()

        answer.append(node)
        npc.discard(node)

        for friend in graph[node]:
            indegree[friend] -= 1

            if indegree[friend] == 0:
                deck.append(friend)
                del indegree[friend]

    
    if (len(set(indegree.values())) == 1 and 0 in set(indegree.values())) or not indegree:
        answer.extend(list(npc))
        print("".join(answer))
        return

    print("Impossible")

            


















    

 
 
 
 
T = 1
for _ in range(T):
    solve()



x = 2
y = x
x = 5
print(x)
print(y)

x = [1,2 ,3]
y = x

x[0] = 5

print(x)
print(y)