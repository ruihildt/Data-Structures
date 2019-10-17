import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        # set the value at the current node
        self.value = value
        # add ref to left child node
        self.left = None
        # add ref to the right child node
        self.right = None

    # Insert the given value into the tree
    def insert(self, value_to_insert):
        # LEFT CASE
        # check if the new nodes value is less than our current ones value
        if value_to_insert < self.value:
            # if the is no left child,
            if self.left == None:
                # place a new node here
                self.left = BinarySearchTree(value_to_insert)
                return
            # otherwise
            else:
                # repeat process for left
                self.left.insert(value_to_insert)

        # RIGHT CASE
        # check if the new nodes value is greater than or equal to the current parent value
        if value_to_insert >= self.value:
            # if there is no right child here
            if self.right == None:
                # place a new one
                self.right = BinarySearchTree(value_to_insert)
                return
            # otherwise
            else:
                # repeat process right
                self.right.insert(value_to_insert)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Check if root node value is equal to target
        if self.value == target:
            # Return True
            return True

        # Check if target is smaller than node value
        if target < self.value and self.left:
            # Search recursively
            return self.left.contains(target)

        # Check if target is bigger or equal to node value
        if target > self.value and self.right:
            # Search recursively
            return self.right.contains(target)

        # Return False when no value has been found
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        # BASE CASE 
        # if empty tree
        if not self:
            # return none
            return None
        
        # RECURSIVE
        # if the the is no right value
        if not self.right:
            # return the root value
            return self.value
        # return the get max of the the right node
        return self.right.get_max()

        # ITTERATIVE
        # set a max value variable to keep track of max value
        # get a ref to current node
        # check if we are at a valid tree node
            # if our current value is greater than the max value
                # update the max value
            # move on to the next right node in the tree
            # setting the current node to the current nodes right
        # return our max value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # base case
        if self.value:
            cb(self.value)

        # left case
        if self.left:
            self.left.for_each(cb)

        # right case
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if not node:
            return None
        
        if self.left:
            return self.left.in_order_print(self.left)

        print(self.value)

        if self.right:
            return self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # use a queue data structure
        q = Queue()
        # enqueue the starting node on to the queue
        q.enqueue(node)
        # loop while the queue has data
        while q.len():
            # dequeue the current item off the queue
            current_node = q.dequeue()
            # print the current value
            print(current_node)
            # if the current node has a left child
            if current_node.left:
                # enqueue the left child on to the queue
                q.enqueue(current_node.left)
            # if the current node has a right child
            if current_node.right:
                # enqueue right child on to the queue
                q.enqueue(current_node.right)          

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # use a stack data structure
        s = Stack()
        # push the starting node on to the stack
        s.push(node)
        # loop while the stack has data
        while s.len():
            # pop the current item off the stack
            current_node = s.pop()
            # print the current value
            print(current_node.value)
            # if the current node has a left child
            if current_node.left:
                # push the left child on to the stack
                s.push(current_node.left)
            # if the current node has a right child
            if current_node.right:
                # push right child on to the stack   
                s.push(current_node.right)       

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
