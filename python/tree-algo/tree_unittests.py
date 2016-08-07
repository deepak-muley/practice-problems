import unittest

from tree import BinaryTree, BinaryTreeNode

class TreeUnitTests(unittest.TestCase):
    
    def setUp(self):
    	pass

    def tearDown(self):
    	pass

    def createBinaryTree(self):
    	#((a + b) - c)/d
    	tree = BinaryTree()
    	root = tree.setRoot('/')
     	nodeMinus = root.addLeft('-')
     	nodeD = root.addRight('d')
     	nodePlus= nodeMinus.addLeft('+')
     	nodeC = nodeMinus.addRight('c')
     	nodeA = nodePlus.addLeft('a')
     	nodeB = nodePlus.addRight('b')
     	return tree


    def createBinarySearchTree(self):
    	pass

    def test_print_inorder(self):
    	tree = self.createBinaryTree()
    	tree.inorderTraversalWithRecursion(tree.getRoot())
        print "\n"

    def test_print_preorder(self):
	tree = self.createBinaryTree()
	tree.preorderTraversalWithRecursion(tree.getRoot())
        print "\n"

    def test_print_postorder(self):
	tree = self.createBinaryTree()
	tree.postorderTraversalWithRecursion(tree.getRoot())
        print "\n"

if __name__ == '__main__':
    unittest.main()
