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
