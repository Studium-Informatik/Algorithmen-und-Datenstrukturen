class Tree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def empty():
        """Returns an empty tree."""
        return None

    def is_empty(self):
        """Checks if the tree is empty."""
        return self is None

    def depth(self):
        """Computes the depth of the tree."""
        if self.is_empty():
            return 0
        else:
            return 1 + max(self.left.depth(), self.right.depth())


    @staticmethod
    def node(value, left=None, right=None):
        """Creates a tree node with a value and two subtrees."""
        return Tree(value, left, right)

    @staticmethod
    def value(tree):
        """Returns the value of the tree's root node."""
        if Tree.is_empty(tree):
            raise ValueError("The tree is empty")
        return tree.value

    @staticmethod
    def left(self):
        """Returns the left subtree of the root node."""
        if self.is_empty():
            raise ValueError("The tree is empty")
        return self.left

    @staticmethod
    def right(self):
        """Returns the right subtree of the root node."""
        if self.is_empty():
            raise ValueError("The tree is empty")
        return self.right

    @staticmethod
    def print_tree(self):
        """Prints the tree in a level-order manner."""
        if self.is_empty():
            print("The tree is empty")
            return

        # To store nodes at each level
        level_nodes = []
        # Queue for level-order traversal
        queue = [(self, 0)]
        current_level = 0
        current_level_nodes = []

        while queue:
            node, level = queue.pop(0)
            if level != current_level:
                level_nodes.append(current_level_nodes)
                current_level_nodes = []
                current_level = level
            current_level_nodes.append(node.value if node else None)
            if node:
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))

        # Add the last level
        if current_level_nodes:
            level_nodes.append(current_level_nodes)

        # Print the tree level by level
        max_width = 2 ** (len(level_nodes) - 1) - 1
        for i, level in enumerate(level_nodes):
            indent = ' ' * (max_width // (2 ** i))
            space_between = ' ' * (max_width // (2 ** (i - 1)) if i > 0 else 0)
            level_str = indent
            level_str += space_between.join(str(node) if node is not None else ' ' for node in level)
            print(level_str)


class BinNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def new(value):
        """Creates a new node with a given value."""
        return BinNode(value)

    def value(self):
        """Returns the value of the node."""
        if self is None:
            raise ValueError("The node is None")
        return self.value

    @staticmethod
    def left(self):
        """Returns the left subtree of the node."""
        if self is None:
            raise ValueError("The node is None")
        return self.left

    @staticmethod
    def right(self):
        """Returns the right subtree of the node."""
        if self is None:
            raise ValueError("The node is None")
        return self.right

    @staticmethod
    def set_value(self, new_value):
        """Sets the value of the node."""
        if self is None:
            raise ValueError("The node is None")
        self.value = new_value
        return self

    @staticmethod
    def set_left(self, left_subtree):
        """Sets the left subtree of the node."""
        if self is None:
            raise ValueError("The node is None")
        self.left = left_subtree
        return self

    @staticmethod
    def set_right(self, right_subtree):
        """Sets the right subtree of the node."""
        if self is None:
            raise ValueError("The node is None")
        self.right = right_subtree
        return self


def preorder(tree):
    """Traverses the tree in preorder."""
    if Tree.is_empty(tree):
        return []
    else:
        return [Tree.value(tree)] + preorder(Tree.left(tree)) + preorder(Tree.right(tree))


def postorder(tree):
    """Traverses the tree in postorder."""
    if Tree.is_empty(tree):
        return []
    else:
        return postorder(Tree.left(tree)) + postorder(Tree.right(tree)) + [Tree.value(tree)]


def levelorder(tree):
    """Traverses the tree in level order."""
    if Tree.is_empty(tree):
        return []
    else:
        queue = [tree]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(Tree.value(node))
            if Tree.left(node):
                queue.append(Tree.left(node))
            if Tree.right(node):
                queue.append(Tree.right(node))
        return result


def main():
    # Create a binary tree
    tree = Tree.node(3,
                     Tree.node(7,
                               Tree.node(4),
                               Tree.node(2)),
                     Tree.node(1,
                               Tree.node(8),
                               Tree.node(6)
                               )
                     )

    # Display the tree
    Tree.print_tree(tree)

    # Traverse the tree in different orders
    print("Preorder traversal:", preorder(tree))
    print("Postorder traversal:", postorder(tree))
    print("Level-order traversal:", levelorder(tree))


if __name__ == '__main__':
    main()
