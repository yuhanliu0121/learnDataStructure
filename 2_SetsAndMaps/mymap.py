class Map:

	def __init__(self):
		self._entry = list()
		
	def __len__(self):
		return len(self._entry)
		
	def __contains__(self, key):
		return self._findPosition(key) is not None
	
	def add(self, key, value):
		idx = self._findPosition(key)
		if idx is None:
			self._entry.append(_MapEntry(key, value))
		else:
			self._entry[idx]._value = value
	
	def valueOf(self, key):
		idx = self._findPosition(key)
		assert  idx is not None, "invalide key"
		return self._entry[idx]._value
	
	def remove(self, key):
		idx = self._findPosition(key)
		assert  key in self, "invalide key"
		del self._entry[idx]
	
	def __iter__(self):
		return _MapIterator(self)
		
	def __str__(self):
		str_list = list()
		for (key, value) in self:
			str_list.append((key, value))
		return str(str_list)
	
	def _findPosition(self, key):
		for idx in range(len(self)):
			if self._entry[idx]._key == key:
				return idx
		return None
	
	
class _MapEntry:
	
	def __init__(self, key, value):
		self._key = key
		self._value = value
		
class _MapIterator:
	
	def __init__(self, map):
		self._theMapEntry = map._entry
		self._cur_idx =0
	
	def __next__(self):
		if self._cur_idx < len(self._theMapEntry):
			temp = (self._theMapEntry[self._cur_idx]._key, self._theMapEntry[self._cur_idx]._value)
			self._cur_idx +=1
			return temp
		else:
			raise StopIteration
			
	def __iter__(self):
		return self
	
	
	
	
	
	
	
	
	
	