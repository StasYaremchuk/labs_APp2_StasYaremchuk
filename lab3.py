class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def invert_binary_tree(tree):
    if tree:
        tree.left, tree.right = tree.right, tree.left
        invert_binary_tree(tree.left)
        invert_binary_tree(tree.right)
    return tree


def level_order(root):
    if not root:
        return
    queue = [root]
    while queue:
        next_queue = []
        for node in queue:
            print(node.value, end=' ')
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        print()
        queue = next_queue


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)


print("Оригінальне дерево:")
level_order(root)

invert_binary_tree(root)
print("\nІнвертоване дерево:")
level_order(root)
