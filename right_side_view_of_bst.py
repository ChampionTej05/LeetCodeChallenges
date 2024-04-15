'''
https://leetcode.com/problems/binary-tree-right-side-view/

use level order traversal and take last node at each iteration
'''


def right_side_view(root):
    from collections import deque

    if not root :
        return root 
    
    queue = deque()
    queue.append(root)
    result = []

    while queue:

        queue_length = len(queue)

        for i in range(queue_length):

            popped_node = queue.popleft()

            # is it the last node in the level 
            if i == queue_length -1 :

                result.append(popped_node.val)
            
            #put childrens of the node 
                
            if popped_node.left:
                queue.append(popped_node.left)
            if popped_node.right:
                queue.append(popped_node.right)

    print(result)
    return result
