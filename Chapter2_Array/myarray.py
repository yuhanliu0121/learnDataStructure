import ctypes

class Array:
	
	def __init__(self, size):
		assert size > 0, "Array size must > 0"
		self._size = size
		ArrayType = ctypes.py_object * size
		self._items = ArrayType()
		self.clear(None)
	
	def __len__(self):
		return self._size
	
	def __getitem__(self, idx):
		assert 0<= idx <len(self), "index out of range"
		return self._items[idx]
	
	def __setitem__(self, idx, value):
		assert 0<= idx <len(self), "index out of range"
		self._items[idx] = value
	
	def clear(self, value):
		for i in range(len(self)):
			self._items[i] = value
			
	def __iter__(self):
		return _ArrayIterator(self)
		
		
class _ArrayIterator:
	
	def __init__(self, array):
		self._theArray = array
		self._cur_idx = 0
		
	def __next__(self):
		if self._cur_idx < len(self._theArray):
			temp = self._theArray[self._cur_idx]
			self._cur_idx += 1
			return temp
		else:
			raise StopIteration
			
	def __iter__(self):
		return self
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		