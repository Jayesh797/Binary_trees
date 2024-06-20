def isSymmetric(self, root):
        def dfs(left,right):
            if(left==None and right==None):
                return True
            if(left==None or right==None):
                return False
            return (left.val==right.val and dfs(left.left,right.right) and dfs(left.right,right.left))
        return dfs(root.left,root.right)