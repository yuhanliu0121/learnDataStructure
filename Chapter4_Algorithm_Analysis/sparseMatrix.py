class SparseMatrix:
	
	def __init__(self, numRows, numCols):
		assert numRows >= 0 and numCols >= 0, "matrix dimension must be > 0"
		self._numRows = numRows
		self._numCols = numCols
		self._elements = list()
		
	def numRows(self):
		return self._numRows

	def numCols(self):
		return self._numCols
		
	def __str__(self):
		matrix = ''
		for i in range(self._numRows):
			matrix += '\n'
			for j in range(self._numCols):
				pos = self._findPosition(i, j)
				if pos == None:
					matrix +='0\t'
				else:
					matrix += (str(self._elements[pos].val) + '\t')
		return matrix
		
	def __getitem__(self, idx):
		row = idx[0]
		col = idx[1]
		assert row <= self._numRows - 1 and col <= self._numCols - 1, "index out of bound"
		pos = self._findPosition(row, col)
		if pos == None:
			return 0
		return self._elements[pos].val
	
	def __setitem__(self, idx, val):
		row = idx[0]
		col = idx[1]
		assert row <= self._numRows and col <= self._numCols, "index out of bound"
		pos = self._findPosition(row, col)
		if val == 0:
			if pos != None:
				self._elements.pop(pos)
		else:
			if pos == None:
				self._elements.append(_MatrixElement(row, col, val))
			else:
				self._elements[pos].val = val
		
	def _findPosition(self, row, col):
		for i in range(len(self._elements)):
			if (self._elements[i].row == row) and (self._elements[i].col == col):
				return i
		return None
		
	def __add__(self, anotherMatrix):
		assert self._numRows == anotherMatrix._numRows and self._numCols == anotherMatrix._numCols, "matrix dimension not match"
		
		newMatrix = SparseMatrix(self._numRows, self._numCols)
		for i in range(len(self._elements)):
			newMatrix._elements.append(self._elements[i])
			
		for i in range(len(anotherMatrix._elements)):
			row = anotherMatrix._elements[i].row
			col = anotherMatrix._elements[i].col
			val = anotherMatrix._elements[i].val
			pos = newMatrix._findPosition(row, col)
			if pos == None:
				newMatrix[row, col] = val
			else:
				newMatrix[row, col] += val
		return newMatrix
	
	def __sub__(self, anotherMatrix):
		assert self._numRows == anotherMatrix._numRows and self._numCols == anotherMatrix._numCols, "matrix dimension not match"
		
		newMatrix = SparseMatrix(self._numRows, self._numCols)
		for i in range(len(self._elements)):
			newMatrix._elements.append(self._elements[i])
			
		for i in range(len(anotherMatrix._elements)):
			row = anotherMatrix._elements[i].row
			col = anotherMatrix._elements[i].col
			val = anotherMatrix._elements[i].val
			pos = newMatrix._findPosition(row, col)
			if pos == None:
				newMatrix[row, col] = -val
			else:
				newMatrix[row, col] -= val
		return newMatrix
		
	def scaleBy(self, scalar):
		for element in self._elements:
			element.val*= scalar
	
	def __mul__(self, anotherMatrix):
		pass
	
class _MatrixElement:
	def __init__(self, row, col, val):
		self.row = row
		self.col = col
		self.val = val


m1 = SparseMatrix(4,4)
m1[0,0] = 4
m1[2,2] = 5

m2 = SparseMatrix(4,4)
m2[0,0] = 4
m2[2,3] = 6

print("m1: ")
print(m1)

print("m1 scaleBy 3: ")
m1.scaleBy(3)
print(m1)

print("m2: ")
print(m2)	


print("m1 - m2: ")
print(m1-m2)

print("m1 + m2: ")
print(m1+m2)