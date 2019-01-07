class Solution:
    def RecursionSymmetry(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        elif root1 == None or root2 == None:
            return False
        if root1.val == root2.val:
            return self.RecursionSymmetry(root1.left, root2.right)
        else:
            return False
    def isSymmetrical(self, pRoot):
        # write code here
        return self.RecursionSymmetry(pRoot, pRoot)
