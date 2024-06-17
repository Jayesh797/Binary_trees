def iterative_preorder(root):
    result=[]
    stack=[root]
    while(stack!=[]):
        root=stack[-1]
        stack.pop()
        result.append(root.val)
        if(root.right):
            stack.append(root.right)
        if(stack.left):
            stack.append(root.left)
    return result
