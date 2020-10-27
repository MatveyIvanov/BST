import unittest

import Lab3_BST as bst


class TestBST(unittest.TestCase):

    # Initialization for each method 
    def setUp(self):
        self.tree = bst.BST(8)
        self.tree.insert(self.tree.root, 3)   #          8
        self.tree.insert(self.tree.root, 10)  #         / \
        self.tree.insert(self.tree.root, 1)   #        3   10
        self.tree.insert(self.tree.root, 6)   #       / \    \ 
        self.tree.insert(self.tree.root, 14)  #      1   6    14
        self.tree.insert(self.tree.root, 4)   #         / \   /
        self.tree.insert(self.tree.root, 7)   #        4   7 13
        self.tree.insert(self.tree.root, 13)
        self.dft_iter = bst.DFT_Iterator(self.tree.root)
        self.bft_iter = bst.BFT_Iterator(self.tree.root)

    def test_init(self):
        tree = bst.BST(8)
        self.assertEqual(len(tree), 1) # Test size
        self.assertIsNone(tree.root.right) 
        self.assertIsNone(tree.root.left)

    def test_size(self):
        self.assertEqual(len(self.tree), 9)

    def test_contains_exception(self):
        tree = bst.BST(8)
        tree.remove(tree.root, 8)
        try:
            tree.contains(tree.root, 8)
        except Exception as e:
            self.assertEqual(str(e), "Tree is empty")

    def test_contains(self):
        self.assertTrue(self.tree.contains(self.tree.root, 13)) # True
        self.assertFalse(self.tree.contains(self.tree.root, 50)) # False
    
    def test_insert_to_empty_tree(self):
        tree = bst.BST(8)
        tree.remove(tree.root, 8)
        tree.insert(tree.root, 5)
        self.assertEqual(tree.root.value, 5) # Check if new root is correct
        self.assertEqual(len(tree), 1) # Check size

    def test_insert_to_empty_tree_with_traversal(self):
        tree = bst.BST(5)
        tree.remove(tree.root, 5)
        tree.insert(tree.root, 4)
        traversal = []
        iterator = bst.DFT_Iterator(tree.root)
        traversal.append(next(iterator))
        self.assertListEqual(traversal, [4]) # If the traversal matches the expected result

    def test_insert_exception(self):
        try:
            self.tree.insert(self.tree.root, 6) # Value already exists in the tree
        except Exception as e:
            self.assertEqual(str(e), "The inserted value is already in the tree")

    def test_insert_size(self):
        self.tree.insert(self.tree.root, 50)
        self.assertEqual(len(self.tree), 10) # Check size

    def test_insert_traversal(self):
        self.tree.insert(self.tree.root, 2)
        traversal = []
        for _ in range(len(self.tree)): # DFT
            traversal.append(next(self.dft_iter))
        self.assertListEqual(traversal, [8, 3, 1, 2, 6, 4, 7, 10, 14, 13]) # If the traversal matches the expected result

    def test_remove_exception(self):
        tree = bst.BST(1)
        tree.remove(tree.root, 1)
        try:
            tree.remove(tree.root, 4) # Trying to remove from empty tree
        except Exception as e:
            self.assertEqual(str(e), "Tree is empty") # If the traversal matches the expected result

    def test_remove_leaf_size(self):
        self.tree.remove(self.tree.root, 13) # Removing leaf
        self.assertEqual(len(self.tree), 8) # Check size

    def test_remove_leaf_traversal(self):
        self.tree.remove(self.tree.root, 13)
        traversal = []
        for _ in range(len(self.tree)): # DFT
            traversal.append(next(self.dft_iter))
        self.assertListEqual(traversal, [8, 3, 1, 6, 4, 7, 10, 14]) # If the traversal matches the expected result

    def test_remove_node_with_one_child_size(self):
        self.tree.remove(self.tree.root, 10)
        self.assertEqual(len(self.tree), 8) # Check size

    def test_remove_node_with_one_child_traversal(self):
        self.tree.remove(self.tree.root, 10) # Removing node with 1 child
        traversal = []
        for _ in range(len(self.tree)): # DFT
            traversal.append(next(self.dft_iter))
        self.assertListEqual(traversal, [8, 3, 1, 6, 4, 7, 14, 13]) # If the traversal matches the expected result

    def test_remove_node_with_two_children_size(self):
        self.tree.remove(self.tree.root, 3)
        self.assertEqual(len(self.tree), 8) # Check size

    def test_remove_node_with_two_children_traversal(self):
        self.tree.remove(self.tree.root, 3) # Removing node with 2 childs
        traversal = []
        for _ in range(len(self.tree)):
            traversal.append(next(self.dft_iter))
        self.assertListEqual(traversal, [8, 4, 1, 6, 7, 10, 14, 13]) # If the traversal matches the expected result

    def test_remove_root(self):
        self.tree.remove(self.tree.root, 8) # Removing root
        traversal = []
        for _ in range(len(self.tree)): # DFT
            traversal.append(next(self.dft_iter))
        self.assertListEqual(traversal, [10, 3, 1, 6, 4, 7, 14, 13]) # If the traversal matches the expected result

    def test_is_empty(self):
        tree = bst.BST(1)
        self.assertFalse(tree.isEmpty()) # Size is 1
        tree.remove(tree.root, 1)
        self.assertTrue(tree.isEmpty()) # Size is 0

    def test_dft_iterator(self):
        traversal = []
        for _ in range(len(self.tree)): # DFT
            traversal.append(next(self.dft_iter))
        self.assertListEqual(traversal, [8, 3, 1, 6, 4, 7, 10, 14, 13]) # If the DFT matches the expected result

    def test_bft_iterator(self):
        traversal = []
        for _ in range(len(self.tree)): # BFT
            traversal.append(next(self.bft_iter))
        self.assertListEqual(traversal, [8, 3, 10, 1, 6, 14, 4, 7, 13]) # If the BFT matches the expected result
