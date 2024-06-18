def postorder_2stack(root):
    st1=[root]
    st2=[]
    res=[]
    while(st1!=[]):
        root=st1[-1]
        st1.pop()
        st2.append(root)
        if(root.left):
            st1.append(root.left)
        if(root.right):
            st1.append(root.right)
    while(st2!=[]):
        top=st2.pop()
        res.append(top.val)
    return res