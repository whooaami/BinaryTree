import math


class Node:

    def __init__(self, value, parent=None):
        self.right = None
        self.left = None
        self.parent = None
        self.value = value


class Tree:

    def __init__(self):
        self.root = None

    def search(self, value):
        found_node = self._search(self.root, value)
        if found_node == None:
            return False
        return True

    def delete(self, value):
        node_to_delete = self._search(self.root, value)
        if node_to_delete is None:
            return
        elif not node_to_delete.left and not node_to_delete.right:
            self._delete_leaf(node_to_delete)
        elif node_to_delete.left and not node_to_delete.right:
            self._delete_node_with_left_child(node_to_delete)
        elif node_to_delete.right and not node_to_delete.left:
            self._delete_node_with_right_child(node_to_delete)
        else:
            self._delete_root(node_to_delete)

    def _delete_leaf(self, node_to_delete):
        if node_to_delete.parent.left == node_to_delete:
            node_to_delete.parent.left = None
        else:
            node_to_delete.parent.right = None
        return

    def _delete_node_with_right_child(self, node_to_delete):
        node_to_delete.value = node_to_delete.right.value
        node_to_delete.right = None

    def _delete_node_with_left_child(self, node_to_delete):
        node_to_delete.value = node_to_delete.left.value
        node_to_delete.left = None

    def _delete_root(self, node_to_delete):
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

    def bypass(self, root):
        result = []
        if root:
            result.append(root.value)
            result += self.bypass(root.left)
            result += self.bypass(root.right)
        return result

    # printing graph stuff
    def print_ascii_graph(self):
        pairs = self._get_pairs_in_order()
        self.print_by_lines(pairs)

    def print_spaces(self, num):
        str = num * " "
        print(str, end="")

    def print_arrows(self, nodes_count, space_from_start):
        self.print_spaces(space_from_start)
        for i in range(nodes_count // 2):
            print("/", end="")
            self.print_spaces(space_from_start * 2)
            print("\\", end="")
            self.print_spaces(space_from_start * 2)

    def print_nodes(self, nodes, space_from_start):
        self.print_spaces(space_from_start)
        while nodes:
            print(nodes.pop(0), end="")
            self.print_spaces(space_from_start * 2)

    def print_by_lines(self, pairs):

        if self.root is None:
            return

        count_pairs = len(pairs)
        count_lines = int(math.log2(count_pairs)) + 1
        nums_on_last_line = pow(count_lines, count_lines - 1)

        pairs_per_line = 1
        spaces_from_start = nums_on_last_line // 2

        # print root
        self.print_spaces(spaces_from_start * 2)
        print(self.root.value)

        for i in range(count_lines):

            nums_in_line = []

            for j in range(pairs_per_line):
                if not pairs:
                    break

                # print(pairs.pop(0), end=" ")
                pair = pairs.pop(0)
                nums_in_line.append(pair[0])
                nums_in_line.append(pair[1])

            self.print_arrows(len(nums_in_line), spaces_from_start)
            print()
            self.print_nodes(nums_in_line, spaces_from_start)
            print()

            spaces_from_start //= 2

            pairs_per_line *= 2

    def _get_pairs_in_order(self):
        if self.root is None:
            return

        queue = [self.root]
        pairs = []
        for i in queue:
            pair = []
            if i.left is not None:
                queue.append(i.left)
                pair.append(i.left.value)
            else:
                pair.append("")

            if i.right is not None:
                queue.append(i.right)
                pair.append(i.right.value)
            else:
                pair.append("")

            pairs.append(pair)

        return pairs


if __name__ == '__main__':
    tree = Tree()
    tree.insert(15)
    tree.insert(6)
    tree.insert(7)
    tree.insert(4)
    tree.insert(5)
    tree.insert(23)
    tree.insert(69)
    tree.insert(30)

    tree.delete(6)
    tree.delete(69)
    tree.delete(69)

    print(tree.bypass(tree.root))
    print(tree.print_ascii_graph())
