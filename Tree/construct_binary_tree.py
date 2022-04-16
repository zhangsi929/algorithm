class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left, self.right = None, None

class ConstructBinaryTree:
    @staticmethod
    def construct_binary_tree_by_horizontal_list(input):
        node_list = []
        for val in input:
            if isinstance(val, int):
                node = TreeNode(val)
                node_list.append(node)
            else:
                node = None
                node_list.append(node)

        for i, node in enumerate(node_list):
            left = i * 2 + 1
            right = i * 2 + 2
            if node:
                if left <= len(node_list) - 1: node.left = node_list[left]
                if right <= len(node_list) - 1: node.right = node_list[right]
            else:
                continue
        return node_list[0]

# test1 = ConstructBinaryTree()
# root = ConstructBinaryTree.construct_binary_tree_by_horizontal_list([1, 2, 3])
# print(root.val)
# print(root.right.val)


        