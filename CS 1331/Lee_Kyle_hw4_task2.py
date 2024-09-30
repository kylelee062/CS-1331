class TreeNode:
    def __init__(self, value, left=None, right=None):
        #Initialize a treenode object with a value and optional left and right child nodes
        self.value = value
        self.left = left
        self.right = right

def tree_height(node):
    #Function to calculate the height of the tree rooted at node.
    if node is None:
        return 0
    else:
        left_height = tree_height(node.left)
        right_height = tree_height(node.right)
        return max(left_height, right_height) + 1

def count_leaves(node):
    #Function to count the number of leaf nodes in the tree rooted at node
    if node is None:
        return 0
    elif node.left is None and node.right is None:
        return 1
    else:
        return count_leaves(node.left) + count_leaves(node.right)

def is_full(node):
    #Function to check if the binary tree rooted at node is full
    if node is None:
        return True
    elif node.left is None and node.right is None:
        return True
    elif node.left is not None and node.right is not None:
        return is_full(node.left) and is_full(node.right)
    else:
        return False

def is_balanced(node):
    #Function to check if the binary tree rooted at node is balanced.
    if node is None:
        return True
    left_height = tree_height(node.left)
    right_height = tree_height(node.right)
    return abs(left_height - right_height) <= 1 and is_balanced(node.left) and is_balanced(node.right)

def tree_info(node):
    #Function to print information about the binary tree rooted at node
    height = tree_height(node)
    leaf_count = count_leaves(node)  
    full = "Yes" if is_full(node) else "No" 
    balanced = "Yes" if is_balanced(node) else "No"  
    #Prints the information
    print("Height of the tree:", height)
    print("Number of leaf nodes:", leaf_count)
    print("Is Full:", full)
    print("Is Balanced:", balanced)

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

tree_info(root)
