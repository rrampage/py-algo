__author__ = 'rrampage'
# Code for Lectures 5 and 6 of MIT 6.006, Fall 2011 OCW


class BstNode:
    # A Binary Tree Node has 3 pointers, 2 to it's children and 1 to it's parent. It stores a key.
    left = None
    right = None
    parent = None
    key = None

    def __init__(self, key):
        self.key = key

    def insert(self, child):
        if child.key > self.key:
            self.right = child
            child.parent = self
        else:
            self.left = child
            child.parent = self

    @staticmethod
    def is_root(x):
        if x.parent is None:
            return True
        else:
            return False


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


def search(root, k):
    if k == root.key:
        return root
    elif k < root.key:
        return search(root.left, k)
    else:
        return search(root.right, k)

