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
    if tree.getLeftChild() is not None:
        postorder(tree.getLeftChild())
    if tree.getRightChild() is not None:
        postorder(tree.getRightChild())
    print(tree.getRootVal(), end=' ')

def preorder(tree):
    print(tree.getRootVal(), end=' ')
    if tree.getLeftChild() is not None:
        preorder(tree.getLeftChild())
    if tree.getRightChild() is not None:
        preorder(tree.getRightChild())

def inorder(tree):
    if tree.getLeftChild() is not None:
        inorder(tree.getLeftChild())
    print(tree.getRootVal(), end=' ')
    if tree.getRightChild() is not None:
        inorder(tree.getRightChild())

# Problem 3

def printexp(tree):
    # If this is true, then the current node is an operation and has both a
    # leftChild and rightChild that must be wrapped in parentheses.
    if tree.getLeftChild() is not None:
        return (
            "(" +
            printexp(tree.getLeftChild()) +
            tree.getRootVal() +
            printexp(tree.getRightChild()) +
            ")"
        )

    # Otherwise, it is a singular operand.
    else:
        return str(tree.getRootVal())

# Problem 4

problem4_breadth_first_traversal = [0,]
problem4_depth_first_traversal = [0,]

# Problem 5

flights = Graph()
