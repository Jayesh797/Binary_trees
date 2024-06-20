def boundary_nodes(self,root):
    if(root==None):
        return root
    result=[]
    result.append(root.val)
    #traverse leftmost without leaf
    def leftmost(node):
        if node.left==None and node.right==None:
            return 
        result.append(node.val)
        

    #trevers leafnodes
    def leaf(node):
        if not node:
            return
        leaf(node.left)

        if node!=root and node.left==None and node.right==None:
            result.append(node.val)
        
        leaf(node.right)
    

    #travers rightmost without leaf
    def rightmost(node):
        if node.left==None and node.right==None:
            return

        if(node.right):
            rightmost(node.right)
        else:
            leftmost(node.left)

        result.append(node.val)

    if(root.left):
        leftmost(root.left)
    
    leaf(root)

    if(root.right):
            rightmost(root.right)

    return result