class Tree:

    def __init__(self):
        self.root = None

    def search(self, value):
        found_node = self._search(self.root, value)
        if found_node == None:
            return False
        return True

    def delete(self, value):
        pass

    def max_value(self):
        pass

    def min_value(self):
        pass

    def insert(self, value):

        if self.root is None:
            self.root = Node(value)
            return

        return self._insert(self.root, value)

    def _insert(self, current_node, value):
        # go to right
        if value > current_node.value:
            # add right leaf if absent
            if current_node.right is None:
                current_node.right = Node(value, current_node)
                return
                # search for a proper position in right branch
            return self._insert(current_node.right, value)
        else:
            # add left leaf if absent
            if current_node.left is None:
                current_node.left = Node(value, current_node)
                return
            return self._insert(current_node.left, value)

    def _search(self, node_to_check, value):

        # no more nodes, our parent is a leaf
        # we found: searched value is equal to the node
        if (node_to_check == None) or (node_to_check.value == value):
            return node_to_check

        if value > node_to_check.value:
            # go right
            return self._search(node_to_check.right, value)
        else:
            # go left
            return self._search(node_to_check.left, value)

    def bypass (self, root):
        result = []
        if root:
            result.append(root.value)
            result += self.bypass(root.left)
            result += self.bypass(root.right)
        return result


class Node:

    def __init__(self, value, parent=None):
        self.right = None
        self.left = None
        self.parent = None
        self.value = value



tree = Tree()
tree.insert(15)
tree.insert(6)
tree.insert(7)
tree.insert(4)
tree.insert(5)
tree.insert(23)
tree.insert(69)
tree.insert(30)

print(tree.search(10))
print(tree.search(4))
print(tree.search(6))
print(tree.bypass(tree.root))
