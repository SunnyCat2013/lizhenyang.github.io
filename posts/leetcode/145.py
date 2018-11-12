# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        # stack_arr = []
        # stack_arr.append(root)
        # idx = 0
        # count = 1
        # while idx < count:
        #     # p_node = TreeNode(None)
        #     p_node = stack_arr[idx] # 这个是给了个指针？
        #     if p_node.right:
        #         count += 1
        #         stack_arr.append(p_node.right)
        #     if p_node.left:
        #         count += 1
        #         stack_arr.append(p_node.left)
        #     idx += 1
        stack_arr = []
        res = []
        stack_arr.append(root)
        while len(stack_arr) > 0:
            p_node = stack_arr[-1]
            print(res)
            print(p_node.val)
            print(p_node.left)
            print(p_node.right)
            if (p_node.left is None) and (p_node.right is None):
                print('return value')
                res.append(stack_arr.pop().val)
                continue
            if p_node.right:
                print('right')
                # stack_arr[-1].right = None
                stack_arr.append(p_node.right)
                p_node.right = None

            if p_node.left is not None:
                print('left')
                # stack_arr[-1].left = None
                stack_arr.append(p_node.left)
                p_node.left = None

        return res

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
b.left = c
a.right = b

solvor = Solution()
solvor.postorderTraversal(a)