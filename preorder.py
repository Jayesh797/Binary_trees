def preorderTraversal(self, root):
        res=[]
        def preorder(root):
            if(root==None):
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return res