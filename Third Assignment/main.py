
import random


class Node:
    """ This class is a node in Binary Tree """

    def __init__(self, data):
        """ Constructor of a node - setting the value """
        self.right = None
        self.left = None
        self.data = data

    def insert(self, data):
        """
        This Function is inserting data to the right node in the tree
        :param data: The data to insert
        """
        if self.data:
            if data[0] < self.data[0]:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


def build_tree():
    """
    This Function is building binary tree of 1000 nodes
    :return: The root node of the tree
    """
    tree = Node(None)
    taken_points = []
    for i in range(1000):
        point = [random.randint(0, 100), random.randint(0, 100)]
        # if a point is taken - continue randomize points
        while point in taken_points:
            point = [random.randint(0, 100), random.randint(0, 100)]
        taken_points += [point]
        tree.insert(point)
    return tree


def _nearest_right_point(tree, x, min_diff, nearest_point):
    """
    This Function is finding the nearest right point to x line.

    so this is O(log(n))
    :param tree: The root node of the tree
    :param x: The x line
    :param min_diff: The minimal difference until now
    :param nearest_point: The point of the minimal difference
    :return: None (getting from param nearest_point the point)
    """

    # The end of the tree
    if not tree:
        return

    # if the current node x is closer to the x value (from the right)
    if 0 < tree.data[0] - x < min_diff:
        min_diff = tree.data[0] - x
        nearest_point[0] = tree.data

    # if x is smaller then current node x going over left subtree else right
    if x < tree.data[0]:
        _nearest_right_point(
            tree.left,
            x,
            min_diff,
            nearest_point
        )
    else:
        _nearest_right_point(
            tree.right,
            x,
            min_diff,
            nearest_point
        )


def nearest_right_point(tree, x):
    """
    This function is wrapping _nearest_right_point function
    to be able to give nice answer and get less args
    :param tree: The root node of the tree
    :param x: The x line
    :return: The nearest point from the right
    """
    # Initialize as the max difference and the 0,0 point
    min_diff, nearest_point = 100, [[0, 0]]
    _nearest_right_point(tree, x, min_diff, nearest_point)
    return nearest_point[0]


def main():
    line = -1
    while not isinstance(line, int) or line < 0 or line > 100:
        try:
            line = int(input("insert line x - needs to be int between 0-100\n"))
        except Exception:
            print("line must be a natural number ...")
    print("testing on random tree with 1000 nodes")
    print(f"nearest right point is {nearest_right_point(build_tree(), line)}")


if __name__ == '__main__':
    main()