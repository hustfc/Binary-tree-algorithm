class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.results = []
    def ListSum(self, l):
        sum = 0
        for i in l:
            sum += i
        return sum
    def RecursionFindPath(self, root, expectNumber, result):
        result.append(root.val)
        temp = result[:]
        if root.left == None and root.right == None and self.ListSum(result) == expectNumber:
            self.results.append(result)
        if root.left:
            self.RecursionFindPath(root.left, expectNumber, result)
        result = temp[:]
        if root.right:
            self.RecursionFindPath(root.right, expectNumber, result)
    def QuickSort(self, results, start, end):
        if start >= end:
            return
        low, high = start, end
        pivot = results[start]
        while low < high:
            while low < high and len(results[high]) <= len(pivot):
                high -= 1
            if low < high:
                results[low] = results[high]
            while low < high and len(results[low]) >= len(pivot):
                low += 1
            if low < high:
                results[high] = results[low]
        results[low] = pivot
        self.QuickSort(results, start, low - 1)
        self.QuickSort(results, low + 1, end)
    def FindPath(self, root, expectNumber):
        # write code here
        if root == None:
            return []
        self.RecursionFindPath(root, expectNumber, [])
        if self.results == []:
            return []
        self.QuickSort(self.results, 0, len(self.results) - 1)
        return self.results
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.right = TreeNode(2)
root.right.right.left = TreeNode(1)
root.right.right.right = TreeNode(5)
expectNum = 7
print(Solution().FindPath(root, expectNum))