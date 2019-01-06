class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.k = 0
    def ReverseInOrder(self, pRoot):
        ans = None
        if pRoot:
            if ans == None and pRoot.right:
                ans = self.ReverseInOrder(pRoot.right)
            if ans == None and self.k == 1:
                ans = pRoot
            if ans == None and self.k != 1:
                self.k -= 1
            if ans == None and pRoot.left:
                ans = self.ReverseInOrder(pRoot.left)
        return ans
    def KthNode(self, pRoot, k):
        # write code here
        if pRoot == None and k < 1:
            return None
        self.k = k
        return self.ReverseInOrder(pRoot)