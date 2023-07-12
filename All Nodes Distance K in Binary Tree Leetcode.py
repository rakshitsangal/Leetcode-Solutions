# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        q=[root]
        d=defaultdict(list)#store neighbours
        while(q):
            
            for i in range(len(q)):
                x=q.pop(0)
                if x.left:
                    d[x].append(x.left)
                    d[x.left].append(x)
                    q.append(x.left)
                if x.right:
                    d[x.right].append(x)
                    d[x].append(x.right)
                    q.append(x.right)


        #find the nodes at distance k
        q=[target]
        vis=set()
        vis.add(target)
        while(q and k>0):
            
            for i in range(len(q)):
                x=q.pop(0)
                for node in d[x]:
                    if node not in vis:
                        vis.add(node)
                        q.append(node)
            k-=2
        ans=[]
        
        for node in q:
            ans.append(node.val)
        return ans
