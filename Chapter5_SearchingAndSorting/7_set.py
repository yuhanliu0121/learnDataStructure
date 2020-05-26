class Set(object):
	def __init__(self):
		self._elements = list()
		
	def __len__(self):
		return len(self._elements)
		
	def __contains__(self, element):
		pos = self._find_position(element)
		return pos < len(self) and self._elements[pos] == element
		
	def add(self, element):
		if element not in self:
			pos = self._find_position(element)
			self._elements.insert(pos, element)
	
	def remove(self, element):
		assert element in self, "element must be in the set"
		pos = self._find_position(element)
		self._elements.pop(pos)
		
	def __iter__(self):
		return _SetIterator(self._elements)
		
	def __str__(self):
		return str(self._elements)
	
	# O(n) complexity	
	def __eq__(self, other_set):
		if len(self) != len(other_set):
			return False
		for i in range(len(self)):
			if self._elements[i] != other_set._elements[i]:
				return False
		return True
		
	def isSubsetOf(self, another_set):
		n1 = len(self)
		n2 = len(another_set)
		
		if n1 > n2:
			return False
		else:
			idx1 = 0
			idx2 = 0
			TrueCount = 0
			while idx2 < n2 and idx1 < n1:
				if self._elements[idx1] != another_set._elements[idx2]:
					idx2 += 1
				else:
					TrueCount +=1
					idx1 += 1
					idx2 += 1
					
			return TrueCount == n1
	
	def union(self, another_set):
		newSet = Set()
		idx1 = 0
		idx2 = 0
		
		while idx1 < (len(self)) and idx2 < (len(another_set)):
			if self._elements[idx1] < another_set._elements[idx2]:
				newSet._elements.append(self._elements[idx1])
				idx1 += 1
			elif self._elements[idx1] > another_set._elements[idx2]:
				newSet._elements.append(another_set._elements[idx2])
				idx2 +=1
			else:
				newSet._elements.append(self._elements[idx1])
				idx1 += 1
				idx2 += 1
		
		if idx1 >= len(self) - 1:
			newSet._elements.extend(another_set._elements[idx2:])
		else:
			newSet._elements.extend(self._elements[idx1:])
		return newSet
		
	def _find_position(self, element):
		n = len(self)
		low = 0
		high = n - 1
		
		while low <= high:
			mid = (low + high) // 2
			if self._elements[mid] == element:
				return mid
			if self._elements[mid] < element:
				low = mid + 1
			else:
				high = mid - 1
		return low


class _SetIterator(object):
	def __init__(self, the_list):
		self.count = 0
		self.the_list = the_list
		
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.count < len(self.the_list):
			self.count += 1
			return self.the_list[self.count-1]
		else:
			raise StopIteration
		
		
def main():
	s = Set()
	
	s.add(0)
	s.add(1)
	s.add(2)
	s.add(3)
	s.add(4)
	
	s2 = Set()
	
	s2.add(0)
	s2.add(1)
	s2.add(2)
	s2.add(3)
	s2.add(4)
	
	s3 = Set()
	s3.add(0)
	s3.add(15)
	s3.add(2)
	s3.add(1)
	s3.add(100)
	
	print("s1 == s2 : " + str(s == s2))
	print("s3 is subset of s ? " + str(s3.isSubsetOf(s)))
	print("s.union(s3): " + str(s.union(s3)))
	



if __name__ == "__main__":
	main()
		
		
		
		
		
		
		