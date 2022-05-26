NB_ROT = 0
REPLACE_VALUE = 0
def reset_nb_rot():
	NB_ROT = 0
class AVL_Node:
	def __init__(self, value):
		self._value = value
		self._left = None
		self._right = None
		self._balance = 0

	def append(self, value):
	#Simply append a value to the tree
		if value < self._value:
			if self._left is None:
				self._left = AVL_Node(value)
			else:
				self._left.append(value)
		elif value > self._value:
			if self._right is None:
				self._right = AVL_Node(value)
			else:
				self._right.append(value)

	def computeBalance(self):
		if self.isLeaf():
			return 0
		if self._left is not None and self._right is not None:
			return self._left.getHeight() - self._right.getHeight()
		elif self._left is not None:
			return 1 + self._left.getHeight()
		else:
			return -1 - self._right.getHeight()

	def applyBalance(self):
		self._balance = self.computeBalance()
		if self._left is not None:
			self._left.applyBalance()
		if self._right is not None:
			self._right.applyBalance()

	def balanceChildren(self):
		if self._left is not None:
			self._left.balanceChildren()
		if self._right is not None:
			self._right.balanceChildren()

		if self._left is not None and self._left.isSimplyLeftUnbalanced():
			self._left = self._left.rot_right()
		if self._left is not None and self._left.isSimplyRightUnbalanced():
			self._left = self._left.rot_left()

		if self._right is not None and self._right.isSimplyLeftUnbalanced():
			self._right = self._right.rot_right()
		if self._right is not None and self._right.isSimplyRightUnbalanced():
			self._right = self._right.rot_left()

		if self._left is not None and self._left.isDifferentlyLeftUnbalanced():
			self._left = self._left.differentRightRotation()
		if self._left is not None and self._left.isDifferentlyRightUnbalanced():
			self._left = self._left.differentRightRotation()

		if self._right is not None and self._right.isDifferentlyLeftUnbalanced():
			self._right = self._right.differentRightRotation()
		if self._right is not None and self._right.isDifferentlyRightUnbalanced():
			self._right = self._right.differentRightRotation()

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
		if self._left is None and self._right is None:
			return True
		return False

	def getHeight(self):
		if self.isLeaf():
			return 0
		leftHeight = 0
		rightHeight = 0
		if self._left is not None:
			leftHeight = self._left.getHeight()
		if self._right is not None:
			rightHeight = self._right.getHeight()
		return max(leftHeight,rightHeight) + 1

	def insert(self, value):
		newArbre = self
		newArbre.append(value)
		newArbre = self.balanceRoot()
		newArbre.balanceChildren()
		newArbre.applyBalance()
		return newArbre
		#Go Left
		if value <= self._value:
			if self._left == None:
				self._left = AVL_Node(value)
			else:
				self._left.insert(value)
			self._balance += 1
			if self.isSimplyLeftUnbalanced():
				newArbre = self.rot_right()
			else:
				newArbre = self
			if self._left is not None and self._left.isSimplyLeftUnbalanced():
				self._left = self._left.rot_right()
			return newArbre
		#Go Right
		else:
			if self._right == None:
				self._right = AVL_Node(value)
			else:
				self._right.insert(value)
			self._balance -= 1
			if self.isSimplyRightUnbalanced():
				newArbre = self.rot_left()
			else:
				newArbre = self
			if self._right is not None and self._right.isSimplyLeftUnbalanced():
				self._right = self._right.rot_right()
			return newArbre

	def isSimplyLeftUnbalanced(self):
		if self._left is not None and self.computeBalance() == 2 and self._left.computeBalance() == 1:
			return True
		return False

	def isDifferentlyLeftUnbalanced(self):
		if self._left is not None and self.computeBalance() == 2 and self._left.computeBalance() == -1:
			return True
		return False

	def isSimplyRightUnbalanced(self):
		if self._right is not None and self.computeBalance() == -2 and self._right.computeBalance() == -1:
			return True
		return False

	def isDifferentlyRightUnbalanced(self):
		if self._right is not None and self.computeBalance() == -2 and self._right.computeBalance() == 1:
			return True
		return False

	def rot_left(self):
		#newRoot = self._right
		#self._right = self._right._left
		#newRoot._left = self
		#return newRoot
		newRoot = self._right
		newLeftRight = self._right._left
		newRoot._left = self
		newRoot._left._right = newLeftRight
		return newRoot

	def rot_right(self):
		newRoot = self._left
		newRightLeft = self._left._right
		newRoot._right = self
		newRoot._right._left = newRightLeft
		return newRoot

	def differentRightRotation(self):
		#formerLeftRightRight = self._left._right._right
		#formerLeftRightLeft = self._left._right._left
		#newRoot = self._left._right
		#newRoot._right = self
		#newRoot._left = self._left
		#newRoot._right._left = formerLeftRightRight
		#newRoot._left._right = formerLeftRightLeft
		self._left = self._left.rot_left()
		newRoot = self.rot_right()
		return newRoot

	def differentLeftRotation(self):
		#formerLeftRightRight = self._left._right._right
		#formerLeftRightLeft = self._left._right._left
		#newRoot = self._left._right
		#newRoot._right = self
		#newRoot._left = self._left
		#newRoot._right._left = formerLeftRightRight
		#newRoot._left._right = formerLeftRightLeft
		self._right = self._right.rot_right()
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
				#self._value = self.getSuccessor()._value
				newArbre = self
				newArbre._value = self.getSuccessor()._value
				newArbre._right = self._right.delete(self.getSuccessor()._value)
				newArbre.applyBalance()
				return newArbre
			self.applyBalance()
			return self

	def getSuccessor(self):
		if self._right is None:
			return self
		if self._right._left is None:
			return self._right
		child = self._right
		while child._left is not None:
			child = child._left
		return child
		
		
				
			

	def printTree(self, level=0):
		print(level*" " + str(self._value) + "(" + str(self.getSuccessor()._value) + ")")
		if self._left != None:
			self._left.printTree(level + 1)
		if self._right != None:
			self._right.printTree(level + 1)

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

if False:
	value = choose()
	arbre = AVL_Node(value)
	arbre.printTree()
	while(True):
		menuChoice = menu()
		while menuChoice not in ["a","d"]:
			menuChoice = menu()
		if menuChoice == "a":
			value = choose()
			arbre = arbre.insert(value)
			arbre.applyBalance()
			#arbre.append(value)
			#arbre = arbre.balanceRoot()
			#arbre.balanceChildren()
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
#print(testArbre._value)