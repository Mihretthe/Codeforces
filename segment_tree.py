


class SegmentTree:

    def calc(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        return (left, right)

    def __init__(self, array):
        self.length = len(array)
        self.array = array

        self.tree = [0] * (2*self.length)
        self.build(0, 0, self.length - 1)

    def build(self,node, left, right):
        if left == right:
            self.tree[node] = self.array[left]
            return
        mid = (left + right) // 2

        left_index, right_index = self.calc(node)
        self.build(left_index, left, mid)
        self.build(right_index, mid + 1, right)

        self.tree[node] = self.tree[left_index] + self.tree[right_index]



    def update(self, index, value):

        self.array[index] = value
        index += self.length - 1
        self.tree[index] = value

        
        parent = (index - 1) // 2
        while parent >= 0:
            left, right = self.calc(parent)
            self.tree[parent] = self.tree[left] + self.tree[right]
            parent -= 1
            parent //= 2   





    def query(self, left, right):
        print(right, len(self.tree))

        total = 0
        left = self.length + left 
        right = self.length + right - 1

        while left < right:
            if left % 2:
                total += self.tree[left]
                left += 1

            if right % 2:
                total += self.tree[right]
                right -= 1

            left //= 2
            right //= 2

        return total

tree = SegmentTree([1,2,3,4,5,6,7,8])

print(tree.query(0, len(tree.array) - 1))
tree.update(3, 5)
print((tree.array))
print(tree.tree)

tree.update(3, 10)
print((tree.array))
print(tree.tree)

tree.update(7, 10)
print((tree.array))
print(tree.tree)



