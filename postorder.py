def postorderTraversal(self, root):
        res=[]
        def postorder(root):
            if(root==None):
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        postorder(root)
        return res