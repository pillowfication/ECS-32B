# ECS32B Spring 2019 Homework 6
# Your name here!
# Markus Tran
# mkhtran@ucdavis.edu

# Grab some helper functions into the current namespace
from hw6_tools import *


# Problem 1

def p(leftOperand, operator, rightOperand):
    tree = ExpTree(operator)
    tree.setLeftChild(leftOperand if isinstance(leftOperand, ExpTree) else ExpTree(leftOperand))
    tree.setRightChild(rightOperand if isinstance(rightOperand, ExpTree) else ExpTree(rightOperand))
    return tree

expTree = p(p(3, '+', p(1, '/', 2)), '*', p(5, '-', 2))

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