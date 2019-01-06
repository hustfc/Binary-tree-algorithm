class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def construct(self, pre, tin, startPre, endPre, startTin, endTin):
        if startPre <= endPre:
            root = TreeNode(pre[startPre])
            i = startTin
            while tin[i] != pre[startPre]:  # 在中序遍历中，找到根节点，然后一分为二
                i += 1
            leftLength = i - startTin  # 左子树的长度
            if leftLength:
                root.left = self.construct(pre, tin, startPre + 1, startPre + leftLength, startTin, i - 1)
            if endTin - i:
                root.right = self.construct(pre, tin, startPre + leftLength + 1, endPre, i + 1, endTin)
        return root
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        return self.construct(pre, tin, 0, len(pre) - 1, 0, len(tin) - 1)
