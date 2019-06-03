# ECS32B Spring 2019 Homework 6
# Your name here!


# Grab some helper functions into the current namespace
from hw6_tools import *


# Problem 1

expTree = None

# Problem 2

def postorder(tree):
    raise NotImplementedError

def preorder(tree):
    raise NotImplementedError

def inorder(tree):
    raise NotImplementedError

# Problem 3

def printexp(tree):
    sVal = ""
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild())+')'
    return sVal

# Problem 4

problem4_breadth_first_traversal = [0,]
problem4_depth_first_traversal = [0,]

# Problem 5

flights = Graph()
