# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
     def widthOfBinaryTree(self, root):
        if not root:
            return 0
        mw = 1
        queue = deque([root])
        index_queue = deque([1])
        while queue:
            level_size = len(queue)
            left_index, right_index = 0, 0
            
            for i in range(level_size):
                node = queue.popleft()
                index = index_queue.popleft()
                
                if i == 0:
                    left_index = index
                if i == level_size - 1:
                    right_index = index
                
                if node.left:
                    queue.append(node.left)
                    index_queue.append(index * 2)
                if node.right:
                    queue.append(node.right)
                    index_queue.append(index * 2 + 1)
            
            mw = max(mw, right_index - left_index + 1)
        return mw
    
