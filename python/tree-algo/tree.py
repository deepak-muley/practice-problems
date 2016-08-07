class Node:
    def __init__(self, data):
        self.data = data

    def getData(self):
        return self.data

class BinaryTreeNode(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.left = None
        self.right = None

    def createNode(self, data):
        return BinaryTreeNode(data)

    def addLeft(self, data):
        self.left = self.createNode(data)
        return self.getLeft()

    def addRight(self, data):
        self.right = self.createNode(data)
        return self.getRight()

    def removeLeft(self):
        self.left = None

    def removeRight(self):
        self.right = None

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

class BinarySearchTreeNode(BinaryTreeNode):
    pass

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def setRoot(self, data):
        self.root = self.createTreeNode(data)
        return self.getRoot()

    def createTreeNode(self, data):
        return Node(data)

    def preorderTraversalWithRecursion(self, root):
        if root == None:
            return
        print root.getData()
        self.preorderTraversalWithRecursion(root.left)
        self.preorderTraversalWithRecursion(root.right)

    def inorderTraversalWithRecursion(self, root):
        if root == None:
            return
        self.inorderTraversalWithRecursion(root.left)
        print root.getData()
        self.inorderTraversalWithRecursion(root.right)

    def postorderTraversalWithRecursion(self, root):
        if root == None:
            return
        self.postorderTraversalWithRecursion(root.left)
        self.postorderTraversalWithRecursion(root.right)
        print root.getData()

    def preorderTraversalWithStack(self):
        pass

    def inorderTraversalWithStack(self):
        pass

    def postorderTraversalWithStack(self):
        pass

    def sizeOfTree(self):
        pass

    def heightOfTree(self):
        pass

    def findAnElement(self, data):
        pass

    def findMinMaxElement(self):
        pass

    def findNumberOfLeafNodes(self):
        pass

    def findNumberOfFullNodes(self):
        pass

    def findSecondLargesNumber(self):
        pass

class BinaryTree(Tree):
    def createTreeNode(self, data):
        return BinaryTreeNode(data)

class BinarySearchTree(Tree):
    def createTreeNode(self, data):
        return BinarySearchTreeNode(data)

