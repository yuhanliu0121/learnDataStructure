class Set:
	def __init__(self):
		self._elements = list()
	
	def __len__(self):
		return len(self._elements)
	
	def __contain__(self, item):
		return item in self._elements
		
	def add(self, item):
		if item not in self._elements:
			self._elements.append(item)
	
	def remove(self, item):
		assert item in self._elements, "element not in the set"
		self._elements.remove(item)
	
	def __eq__(self, other_set):
		assert isinstance(other_set, Set), "the operation must be done with two sets"
		if len(self) == len(other_set):
			return self.isSubsetOf(other_set)
		else:
			return False
	
	def isSubsetOf(self, other_set):
		for e1 in self:
			if e1 not in other_set:
				return False
		return True
		
	def __iter__(self):
		return self._elements.__iter__()
	
	def union(self, other_set):
		assert isinstance(other_set, Set), "the operation must be done with two sets"
		new_set = Set()
		new_set._elements.extend(other_set)
		for e in self:
			if e not in new_set:
				new_set.add(e)
		return new_set
		
	def interset(self, other_set):
		assert isinstance(other_set, Set), "the operation must be done with two sets"
		new_set = Set()
		for e in self:
			if e in other_set:
				new_set.add(e)
		return new_set
	
	def difference(self, other_set):
		assert isinstance(other_set, Set), "the operation must be done with two sets"
		new_set = Set()
		for e in self:
			if e  not in other_set:
				new_set.add(e)
		for e in other_set:
			if e not in self:
				new_set.add(e)
		return new_set
	
	def __str__(self):
		return str(self._elements)
	
			