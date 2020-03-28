from myarray import Array

class Array2D:

	def __init__(self, num_row, num_col):
		assert num_row >0 and  num_col >0, "Array size must > 0"
		
		self._row_array = Array(num_row)
		for i in range(num_row):
			self._row_array[i] = Array(num_col)
		self.clear(None)
			
	def num_rows(self):
		return len(self._row_array)
		
	def num_cols(self):
		return len(self._row_array[0])
		
	def clear(self, value):
		for i in range(self.num_rows()):
			for j in range(self.num_cols()):
				self._row_array[i][j] = value
			
	def __getitem__(self, idx):
		assert len(idx) ==2, "expected two index"
		row_idx = idx[0]
		col_idx = idx[1]
		assert 0<= row_idx <= self.num_rows() and 0<= col_idx <= self.num_cols(), "index out of range"
		return self._row_array[row_idx][col_idx]
		
	def __setitem__(self, idx, value):
		assert len(idx) ==2, "expected two index"
		row_idx = idx[0]
		col_idx = idx[1]
		assert 0<= row_idx <= self.num_rows() and 0<= col_idx <= self.num_cols(), "index out of range"
		self._row_array[row_idx][col_idx] = value			
			
			
			
			
			
			
			
			
			
			