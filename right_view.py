def rightSideView(self, root):
        if root==None:
            return []
        result=[]
        queue=[root]
        next_queue=[]
        level=[]
        while(queue!=[]):
            for root in queue:
                level.append(root.val)
                if(root.left):
                    next_queue.append(root.left)
                if(root.right):
                    next_queue.append(root.right)
            result.append(level)
            level=[]
            queue=next_queue
            next_queue=[]
        act_result=[]
        for ele in result:
            act_result.append(ele[-1])
        return act_result
