__author__ = 'rrampage'
# Code for Lectures 5 and 6 of MIT 6.006, Fall 2011 OCW


class BstNode:
    left = None
    right = None
    parent = None
    key = None

    # A Binary Tree Node has 3 pointers, 2 to it's children and 1 to it's parent. It stores a key.
    # When initializing a node, we point it to it's parent and fill it with the relevant data
    def __init__(self, parent, key):
        self.parent = parent
        self.key = key



