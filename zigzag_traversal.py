def zigzagLevelOrder(self, root):
        result=[]
        queue=[root]
        next_queue=[]
        level=[]
        i=0
        if(root==None):
            return result
        while queue!=[]:
            for root in queue:
                level.append(root.val)
                if root.left:
                    next_queue.append(root.left)
                if root.right:
                    next_queue.append(root.right)
            if(i%2==0):
                result.append(level)
            else:
                result.append(level[::-1])
            i+=1
            level=[]
            queue=next_queue
            next_queue=[]
        return result