from myarray import Array


class _MatrixElementNode(object):
    def __init__(self, col, val):
        self.col = col
        self.val = val
        self.next = None


class SparseMatrix(object):
    def __init__(self, num_rows, num_cols):
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._list_of_array = Array(num_rows)

    def num_rows(self):
        return self._num_rows

    def num_cols(self):
        return self._num_cols

    def __getitem__(self, idx):
        assert len(idx) == 2, "expected 2 index but get " + str(len(idx))

        row = idx[0]
        col = idx[1]

        assert row < self.num_rows() and col < self.num_cols(), "index out of range"

        current_node = self._list_of_array[row]

        while current_node is not None and current_node.col < col:
            current_node = current_node.next

        if current_node is not None and current_node.col == col:
            return current_node.val
        return 0

    def __setitem__(self, idx, val):
        assert len(idx) == 2, "expected 2 index but get " + str(len(idx))

        row = idx[0]
        col = idx[1]

        assert row < self.num_rows() and col < self.num_cols(), "index out of range"

        pre_node = None
        current_node = self._list_of_array[row]

        while current_node is not None and current_node.col < col:
            pre_node = current_node
            current_node = current_node.next

        if val == 0.0:
            if current_node is not None:
                if current_node == self._list_of_array[row]:
                    self._list_of_array[row] = current_node.next
                else:
                    pre_node.next = current_node.next
        else:
            new_node = _MatrixElementNode(col, val)

            if current_node is not None:
                if current_node == self._list_of_array[row]:
                    if current_node.col == col:
                        current_node.val = val
                    else:
                        self._list_of_array[row] = new_node
                        new_node.next = current_node

                elif current_node.col == col:
                    current_node.val = val

                else:
                    pre_node.next = new_node
                    new_node.next = current_node
            else:
                if current_node == self._list_of_array[row]:
                    self._list_of_array[row] = new_node
                else:
                    pre_node.next = new_node

    def show(self):
        for row in range(self.num_rows()):
            print()
            string_list = [0] * self.num_cols()
            current_node = self._list_of_array[row]

            while current_node is not None:
                string_list[current_node.col] = current_node.val
                current_node = current_node.next

            for s in string_list:
                print(s, end='\t')
        print()
        print()

    def scale_by(self, scalar):
        new_matrix = self.copy()
        
        for row in range(new_matrix.num_rows()):
            current_node = new_matrix._list_of_array[row]
            while current_node is not None:
                col = current_node.col
                new_matrix[row, col] = new_matrix[row, col] * scalar
                current_node = current_node.next
        return new_matrix

    def transpose(self):
        pass

    def copy(self):
        new_matrix = SparseMatrix(self.num_rows(), self.num_cols())

        for row in range(new_matrix.num_rows()):
            current_node_self = self._list_of_array[row]
            
            if current_node_self is not None:
                new_matrix._list_of_array[row] = _MatrixElementNode(current_node_self.col, current_node_self.val)
                current_node_new = new_matrix._list_of_array[row]
                current_node_self = current_node_self.next
            
            while current_node_self is not None:
                current_node_new.next = _MatrixElementNode(current_node_self.col, current_node_self.val)

                current_node_new = current_node_new.next
                current_node_self = current_node_self.next

        return new_matrix

    def __add__(self, other):
        assert self.num_rows() == other.num_rows() and self.num_cols() == other.num_cols(), "size of two matrix does not match"

        new_matrix = self.copy()

        for row in range(new_matrix.num_rows()):
            current_node2 = other._list_of_array[row]

            while current_node2 is not None:
                col = current_node2.col
                new_matrix[row, col] = new_matrix[row, col] + other[row, col]

                current_node2 = current_node2.next

        return new_matrix

    def __sub__(self, other):
        assert self.num_rows() == other.num_rows() and self.num_cols() == other.num_cols(), "size of two matrix does not match"

        other_copy = other.copy()
        
        for row in range(other_copy.num_rows()):
            current_node = other_copy._list_of_array[row]
            while current_node is not None:
                current_node.val = -current_node.val
                current_node = current_node.next

        return self + other_copy


def main():
    sm1 = SparseMatrix(5, 5)
    sm2 = SparseMatrix(5, 5)

    print("sm1: ")
    sm1.show()

    sm1[0, 0] = 0
    sm1[0, 0] = 10
    sm1[0, 0] = 0
    sm1[0, 0] = 8

    sm1[0, 1] = 5
    sm1[0, 1] = 0
    sm1[0, 1] = 5
    
    sm1[2,2] = 56

    sm1[0,4] = 332
    sm1[0, 2] = 4
    sm1[4, 4] = 100
    
    
    sm2[2,2] = -56
    sm2[0, 4] = -332
    sm2[0, 0] = -8
    sm2[0, 2] = 12

    print("assigen value to partial elements of sm1:")
    sm1.show()

    print("assigen value to partial elements of sm2:")
    sm2.show()

    print("sm1 + sm2: ")
    sm3 = sm1 + sm2
    sm3.show()
    
    print("sm1 - sm2: ")
    sm3 = sm1 - sm2
    sm3.show()
    
    print("sm1 scale by 0: ")
    sm3 = sm1.scale_by(0)
    sm3.show()
    
    print("sm1 scale by 2: ")
    sm3 = sm1.scale_by(2)
    sm3.show()
    
    


if __name__ == "__main__":
    main()
