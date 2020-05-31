class Bag(object):
	def __init__(self):
		self._head = None
		self._len = 0
	
	def __len__(self):
		return self._len
		
	def __contains__(self, target):
		current_node = self._head
		while current_node != None and current_node.data != target:
			current_node = current_node.next
		
		return current_node != None
		
	def __iter__(self):
		return _BagIterator(self._head)
	
	def add(self, data):
		new_node = _BagListNode(data)
		new_node.next = self._head
		self._head = new_node
		self._len += 1
		
	def remove(self, target):
		assert target in self, "item not in the bag"
		
		pre_node = None
		current_node = self._head
		
		while current_node != None and current_node.data != target:
			pre_node = current_node
			current_node = current_node.next
			
		if current_node != None:
			if current_node == self._head:
				self._head = self._head.next
				self._len -= 1
				return current_node.data
			else:
				pre_node.next = current_node.next
				self._len -= 1
				return current_node.data
			

class _BagListNode(object):
	def __init__(self, data):
		self.data = data
		self.next = None
		
class _BagIterator(object):
	def __init__(self, head):
		self.current_node = head
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.current_node != None:
			temp = self.current_node.data
			self.current_node = self.current_node.next
			return temp
		else:
			raise StopIteration
			
			
def main():
	bag = Bag()
	
	bag.add(1)
	bag.add(2)
	bag.add(4)
	bag.add(5)
	bag.add(17)
	bag.add(19)
	
	print("bag: ")
	for i in bag:
		print(i, end = ' ')
	print()
	print("bag length is %d" % len(bag))
	
	print()
	
	print("remove 1: ")
	bag.remove(1)
	for i in bag:
		print(i, end = ' ')
	
	print()
	
	print("remove 5: ")
	bag.remove(5)
	for i in bag:
		print(i, end = ' ')

	print()
	
	print("remove 19: ")
	bag.remove(19)
	for i in bag:
		print(i, end = ' ')		
	
	
if __name__ == "__main__":
	main()