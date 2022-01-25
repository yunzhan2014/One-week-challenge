class Solution:
            def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
                
                def merge(node1, node2):
                    if not node1: return node2
                    if not node2: return node1
                    node1.val += node2.val
                    node1.left = merge(node1.left, node2.left)
                    node1.right = merge(node1.right, node2.right)
                    return node1
                    
                result = merge(root1, root2)
                return result