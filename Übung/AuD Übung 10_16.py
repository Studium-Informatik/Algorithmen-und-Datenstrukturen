class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def toBinTreeArr(self):
        queue = [self]
        result = []

        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.value)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        return result

    def toArray(self):
        if not self:
            return []
        if not self.left and not self.right:
            return [self.value]
        if not self.left:
            return [self.value] + self.right.toArray()
        if not self.right:
            return self.left.toArray() + [self.value]
        return self.left.toArray() + [self.value] + self.right.toArray()

    def print_tree(self):
        """Prints the tree in a level-order manner."""
        if self is None:
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


def add(node, tree):
    if tree is None:
        return Node(node)
    if tree.value == node:
        return tree
    if node < tree.value:
        tree.left = add(node, tree.left)
    else:
        tree.right = add(node, tree.right)
    return tree


def remove(node, tree):
    if tree is None:
        return tree

    if node < tree.value:
        tree.left = remove(node, tree.left)
    elif node > tree.value:
        tree.right = remove(node, tree.right)
    else:
        # Node found, handle the three cases
        if tree.left is None:
            return tree.right
        elif tree.right is None:
            return tree.left
        else:
            # Node with two children: Get the in-order predecessor
            max_node = find_max(tree.left)
            tree.value = max_node.value
            tree.left = remove(max_node.value, tree.left)

    return tree

def find_max(tree):
    current = tree
    while current.right is not None:
        current = current.right
    return current


def main():
    addNodes = [5, 2, 7, 8, 4, 1, 2, 9, 6, 3]

    tree = None
    for node in addNodes:
        tree = add(node, tree)
        tree.print_tree()
        print("-" * 30)


    # Removing nodes
    removeNodes = [5, 1, 5, 2, 7]
    for node in removeNodes:
        print(f"Removing {node}...")
        tree = remove(node, tree)
        tree.print_tree()
        print(tree.toArray())
        print("-" * 30)


if __name__ == "__main__":
    main()
