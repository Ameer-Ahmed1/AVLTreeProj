#username - Ameer Ahmed
#id1      - 324993690
#name1    - Ameer Ahmed 
#id2      - 324938539
#name2    - Mays Far  



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
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
		if(self.key):
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
		# add your fields here



	"""searches for a node in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: node corresponding to key.
	"""
	def search(self, key):
		# a recursive function that searches for the key according to the current node
		def search_rec(node, key):
			if node.key == key:
				return node
			elif node.key > key:
				return search_rec(node.getleft(),key)
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
		parent = None
		child = self.get_root()
		while child != None:
			parent = child
			child.set_size(child.get_size() + 1) # change the size of the current node
			if key < child.get_key(self):
				child = child.get_left(self)
			else:
				child = child.get_right(self)

		newNode.set_parent(parent)

		if parent == None: # tree was empty
			self.root = newNode
			return None
		elif key < parent.key:
			parent.set_left(newNode)
		else:
			parent.set_right(newNode)	

		# update hight until a rotation and fix AVL Criminals
		while (parent != None):
			bfParent = self.getBF(parent)
			oldHeight = parent.get_height()
			parent.set_height(max(parent.get_left().get_height(), parent.get_right().get_height()))

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
							parent.set_left(self.rotate_left(parent.get_left()))
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
							num
				
				else:
					parent = grandParent

	
	def getBF(self, node):
		return node.get_left().get_height() - node.get_right().get_height()

	def rotate_right(self, node):
		# node is the node with a |bf| > 1

		# the left child of node
		left = node.get_left()
		# the right child of the left child of node
		leftR = left.get_right()

		# change the left child and the right child
		left.set_right(node)
		node.set_left(leftR)

		# change the heights
		node.set_height(1 + max(node.get_left().get_height(), node.get_right().get_height()))
		node.set_size(node.get_left().get_size() + node.get_right().get_size())
		left.set_height(1 + max(left.get_left().get_height(), left.get_right().get_heigth()))
		left.set_size(left.get_left().get_size() + left.get_right().get_size())

		# return left in order to continue traversing the tree upward
		return left

	def rotate_left(self, node):
		# get the right child of node
		right = node.get_right()
		# get the left child of right
		rightL = right.get_left()


		# change the left child and the right child
		right.set_left(node)
		node.set_left(rightL)

		node.set_height(1 + max(node.get_left().get_height(), node.get_right().get_height()))
		node.set_size(node.get_left().get_size() + node.get_right().get_size())
		right.set_height(1 + max(right.get_left().get_height(), right.get_right().get_heigth()))
		right.set_size(right.get_left().get_size() + right.get_right().get_size())

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

		parent = self.deleteBst(node) # delete the node as in a bst

		# traverse up to make rotations while needed
		while (parent != None):
			oldHeight = parent.get_height()
			parent.set_size(parent.get_size() - 1)
			parent.set_height(max(parent.get_left().get_height(), parent.get_right().get_height()))
			bfParent = self.getBF(parent)
			newParent = parent.get_parent()

			terminate = False

		if (not terminate):
			if abs(bfParent) < 2:
				if (parent.get_height() != oldHeight):
					parent = newParent
				else:
					terminate = True
			
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
				parent.set_right(None)
			else:
				parent.set_left(None)

		# node has no right child:
		elif(node.get_left() and not node.get_right()):
			nextNode = node.get_left()
			if(node == parent.get_right()):
				parent.set_right(nextNode)
			else:
				parent.set_left(nextNode)

		# node has no left child:
		elif(node.get_right() and not node.get_left()):
			nextNode = node.get_right()
			if(node == parent.get_right()):
				parent.set_right(nextNode)
			else:
				parent.set_left(nextNode)

		# node has both children:
		else:
			y = self.successor(node)

			parent = y.get_parent()
			# delete y from the tree
			y.get_parent().set_left(y.get_right())
			
			# replace node by y
			y.set_parent(node.get_parent())
			y.set_right(node.get_right())
			y.set_left(node.get_left())
		
		

		return parent
		
	# return the successor of a given node
	def successor(self, node):
		if (node.get_right()):

			node = node.get_right()
			while(node.get_left()):
				# node.set_size(node.get_size() - 1)
				node = node.get_left()
			return node
		else:
			while (node.get_parent().get_right() == node):
				node = node.get_parent()
			return node.get_parent()
	
	# return the predecessor of a given node
	# def predecessor(self, node):



	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		return None


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
		return None

	
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
	def join(self, tree, key, val):
		return None


	"""compute the rank of node in the self

	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary which we want to compute its rank
	@rtype: int
	@returns: the rank of node in self
	"""
	def rank(self, node):
		return None


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
				x = self.get_left()
			else:
				i = i - r
		
		


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return None

	