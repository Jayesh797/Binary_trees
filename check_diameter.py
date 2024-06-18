def diameterOfBinaryTree(self, root):
        def check(root,diameter):
            if(root==None):
                return 0
            lh=check(root.left,diameter)
            rh=check(root.right,diameter)
            diameter[0]=max(diameter[0],lh+rh)
            return 1+max(lh,rh)
        diameter=[0]
        check(root,diameter)
        return diameter[0]
        