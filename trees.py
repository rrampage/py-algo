__author__ = 'rrampage'
# Code for Lectures 5 and 6 of MIT 6.006, Fall 2011 OCW

from collections import deque


class BstNode:
    # A Binary Tree Node has 3 pointers, 2 to it's children and 1 to it's parent. It stores a key.
    left = None
    right = None
    parent = None
    key = None
    # height of tree. 0 for leaf.
    height = 0

    def __init__(self, key):
        self.key = key


# Method for BST insert. AVL trees will need to obey the AVL property of height difference between sub-trees <= 1
def insert(node, child):
    if child.key > node.key:
        if node.right is None:
            node.right = child
            child.parent = node
        else:
            insert(node.right, child)
    else:
        if node.left is None:
            node.left = child
            child.parent = node
        else:
            insert(node.left, child)


def is_root(x):
    x.parent is None


def is_leaf(x):
    return (x.right is None) and (x.left is None)


def get_root_node(x):
    x if (x.parent is None) else get_root_node(x.parent)


def height(x):
    return -1 if (x is None) else 1 + (max(height(x.left), height(x.right)))


# Print tree from node. If not root node, sub-tree is printed
# Code from http://stackoverflow.com/a/18945739/1625748
def tree_print(x):
    nodes = deque()
    levels = deque()
    nodes.append(x)
    level = 0
    levels.append(level)
    print level, [x.key]
    while len(nodes) > 0:
        u = nodes.popleft()
        l = levels.popleft()
        if u.left is not None:
            nodes.append(u.left)
            levels.append(l+1)
        if u.right is not None:
            nodes.append(u.right)
            levels.append(l+1)
        # If there is a node still in the queue and all the nodes in the queue
        # are at the same level, then increment the level and print.
        if len(levels) > 0 and levels[0] > level and levels[0] == levels[-1]:
            level += 1
            print level, [x.key for x in nodes]


def max_node(root):
    n = root
    while n.right is not None:
        n = n.right
    return n


def min_node(root):
    n = root
    while n.left is not None:
        n = n.left
    return n


def search(node, key):
    if is_leaf(node):
        return node
    if key == node.key:
        return node
    elif key < node.key:
        return search(node.left, key)
    else:
        return search(node.right, key)


# Rotates node x such that it becomes left child of it's former right child and the parent of right child's left child
# Example:      y-(B,C)         C
#           x -         => y-
#               A               x-(A,B)
def left_rotate(x):
    # Here, y is x's right child. b is y's left child
    # Temporary variable m is used to store x's original parent which will becomes y's parent
    m = x.parent
    y = x.right
    b = y.left
    # Setting x's parent as y's parent and x as y's left child, y as x's parent
    y.parent = m
    y.left = x
    x.parent = y
    # Setting b's parent as x and x's right as b
    b.parent = x
    x.right = b
    # TODO Not sure what to return here.
    # Returning y as it has taken x's position in the tree and is now balanced
    return y


# Rotates node y such that it becomes right child of it's former left child and the parent of left child's right child
# Example:      (C)              (y)-(B,C)
#           y-              => x-
#               (x - (A,B)        A
def right_rotate(y):
    # Here, x is y's left child. b is x's right child
    # Temporary variable m is used to store y's original parent which will becomes x's parent
    m = y.parent
    x = y.left
    b = x.right
    # Setting x's parent as y's parent and x as y's left child, y as x's parent
    x.parent = m
    x.right = y
    y.parent = x
    # Setting b's parent as x and x's right as b
    b.parent = y
    y.left = b
    # TODO Not sure what to return here.
    # Returning x as it has taken y's position in the tree and is now balanced
    return x


def main():
    print "Hello world!"
    a = BstNode(3)
    insert(a, BstNode(4))
    insert(a, BstNode(5))
    insert(a, BstNode(2))
    tree_print(a)
    print height(a)
    print(height(a.right.right))


if __name__ == "__main__":
    import cProfile
    cProfile.run("main()")
