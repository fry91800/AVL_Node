class AVL_Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.balance = 0

	def append(self, value):
	#Simply append a value to the tree
		if value < self.value:
			if self.left is None:
				self.left = AVL_Node(value)
			else:
				self.left.append(value)
		elif value > self.value:
			if self.right is None:
				self.right = AVL_Node(value)
			else:
				self.right.append(value)

	def computeBalance(self):
		if self.isLeaf():
			return 0
		if self.left is not None and self.right is not None:
			return self.left.getHeight() - self.right.getHeight()
		elif self.left is not None:
			return 1 + self.left.getHeight()
		else:
			return -1 - self.right.getHeight()

	def balanceChildren(self):
		if self.left is not None:
			self.left.balanceChildren()
		if self.right is not None:
			self.right.balanceChildren()
		if self.left is not None and self.left.isSimplyLeftUnbalanced():
			self.left = self.left.simpleRightRotation()
		if self.left is not None and self.left.isSimplyRightUnbalanced():
			self.left = self.left.simpleLeftRotation()
		if self.right is not None and self.right.isSimplyLeftUnbalanced():
			self.right = self.right.simpleRightRotation()
		if self.right is not None and self.right.isSimplyRightUnbalanced():
			self.right = self.right.simpleLeftRotation()
	def isLeaf(self):
		if self.left is None and self.right is None:
			return True
		return False

	def getHeight(self):
		if self.isLeaf():
			return 0
		else:
			if self.left is None:
				return 1 + self.right.getHeight()
			else:
				return 1 + self.left.getHeight()
		return max(self.left.getHeight(),self.right.getHeight())

	def insert(self, value):
		#Go Left
		if value <= self.value:
			if self.left == None:
				self.left = AVL_Node(value)
			else:
				self.left.insert(value)
			self.balance += 1
			if self.isSimplyLeftUnbalanced():
				newArbre = self.simpleRightRotation()
			else:
				newArbre = self
			if self.left is not None and self.left.isSimplyLeftUnbalanced():
				self.left = self.left.simpleRightRotation()
			return newArbre
		#Go Right
		else:
			if self.right == None:
				self.right = AVL_Node(value)
			else:
				self.right.insert(value)
			self.balance -= 1
			if self.isSimplyRightUnbalanced():
				newArbre = self.simpleLeftRotation()
			else:
				newArbre = self
			if self.right is not None and self.right.isSimplyLeftUnbalanced():
				self.right = self.right.simpleRightRotation()
			return newArbre

	def isSimplyLeftUnbalanced(self):
		if self.left is not None and self.computeBalance() == 2 and self.left.computeBalance() == 1:
			return True
		return False

	def isSimplyRightUnbalanced(self):
		if self.right is not None and self.computeBalance() == -2 and self.right.computeBalance() == -1:
			return True
		return False

	def simpleLeftRotation(self):
		newRoot = self.right
		self.right = self.right.left
		newRoot.left = self
		return newRoot

	def simpleRightRotation(self):
		newRoot = self.left
		self.left = self.left.right
		newRoot.right = self
		return newRoot

	def changeLeftChildren(self):
		self.left.value = 8

	def printTree(self, level=0):
		print(level*" " + str(self.value))
		if self.left != None:
			self.left.printTree(level + 1)
		if self.right != None:
			self.right.printTree(level + 1)

testArbre = AVL_Node(10)
testArbre.append(11)
testArbre.append(12)
testArbre.append(13)
testArbre.append(14)
testArbre.append(15)
testArbre.append(16)
testArbre.append(17)
testArbre.printTree()
#testArbre = testArbre.simpleRightRotation()
#print(testArbre.value)