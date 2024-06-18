def isBalanced(self, root):
        def check(root):
            if(root==None):
                return 0
            lh=check(root.left)
            rh=check(root.right)
            if(lh==-1 or rh==-1):
                return -1
            if(abs(lh-rh)>1):
                return -1
            return max(lh,rh)+1
        return check(root)!=-1