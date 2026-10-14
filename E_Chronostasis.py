from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def createBst(lst):
    if not lst:
        return 

    mid = len(lst) // 2
    root = TreeNode(lst[mid])
    root.left = createBst(lst[:mid])
    root.right = createBst(lst[mid + 1:])

    return root

def deleteNode(root: TreeNode, value):

    if not root:
        return 

    if root.val > value:
        root.left =  deleteNode(root.left, value)
    elif root.val < value:
        root.right = deleteNode(root.right, value)
    else:

        if not root.left:
            return root.right
        
        if not root.right:
            return root.left

        temp = leftMost(root.right)
        root.val = temp.val

        root.right = deleteNode(root.right, temp.val)
    return root
        

def leftMost(root: TreeNode):

    current = root
    while current.left:
        current = current.left

    return current

def search(root: TreeNode, target):

    answer = root

    while root:
        if root.val + target > 0:
            answer = root
            root = root.left
        else:
            root = root.right

    return answer


def solve():
    n = I()
    a = IL()

    positives = [i for i in a if i > 0]
    negatives = [i for i in a if i <= 0]

    negatives.sort()
    positives.sort(reverse=True)

    root = createBst(negatives)

    if positives:
        answer = [positives.pop()]
        while len(answer) < n:
            find = search(root, answer[-1])

            if find and find.val + answer[-1] > 0:
                answer.append(find.val + answer[-1])
                root = deleteNode(root, find.val)
            else:
                if positives:
                    answer.append(answer[-1] + positives.pop())
                else:
                    print(-1)
                    return

    else:
        print(-1)
        return



    
    print(*answer)
 
 
 
 
T = I()
for _ in range(T):
    solve()