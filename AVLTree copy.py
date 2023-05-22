#username - Ameer Ahmed
#id1      - 324993690
#name1    - Ameer Ahmed 
#id2      - 324938539
#name2    - Mays Far  
import random

"""A class represnting a node in an AVL tree"""

class AVLNode2(object):
	"""Constructor, you are allowed to add more fields. 
	
	@type key: int or None
	@param key: key of your node
	@type value: any
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.size = 0
		

	"""returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	def get_key(self):
		if(self.key != None):
			return self.key
		return None


	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	def get_value(self):
		if(self.value):
			return self.value
		return None


	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	def get_left(self):
		if (self.left):
			return self.left
		return None


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self):
		if(self.right):
			return self.right
		return None


	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def get_parent(self):
		if self.parent:
			return self.parent
		return None


	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def get_height(self):
		return self.height


	"""returns the size of the subtree

	@rtype: int
	@returns: the size of the subtree of self, 0 if the node is virtual
	"""
	def get_size(self):
		return self.size


	"""sets key

	@type key: int or None
	@param key: key
	"""
	def set_key(self, key):
		self.key = key


	"""sets value

	@type value: any
	@param value: data
	"""
	def set_value(self, value):
		self.value = value


	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node):
		self.left = node


	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node):
		self.right = node


	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node):
		self.parent = node


	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	def set_height(self, h):
		self.height = h


	"""sets the size of node

	@type s: int
	@param s: the size
	"""
	def set_size(self, s):
		self.size = s

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		return self.key != None



"""
A class implementing an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		self.max = None
		self.counter = 0
		# add your fields here

	def printTree(self, node, level=0):
		if node is not None:
			self.printTree(node.right, level + 1)
			print(' ' * 8 * level + '-> ' + str(node.value) + "{" + str(node.get_size()) + "," + str(node.get_height()) + "}")
			self.printTree(node.left, level + 1)


	"""searches for a node in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: node corresponding to key.
	"""
	def search(self, key):
		# a recursive function that searches for the key according to the current node
		def search_rec(node, key):
			if not node.is_real_node():
				return None
			elif node.key == key:
				return node
			elif node.key > key:
				return search_rec(node.get_left(),key)
			else:
				return search_rec(node.get_right(), key)
		
		# return the result of calling the search_rec function with the root
		return search_rec(self.root, key)

	"""inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, key, val):

		num = 0 # the number of rotations
		foundCriminal = False

		# insert bst
		newNode = AVLNode(key, val)
		vrL = AVLNode(None,0)
		vrR = AVLNode(None, 0)
		newNode.set_right(vrR)
		newNode.set_left(vrL)
		vrL.set_parent(newNode)
		vrR.set_parent(newNode)
		newNode.set_height(0)
		newNode.set_size(1)
		if (self.get_root() == None):
			self.set_root(newNode)
			return 0

		parent = None
		child = self.get_root()
		while (child.is_real_node()):
			parent = child
			# print(str(child.get_key()) + " size added")
			child.set_size(child.get_size() + 1) # change the size of the current node
			if key < child.get_key():
				child = child.get_left()
			else:
				child = child.get_right()

		newNode.set_parent(parent)

		
		if key < parent.key:
			parent.set_left(newNode)
		else:
			parent.set_right(newNode)	



		# while(parent != None):
		# 	parent.set_height(max(parent.get_left().get_height(), parent.get_right().get_height()) + 1)
		# 	parent = parent.get_parent()

		# update hight until a rotation and fix AVL Criminals
		while (parent != None):
			bfParent = self.getBF(parent)
			oldHeight = parent.get_height()
			parent.set_height(max(parent.get_left().get_height(), parent.get_right().get_height()) + 1)
			grandParent = parent.get_parent()

			if (not foundCriminal):
				if abs(bfParent) < 2:
					if (parent.get_height() == oldHeight):
						num = 0
						foundCriminal = True
					else:
						parent = grandParent

				elif abs(bfParent) == 2:
					foundCriminal = True
					# L
					if bfParent == 2:
						bfLParent = self.getBF(parent.get_left())
						# LL
						if  bfLParent == 1:
							self.rotate_right(parent)

							num = 1

						# LR
						if bfLParent == -1:
							left = self.rotate_left(parent.get_left())
							parent.set_left(left)
							left.set_parent(parent)
							self.rotate_right(parent)
							num = 2

					# R
					elif bfParent == -2:
						bfRParent = self.getBF(parent.get_right())

						# RR
						if bfRParent == -1 :
							self.rotate_left(parent)
							num = 1

						# RL
						if bfRParent == 1:
							parent.set_right(self.rotate_right(parent.get_right()))
							self.rotate_left(parent)
							num = 1
					parent = grandParent
				
			else:
				parent = grandParent

		return num
	

	
	def getBF(self, node):
		return node.get_left().get_height() - node.get_right().get_height()

	def rotate_right(self, node):
		# node is the node with a |bf| > 1

		# the left child of node
		left = node.get_left()
		# the right child of the left child of node
		leftR = left.get_right()
		# the parent of node
		parent = node.get_parent()


		# change the left child and the right child
		left.set_right(node)
		node.set_parent(left)
		node.set_left(leftR)
		leftR.set_parent(node)
		left.set_parent(parent)
		if(node == self.get_root()):
			self.set_root(left)
			left.set_parent(None)
		else:
			if(parent.get_left() == node):
				parent.set_left(left)
			else:
				parent.set_right(left)

		# change the heights
		node.set_height(1 + max(node.get_left().get_height(), node.get_right().get_height()))
		node.set_size(node.get_left().get_size() + node.get_right().get_size() + 1)
		left.set_height(1 + max(left.get_left().get_height(), left.get_right().get_height()))
		left.set_size(left.get_left().get_size() + left.get_right().get_size() + 1)

		# return left in order to continue traversing the tree upward
		return left

	def rotate_left(self, node):
		# get the right child of node
		right = node.get_right()
		# get the left child of right
		rightL = right.get_left()
		# the parent of node
		parent = node.get_parent()


		# change the left child and the right child
		right.set_left(node)
		node.set_parent(right)
		node.set_right(rightL)
		rightL.set_parent(node)
		right.set_parent(parent)

		if(node == self.get_root()):
			self.set_root(right)
			right.set_parent(None)
		else:
			if(parent.get_right() == node):
				parent.set_right(right)
			else:
				parent.set_left(right)

		node.set_height(1 + max(node.get_left().get_height(), node.get_right().get_height()))
		node.set_size(node.get_left().get_size() + node.get_right().get_size() + 1)
		right.set_height(1 + max(right.get_left().get_height(), right.get_right().get_height()))
		right.set_size(right.get_left().get_size() + right.get_right().get_size() + 1)


		return right
	
	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""


# while(parent != None):
# 			parent.set_size(y.get_size() - 1)
# 			parent.set_height(max(parent.get_left().get_height(), parent.get_right().get_height()))
# 			parent = parent.get_parent()

	def delete(self, node):
		
		if (self.root == None):
			return 0
		
		numRotations = 0 #the number of rotations to make the tree balanced

		# successor = self.successor(node)

		parent = self.deleteBst(node) # delete the node as in a bst
		print(parent)

		# traverse up to make rotations while needed
		terminate = False
		while (parent != None):
			oldHeight = parent.get_height()
			parent.set_size(parent.get_size() - 1)
			parent.set_height(max(parent.get_left().get_height(), parent.get_right().get_height()) + 1)
			bfParent = self.getBF(parent)
			newParent = parent.get_parent()

			if (not terminate):
				if abs(bfParent) < 2:
					if (parent.get_height() != oldHeight):
						parent = newParent
					else:
						terminate = True
						parent = newParent

				elif abs(bfParent) == 2:
					# L
					if bfParent == 2:
						bfLParent = self.getBF(parent.get_left())
						# LL
						if  bfLParent >= 0:
							self.rotate_right(parent)

						# LR
						if bfLParent < 0:
							parent.set_left(self.rotate_left(parent.get_left()))
							self.rotate_right(parent)

						numRotations += 1	

					# R
					elif bfParent == -2:
						bfRParent = self.getBF(parent.get_right())

						# RR
						if bfRParent <= 0 :
							self.rotate_left(parent)

						# RL
						if bfRParent > 0:
							parent.set_right(self.rotate_right(parent.get_right()))
							self.rotate_left(parent)


					numRotations += 1 # update the rotations number

					parent = newParent
			else:
				parent = newParent # update the parent to its parent
		return numRotations

	# normal bst deletion
	def deleteBst(self, node):
		parent = node.get_parent()

		# node is a leaf:
		if (not node.get_left().is_real_node() and not node.get_right().is_real_node()):
			if (node == parent.get_right()):
				parent.set_right(node.get_right())
				node.get_right().set_parent(parent)
			else:
				parent.set_left(node.get_left())
				node.get_left().set_parent(parent)

		# node has no right child:
		elif(node.get_left().is_real_node() and not node.get_right().is_real_node()):
			nextNode = node.get_left()
			if(node == parent.get_right()):
				parent.set_right(nextNode)
	
			else:
				parent.set_left(nextNode)
			nextNode.set_parent(parent)
		# node has no left child:
		elif(node.get_right().is_real_node() and not node.get_left().is_real_node()):
			nextNode = node.get_right()
			if(node == parent.get_right()):
				parent.set_right(nextNode)
			else:
				parent.set_left(nextNode)
			nextNode.set_parent(parent)

		# node has both children:
		else:
			y = self.successor(node)

			parent = y.get_parent()
			flag = parent == node # if the parent of the successor is the node

			# replace node by y
			y.set_parent(node.get_parent())
			y.set_left(node.get_left())
			node.get_left().set_parent(y)
			
			if(not flag):
				# delete y from the tree
				parent.set_left(y.get_right())
				y.get_right().set_parent(parent)
				y.set_right(node.get_right())
				node.get_right().set_parent(y)
			
			if(node == self.get_root()):
				self.set_root(y)
			else:
				if(node.get_parent().get_left() == node):
					node.get_parent().set_left(y)
				else:
					node.get_parent().set_right(y)
				
			y.set_size(y.get_right().get_size() + y.get_left().get_size() + 1)
			if(flag):
				return y
		
		return parent
		
	# return the successor of a given node
	def successor(self, node):
		
		if (node.get_right().is_real_node()):
			node = node.get_right()
			while(node.get_left().is_real_node()):
				# node.set_size(node.get_size() - 1)
				node = node.get_left()
			return node
		else:
			while (node.get_parent() != None and node.get_parent().get_right() == node):
				node = node.get_parent()
			return node.get_parent()
	
	# return the predecessor of a given node
	# def predecessor(self, node):



	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array_rec(self,root):
		if root == None or root.get_key() == None:
			return []
		if self.not_leaf(root):
			arr = self.avl_to_array_rec(root.get_left()) + [root.key] + self.avl_to_array_rec(root.get_right())
			return arr
		return [root.get_key()]
	
	def avl_to_array(self):
		return self.avl_to_array_rec(self.root)

	def not_leaf(self,node):
		return node.get_right().is_real_node() or node.get_left().is_real_node()


	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.get_root().get_size()	

	
	"""splits the dictionary at a given node

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node):
		T1 = AVLTree()
		T1.set_root(node.get_left()) # smaller nodes 
		
		T2 = AVLTree()
		T2.set_root(node.get_right()) # bigger nodes

		parent = node.get_parent()
		node.get_left().set_parent(None)
		node.get_right().set_parent(None)

		vrNode = AVLNode(None, 0)

		node.set_right(vrNode)
		node.set_left(vrNode)

		while(parent != None):
			if(parent.get_right() == node):
				left = AVLTree()
				left.set_root(parent.get_left())
				left.get_root().set_parent(None)
				parent.set_left(vrNode)
				T1.join(left, parent.get_key(), parent.get_value())
				T1.printTree(T1.get_root())
				node = parent
				parent.get_right().set_parent(None)
				parent.set_right(vrNode)


			else:
				right = AVLTree()
				right.set_root(parent.get_right())
				right.get_root().set_parent(None)
				parent.set_right(vrNode)
				T2.join(right, parent.get_right().get_key(), parent.get_value())
				node = parent
				parent.get_left().set_parent(None)
				parent.set_left(vrNode)
			parent = parent.get_parent()

		T1.printTree(T1.get_root())
		T2.printTree(T2.get_root())
		return [T1, T2]
		

	
	"""joins self with key and another AVLTree

	@type tree: AVLTree 
	@param tree: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree are larger than key,
	or the other way around.
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def join(self, tree, key, value):
		# root = self.get_root()
		heightSelf = self.get_root().get_height()
		heightTree = tree.get_root().get_height()

		addedNode =  AVLNode(key, value)

		if(not self.get_root() and not tree.get_root()):
			self.set_root(addedNode)
		elif(not self.get_root()):
			tree.insert(addedNode)
			self.set_root(tree.get_root())
		elif(not tree.get_root()):
			self.insert(addedNode)


		A = None
		B = None

		if heightSelf < heightTree:
			A = self
			B = tree
		else:
			A = tree
			B = self

		node = B.get_root()
		parent = None

		if(A.get_root().get_key() < B.get_root().get_key()):
			while(node.get_height() > A.get_height()):
				node = node.get_left()
			parent = node.get_parent()
			addedNode.set_parent(parent)
			addedNode.set_left(A.get_root())
			A.get_root().set_parent(addedNode)
			addedNode.set_right(node)
			node.set_parent(addedNode)
			parent.set_left(addedNode)
		else:
			while(node.get_height() > A.get_root().get_height()):
				node = node.get_right()
			parent = node.get_parent()
			addedNode.set_parent(parent)
			addedNode.set_right(A.get_root())
			A.get_root().set_parent(addedNode)
			addedNode.set_left(node)
			node.set_parent(addedNode)
			parent.set_right(addedNode)


		bf_addedNode = self.getBF(addedNode)

		c = addedNode
		while (c != None):
			oldHeight = c.get_height()
			c.set_size(c.get_left().get_size() + c.get_right().get_size() + 1)
			c.set_height(max(c.get_left().get_height(), c.get_right().get_height()))
			bfC = self.getBF(c)
			newParent = c.get_parent()

			if (newParent == None):
				self.set_root(c)

			
			if abs(bfC) < 2:
				if (c.get_height() != oldHeight):
					c = newParent
			
			elif abs(bfC) == 2:
				# L
				if bfC == 2:
					bfLC = self.getBF(c.get_left())
					# LL
					if  bfLC >= 0:
						self.rotate_right(parent)
					
					# LR
					elif bfLC < 0:
						c.set_left(self.rotate_left(c.get_left()))
						self.rotate_right(c)
				# R
				elif bfC == -2:
					bfRC = self.getBF(c.get_right())

					# RR
					if bfRC <= 0 :
						self.rotate_left(c)

					# RL
					if bfRC > 0:
						c.set_right(self.rotate_right(c.get_right()))
						self.rotate_left(c)
				c = newParent
			



		return bf_addedNode
		
		

	"""compute the rank of node in the self

	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary which we want to compute its rank
	@rtype: int
	@returns: the rank of node in self
	"""
	def rank(self, node):
		if(node.get_left):
			rankNode = node.get_left().get_size() + 1
		else:
			rankNode = 1
		while node.get_parent() != None:
			parent = node.get_parent()
			if(parent.get_right() == node):
				if(parent.get_left()):
					rankNode += parent.get_left().get_size() + 1
				else:
					rankNode += 1
			node = node.get_parent()
		return rankNode
				


	"""finds the i'th smallest item (according to keys) in self

	@type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@rtype: int
	@returns: the item of rank i in self
	"""
	def select(self, i):
		x = self.root

		while True:
			r = x.get_left().get_size() + 1
			if i == r:
				return x
			elif i < r:
				x = x.get_left()
			else:
				i = i - r
				x = x.get_right()
		

	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root
	
	def set_root(self, node):
		self.root = node
	
	def insertFinger(self, key, val):
		#( key> self.max.get_key()):
		#	self.max = AVLNode(key)

		num = 0 # the number of rotations
		foundCriminal = False

		
		# insert finger
		newNode = AVLNode(key, val)
		vrL = AVLNode(None,0)
		vrR = AVLNode(None, 0)
		newNode.set_right(vrR)
		newNode.set_left(vrL)
		vrL.set_parent(newNode)
		vrR.set_parent(newNode)
		newNode.set_height(0)
		newNode.set_size(1)
		
		# if the root is none
		if (self.get_root() == None):
			self.set_root(newNode)
			self.get_root().set_parent(None)
			self.max = newNode
			return 0
		
		# the node to start updating the sizes and heights
		parent = None
		parentPointer = parent
		# if the inserted node is bigger than the current max
		if (newNode.get_key() > self.max.get_key()):
			self.max.set_right(newNode)
			newNode.set_parent(self.max)
			self.max = newNode
			parent = newNode.get_parent()
			parentPointer = parent
			self.counter += 1

		# the inserted node is smaller than the max
		else:
			parent = self.max.get_parent()
			child = self.max
			while (parent != None and parent.get_key() > newNode.get_key() ):
				parent = parent.get_parent()
				self.counter += 1
				child = child.get_parent()
			
			# INSERT starting from the child node as the root
			while child.is_real_node():
				if(child.get_key() > newNode.get_key()):
					child = child.get_left()
				else:
					child = child.get_right()
				self.counter += 1
			
			# connect the new node to the parent of the child (child currently is virtual)
			parent = child.get_parent()
			parentPointer = parent
			newNode.set_parent(parent)
			if key < parent.get_key():
				parent.set_left(newNode)
			else:
				parent.set_right(newNode)	
			
		# update thes sizes starting from the parent of the new Node (parent)
		while parent != None:
			parent.set_size(parent.get_left().get_size() + parent.get_right().get_size() + 1)
			parent = parent.get_parent()


		while (parentPointer != None):
			bfParent = self.getBF(parentPointer)
			oldHeight = parentPointer.get_height()
			parentPointer.set_height(max(parentPointer.get_left().get_height(), parentPointer.get_right().get_height()) + 1)
			grandParent = parentPointer.get_parent()

			if (not foundCriminal):
				if abs(bfParent) < 2:
					if (parentPointer.get_height() == oldHeight):
						num = 0
						foundCriminal = True
					else:
						parentPointer = grandParent

				elif abs(bfParent) == 2:
					self.counter += 1
					foundCriminal = True
					# L
					if bfParent == 2:
						bfLParent = self.getBF(parentPointer.get_left())
						# LL
						if  bfLParent == 1:
							self.rotate_right(parentPointer)

							num = 1

						# LR
						if bfLParent == -1:
							left = self.rotate_left(parentPointer.get_left())
							parentPointer.set_left(left)
							left.set_parent(parentPointer)
							self.rotate_right(parentPointer)
							num = 2

					# R
					elif bfParent == -2:
						bfRParent = self.getBF(parentPointer.get_right())

						# RR
						if bfRParent == -1 :
							self.rotate_left(parentPointer)
							num = 1

						# RL
						if bfRParent == 1:
							parentPointer.set_right(self.rotate_right(parentPointer.get_right()))
							self.rotate_left(parentPointer)
							num = 1
					parentPointer = grandParent
				
			else:
				parentPointer = grandParent

		return num

	def buildTree(i):
		newTree= AVLTree2()
		values = list(range(1, i+1))
		random.shuffle(values)
		for value in values:
			if(newTree.get_root()==None):
				newNode= AVLNode2(value, 10)
				newTree.set_root(newNode)
			newTree.insert(value,10)
		return newTree
		

	def split2(self, node):
		sum=0
		num = 0
		max = 0
		T1 = AVLTree()
		T1.set_root(node.get_left()) # smaller nodes 
		
		T2 = AVLTree()
		T2.set_root(node.get_right()) # bigger nodes

		parent = node.get_parent()
		node.get_left().set_parent(None)
		node.get_right().set_parent(None)

		vrNode = AVLNode(None, 0)

		node.set_right(vrNode)
		node.set_left(vrNode)

		while(parent != None):
			if(parent.get_right() == node):
				left = AVLTree()
				left.set_root(parent.get_left())
				left.get_root().set_parent(None)
				parent.set_left(vrNode)
				heightDiff = T1.join(left, parent.get_key(), parent.get_value())
				sum = sum+ heightDiff
				num = num+1
				if heightDiff > max:
					max = heightDiff
				T1.printTree(T1.get_root())
				node = parent
				parent.get_right().set_parent(None)
				parent.set_right(vrNode)


			else:
				right = AVLTree()
				right.set_root(parent.get_right())
				right.get_root().set_parent(None)
				parent.set_right(vrNode)
				heightDiff = T2.join(right, parent.get_right().get_key(), parent.get_value())
				sum = sum + heightDiff
				num = num + 1
				if heightDiff >max:
					max = heightDiff
				node = parent
				parent.get_left().set_parent(None)
				parent.set_left(vrNode)
			parent = parent.get_parent()

		T1.printTree(T1.get_root())
		T2.printTree(T2.get_root())
		return [sum, num, max]
	
		
	def join2(self, tree, key, value):
		# root = self.get_root()
		heightSelf = self.get_root().get_height()
		heightTree = tree.get_root().get_height()

		addedNode =  AVLNode(key, value)

		if(not self.get_root() and not tree.get_root()):
			self.set_root(addedNode)
		elif(not self.get_root()):
			tree.insert(addedNode)
			self.set_root(tree.get_root())
		elif(not tree.get_root()):
			self.insert(addedNode)

		A = None
		B = None

		if heightSelf < heightTree:
			A = self
			B = tree
		else:
			A = tree
			B = self

		node = B.get_root()
		parent = None

		if(A.get_root().get_key() < B.get_root().get_key()):
			while(node.get_height() > A.get_height()):
				node = node.get_left()
			parent = node.get_parent()
			addedNode.set_parent(parent)
			addedNode.set_left(A.get_root())
			A.get_root().set_parent(addedNode)
			addedNode.set_right(node)
			node.set_parent(addedNode)
			parent.set_left(addedNode)
		else:
			while(node.get_height() > A.get_root().get_height()):
				node = node.get_right()
			parent = node.get_parent()
			addedNode.set_parent(parent)
			addedNode.set_right(A.get_root())
			A.get_root().set_parent(addedNode)
			addedNode.set_left(node)
			node.set_parent(addedNode)
			parent.set_right(addedNode)


		bf_addedNode = self.getBF(addedNode)

		c = addedNode
		while (c != None):
			oldHeight = c.get_height()
			c.set_size(c.get_left().get_size() + c.get_right().get_size() + 1)
			c.set_height(max(c.get_left().get_height(), c.get_right().get_height()))
			bfC = self.getBF(c)
			newParent = c.get_parent()

			if (newParent == None):
				self.set_root(c)

			
			if abs(bfC) < 2:
				if (c.get_height() != oldHeight):
					c = newParent
			
			elif abs(bfC) == 2:
				# L
				if bfC == 2:
					bfLC = self.getBF(c.get_left())
					# LL
					if  bfLC >= 0:
						self.rotate_right(parent)
					
					# LR
					elif bfLC < 0:
						c.set_left(self.rotate_left(c.get_left()))
						self.rotate_right(c)
				# R
				elif bfC == -2:
					bfRC = self.getBF(c.get_right())

					# RR
					if bfRC <= 0 :
						self.rotate_left(c)

					# RL
					if bfRC > 0:
						c.set_right(self.rotate_right(c.get_right()))
						self.rotate_left(c)
				c = newParent
			



		return bf_addedNode