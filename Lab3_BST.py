import Queue, Stack

class Node:
    
    def __init__(self, val):
        self.value = val # Node value
        self.left = None # Left child
        self.right = None # Right child

class BST:

    def __init__(self, val):
        self.root = Node(val) # Root of the tree
        self.size = 1 # Number of nodes in the tree

    def __len__(self): 
        return self.size # Get size of the tree

    def contains(self, root, key):
        if self.isEmpty():
            raise Exception("Tree is empty") 
        if root.value == key: # If node with searched key is found
            return True
        elif root.value > key and root.left is not None: 
            return self.contains(root.left, key) # Go to the left subtree
        elif root.value < key and root.right is not None:
            return self.contains(root.right, key) # Go to the right subtree
        else:
            return False

    def insert(self, root, key):
        if self.isEmpty():
            self.root = Node(key) # Create new root
            self.size += 1
        elif root.value == key:
            raise Exception("The inserted value is already in the tree")
        elif root.value > key:
            if root.left is None: # If no left child
                root.left = Node(key) # Create left child
                self.size += 1
            else:
                self.insert(root.left, key) # Go to left subtree
        elif root.value < key:
            if root.right is None: # If no right child
                root.right = Node(key) # Create right child
                self.size += 1
            else:
                self.insert(root.right, key) # Go to right subtree

    def remove(self, root, key):
        if self.isEmpty():
            raise Exception("Tree is empty")
        elif root is None:
            return root
        elif root.value == key: # If node to delete is found
            if root.left is None: # If node has only right child or doesnt have children
                if root.value == self.root.value: # If node is root
                    self.root = root.right
                root = root.right # Replace node with right child
                self.size -= 1
            elif root.right is None: # If node has only left child or doesnt have children
                if root.value == self.root.value: # If node is root
                    self.root = root.left
                root = root.left # Replace node with left child
                self.size -= 1
            else: # If node has both children
                cur = root.right
                while cur.left is not None: # Search for min node in right subtree of the node
                    cur = cur.left
                root.value, cur.value = cur.value, root.value # Swap node with min node
                root.right = self.remove(root.right, cur.value) # Delete node
        elif root.value > key: # Go to left subtree
            root.left = self.remove(root.left, key)
        else: # Go to right subtree
            root.right = self.remove(root.right, key)
        return root

    def isEmpty(self):
        if self.root is None:
            return True
        else: 
            return False


# Iterator for depth-first traversal
class DFT_Iterator:
    
    def __init__(self, root):
        self.stack = Stack.Stack() # Initialize stack
        self.stack.push(root) # Push root node to the stack

    def __next__(self): 
        if self.has_next():
            temp = self.stack.pop() # Get the top node from the stack
            if temp.right is not None: # Push right child to the stack if it exists
                self.stack.push(temp.right)
            if temp.left is not None: # Push left child to the stack if it exists
                self.stack.push(temp.left)
            return temp.value # Return value of current node
        else:
            raise StopIteration # If traversal is done

    def has_next(self):
        if self.stack.isEmpty():
            return False
        else:
            return True


# Iterator for breadth-first traversal
class BFT_Iterator:

    def __init__(self, root):
        self.queue = Queue.Queue() # Initialize queue
        self.queue.enqueue(root) # Push root to the queue

    def __next__(self):
        if self.has_next():
            temp = self.queue.dequeue() # Get first node from the queue
            if temp.left is not None: # Add left child to the queue if it exists
                self.queue.enqueue(temp.left)
            if temp.right is not None: # Add right child to the queue if it exists
                self.queue.enqueue(temp.right)
            return temp.value # Return value of the current node
        else:
            raise StopIteration # If traversal is done

    def has_next(self):
        if self.queue.isEmpty():
            return False
        else:
            return True
