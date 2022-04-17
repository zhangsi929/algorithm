from construct_binary_tree import ConstructBinaryTree
import sys
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

class Solution:
    def findMaxSum(self, root):
        self.max_sum = -sys.maxsize - 1
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

#follow up
class Solution2:
    def maxPathSum(self, root) -> int:
        if not root:
            return 0
        self.max_sum = root.val
        self.helper(root)
        return self.max_sum
    
    def helper(self, root):
        if not root:
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        self.max_sum = max(self.max_sum, l + r + root.val)
        if l + r + root.val < 0:
            return 0
        return max(l + root.val, r + root.val)

solution = Solution()
result = solution.findMaxSum(root1)
print(result)
        



        