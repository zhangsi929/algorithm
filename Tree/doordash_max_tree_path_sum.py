
from re import S
from turtle import right
from construct_binary_tree import ConstructBinaryTree
'''
Doordash:
Given a binary tree, find the maximum path sum from any two "alive nodes" within the tree. 
We can assume a node is an alive node if and only if it is a leaf node,
indicated by an asterisk below.
     5
    /  \
   2    0
  /    /  \
*25   *14  *15
47 = 25 + 2 + 5 + 15
Follow - up
What if any nodes in the tree can be alive instead of just the leaves
'''

case1 = [5, 2, 0, 25, None, 14, 15]
root1 = ConstructBinaryTree.construct_binary_tree_by_horizontal_list(case1)

# class TreeNode:
#     def __init__(self, val) -> None:
#         self.val = val
#         self.left, self.right = None, None

class Solution:
    def findMaxSum(self, root):
        self.max_sum = 0
        if not root:
            return 0
        self.helper(root)
        return self.max_sum
    
    def helper(self, root):
        if not root:
          return 0
        left_max_sum_to_leaf = self.helper(root.left)
        right_max_sum_to_leaf = self.helper(root.right)
        self.max_sum = max(self.max_sum, root.val + left_max_sum_to_leaf + right_max_sum_to_leaf)
        return max(left_max_sum_to_leaf + root.val, right_max_sum_to_leaf + root.val)

solution = Solution()
result = solution.findMaxSum(root1)
print(result)
        



        