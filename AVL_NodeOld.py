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

	def applyBalance(self):
		self._balance = self.computeBalance()
		if self._left is not None:
			self._left._balance = self._left.computeBalance()
		if self._right is not None:
			self._right._balance = self._right.computeBalance()

	def balanceChildren(self):
		if self.left is not None:
			self.left.balanceChildren()
		if self.right is not None:
			self.right.balanceChildren()

		if self.left is not None and self.left.isSimplyLeftUnbalanced():
			self.left = self.left.rot_right()
		if self.left is not None and self.left.isSimplyRightUnbalanced():
			self.left = self.left.rot_left()

		if self.right is not None and self.right.isSimplyLeftUnbalanced():
			self.right = self.right.rot_right()
		if self.right is not None and self.right.isSimplyRightUnbalanced():
			self.right = self.right.rot_left()

		if self.left is not None and self.left.isDifferentlyLeftUnbalanced():
			self.left = self.left.differentRightRotation()
		if self.left is not None and self.left.isDifferentlyRightUnbalanced():
			self.left = self.left.differentRightRotation()

		if self.right is not None and self.right.isDifferentlyLeftUnbalanced():
			self.right = self.right.differentRightRotation()
		if self.right is not None and self.right.isDifferentlyRightUnbalanced():
			self.right = self.right.differentRightRotation()

	def balanceRoot(self):
		if self.isSimplyLeftUnbalanced():	
			return self.rot_right()
		if self.isSimplyRightUnbalanced():	
			return self.rot_left()
		if self.isDifferentlyLeftUnbalanced():	
			return self.differentRightRotation()
		if self.isDifferentlyRightUnbalanced():	
			return self.differentLeftRotation()
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

	def insert(self, value):
		#Go Left
		if value <= self.value:
			if self.left == None:
				self.left = AVL_Node(value)
			else:
				self.left.insert(value)
			self.balance += 1
			if self.isSimplyLeftUnbalanced():
				newArbre = self.rot_right()
			else:
				newArbre = self
			if self.left is not None and self.left.isSimplyLeftUnbalanced():
				self.left = self.left.rot_right()
			return newArbre
		#Go Right
		else:
			if self.right == None:
				self.right = AVL_Node(value)
			else:
				self.right.insert(value)
			self.balance -= 1
			if self.isSimplyRightUnbalanced():
				newArbre = self.rot_left()
			else:
				newArbre = self
			if self.right is not None and self.right.isSimplyLeftUnbalanced():
				self.right = self.right.rot_right()
			return newArbre

	def isSimplyLeftUnbalanced(self):
		if self.left is not None and self.computeBalance() == 2 and self.left.computeBalance() == 1:
			return True
		return False

	def isDifferentlyLeftUnbalanced(self):
		if self.left is not None and self.computeBalance() == 2 and self.left.computeBalance() == -1:
			return True
		return False

	def isSimplyRightUnbalanced(self):
		if self.right is not None and self.computeBalance() == -2 and self.right.computeBalance() == -1:
			return True
		return False

	def isDifferentlyRightUnbalanced(self):
		if self.right is not None and self.computeBalance() == -2 and self.right.computeBalance() == 1:
			return True
		return False

	def rot_left(self):
		#newRoot = self.right
		#self.right = self.right.left
		#newRoot.left = self
		#return newRoot
		newRoot = self.right
		newLeftRight = self.right.left
		newRoot.left = self
		newRoot.left.right = newLeftRight
		return newRoot

	def rot_right(self):
		newRoot = self.left
		newRightLeft = self.left.right
		newRoot.right = self
		newRoot.right.left = newRightLeft
		return newRoot

	def differentRightRotation(self):
		#formerLeftRightRight = self.left.right.right
		#formerLeftRightLeft = self.left.right.left
		#newRoot = self.left.right
		#newRoot.right = self
		#newRoot.left = self.left
		#newRoot.right.left = formerLeftRightRight
		#newRoot.left.right = formerLeftRightLeft
		self.left = self.left.rot_left()
		newRoot = self.rot_right()
		return newRoot

	def differentLeftRotation(self):
		#formerLeftRightRight = self.left.right.right
		#formerLeftRightLeft = self.left.right.left
		#newRoot = self.left.right
		#newRoot.right = self
		#newRoot.left = self.left
		#newRoot.right.left = formerLeftRightRight
		#newRoot.left.right = formerLeftRightLeft
		self.right = self.right.rot_right()
		newRoot = self.rot_left()
		return newRoot

	def delete(self, value):
		if self.isLeaf():
			if self._value != value:
				return self
			else:
				return None
		else:
		#Go left
			if value < self._value:
				if self._left is not None:
					self._left = self._left.delete(value)
				else:
					return self
		#Go Right
			if value > self._value:
				if self._right is not None:
					self._right = self._right.delete(value)
				else:
					return self
		#Delete
			if value == self._value:
				if self._right is None:
					return self._left
				if self._left is None:
					return self._right
				self._value = self.getSuccessor()._value
				self.delete(value)
				return newArbre
			return self

	def getSuccessor(self):
		child = self.right
		while child.left is not None:
			child = child.left
		return child
		
		
				
			

	def printTree(self, level=0):
		print(level*" " + str(self.value) + "(" + str(self.computeBalance()) + ")")
		if self.left != None:
			self.left.printTree(level + 1)
		if self.right != None:
			self.right.printTree(level + 1)

def choose():
	choice = int(input("type a number, q to quit"))
	if choice == "q":
		exit()
	else:
		return int(choice)

def menu():
	choice = input("a to add, d to delete, q to quit")
	if choice == "q":
		exit()
	else:
		return choice

if True:
	value = choose()
	arbre = AVL_Node(value)
	arbre.printTree()
	while(True):
		menuChoice = menu()
		while menuChoice not in ["a","d"]:
			menuChoice = menu()
		if menuChoice == "a":
			value = choose()
			arbre.append(value)
			arbre = arbre.balanceRoot()
			arbre.balanceChildren()
			arbre.printTree()
		elif menuChoice == "d":
			value = choose()
			arbre.delete(value)
			arbre = arbre.balanceRoot()
			arbre.balanceChildren()
			arbre.printTree()
	for i in range(1,10):
		value = choose()
		arbre.append(value)
		arbre = arbre.balanceRoot()
		arbre.balanceChildren()
		arbre.printTree()
	choice = int(input("type a number to DELETE, q to quit"))
	arbre.delete(choice)
	arbre = arbre.balanceRoot()
	arbre.balanceChildren()
	arbre.printTree()
	quit()
#testArbre = testArbre.rot_right()
#print(testArbre.value)