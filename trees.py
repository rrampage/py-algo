__author__ = 'rrampage'
# Code for Lectures 5 and 6 of MIT 6.006, Fall 2011 OCW


class BstNode:
    left = None
    right = None
    parent = None

    # A Binary Tree Node has 3 pointers, 2 to it's children and 1 to it's parent
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right



