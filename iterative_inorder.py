def iteravtive_inorder(root):
    stack=[]
    cur=root
    res=[]
    while(stack!=[] and cur!=None):
        while(cur):
            stack.append(cur)
            cur=cur.left
        cur=stack.pop()
        res.append(cur)
        cur=cur.right
    return res
