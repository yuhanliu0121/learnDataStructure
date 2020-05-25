from myarray2d import Array2D

class Matrix(Array2D):

	def scaleBy(self, scalar):
		for i in range(self.num_rows()):
			for j in range(self.num_cols()):
				self[i, j] *= scalar
	
	def transpose(self):
		trans = Matrix(self.num_cols(), self.num_rows())
		for i in range(trans.num_rows()):
			for j in range(trans.num_cols()):
				trans[i, j] = self[j, i]
		return trans
		
	def show(self):
		for i in range(self.num_cols()):
			print('')
			for j in range(self.num_rows()):
				print(str(self[j, i]) + ' ', end='')
        
	def __add__(self, other):
		assert isinstance(other, Matrix), "both operators must be Matrix" 
		assert self.num_rows() == other.num_rows() and self.num_cols() == other.num_cols(), "dimensions do not agree"
		
		result = Matrix(self.num_rows(), self.num_cols())
		for i in range(result.num_rows()):
			for j in range(result.num_cols()):
				result[i, j] = self[i, j] + other[i, j]
		return result
		
	def __sub__(self, other):
		assert isinstance(other, Matrix), "both operators must be Matrix" 
		assert self.num_rows() == other.num_rows() and self.num_cols() == other.num_cols(), "dimensions do not agree"
		
		result = Matrix(self.num_rows(), self.num_cols())
		for i in range(result.num_rows()):
			for j in range(result.num_cols()):
				result[i, j] = self[i, j] - other[i, j]
		return result
	
	def __mul__(self, other):
		assert isinstance(other, Matrix), "both operators must be Matrix" 
		assert self.num_rows() == other.num_cols(), "dimensions problem"
		
		result = Matrix(self.num_cols(), other.num_rows())
		for i in range(result.num_cols()):
			for j in range(result.num_rows()):
				temp = 0
				for ii in range(self.num_rows()):
					temp += self[ii, i] *  other[j, ii]
				result[i, j] = temp
		return result.transpose()