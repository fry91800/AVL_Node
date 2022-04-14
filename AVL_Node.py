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

	def balanceRoot(self):
		if self.isSimplyLeftUnbalanced():	
			return self.simpleRightRotation()
		if self.isSimplyRightUnbalanced():	
			return self.simpleLeftRotation()
		return self
	def isLeaf(self):
		if self.left is None and self.right is None:
			return True
		return False

	def getHeight(self):
		if self.isLeaf():
			return 0
		leftHeight = 0
		rightHeight = 0
		if self.left is not None:
			leftHeight = self.left.getHeight()
		if self.right is not None:
			rightHeight = self.right.getHeight()
		return max(leftHeight,rightHeight) + 1
		

	def getOldHeight(self):
		if self.isLeaf():
			return 0
		else:
			if self.left is None:
				return 1 + self.right.getHeight()
			else:
				return 1 + self.left.getHeight()
		return 1 + max(self.left.getHeight(),self.right.getHeight())

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
		print(level*" " + str(self.value) + "(" + str(self.computeBalance()) + ")")
		if self.left != None:
			self.left.printTree(level + 1)
		if self.right != None:
			self.right.printTree(level + 1)

def choose():
	choice = input("type a number to add, q to quit")
	if choice == "q":
		exit()
	else:
		return int(choice)

value = choose()
arbre = AVL_Node(value)
arbre.printTree()
while(True):
	value = choose()
	arbre.append(value)
	arbre = arbre.balanceRoot()
	arbre.balanceChildren()
	arbre.printTree()
#testArbre = testArbre.simpleRightRotation()
#print(testArbre.value)