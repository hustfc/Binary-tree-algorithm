class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root
        root.left, root.right = self.Mirror(root.right), self.Mirror(root.left)
        return root
