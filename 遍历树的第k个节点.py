class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.k = 0
    def InOrder(self, Root):
        ans = None
        if Root:
            if ans == None and Root.left:
                ans = self.InOrder(Root.left)   #往左遍历
            if ans == None and self.k == 1:
                ans = Root                      #遍历到目标节点
            if ans == None and self.k != 1:     #没有遍历到目标节点，k--
                self.k -= 1
            if ans == None and Root.right:      #往右遍历
                ans = self.InOrder(Root.right)
        return ans
    def KthNode(self, Root, k):
        if Root == None or k <= 0:
            return None
        self.k = k
        return self.InOrder(Root)