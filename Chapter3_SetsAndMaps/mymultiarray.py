import sys
import os

sys.path.append(os.path.abspath("../1_Array"))

from myarray import Array


class MultiArray:

    def __init__(self, *dimensions):
        assert len(dimensions) > 1, "number of dimensions must be at least 2"
        self._dims = dimensions
        self._size = 1
        for s in self._dims:
            assert s > 0, "invalid size of dimensions"
            self._size *= s
        self._elements = Array(self._size)
        self._factors = Array(len(self._dims))

        temp = 1
        for i in range(len(self._dims)):
            self._factors[i] = temp
            temp *= dimensions[-i - 1]

    def num_dims(self):
        return len(self._dims)

    def length(self, dim):
        assert 1 <= dim <= len(self._dims), "invalid dimension"
        return self._dims[dim - 1]

    def __getitem__(self, idx_tuple):
        assert len(idx_tuple) == len(self._dims), "invalid number of index"
        idx = self._compute_idx(idx_tuple)
        assert idx is not None, "index out of range"
        return self._elements[idx]

    def __setitem__(self, idx_tuple, value):
        assert len(idx_tuple) == len(self._dims), "not enough index"
        idx = self._compute_idx(idx_tuple)
        assert idx is not None, "index out of range"
        self._elements[idx] = value
        return True

    def __str__(self):
        str_list = []
        for i in self._elements:
            str_list.append(i)
        return str(str_list)

    def clear(self, value):
        self._elements.clear(value)

    def _compute_idx(self, idx_tuple):
        index = 0
        for i in range(len(idx_tuple)):
            assert idx_tuple[i] >= 0, "invalid index"
            index += self._factors[i] * idx_tuple[-i - 1]
        if index > self._size or index < 0:
            return None
        return index

# Error 				
# Array can not have negative index
# for get to add return in _compute_idx
# typo  idx = self._compute_idx(idx_tuple, value) which should be idx = self._compute_idx(idx_tuple)




