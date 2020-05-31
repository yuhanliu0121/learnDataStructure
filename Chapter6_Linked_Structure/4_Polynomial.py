from copy import deepcopy

class Polynomial(object):
    
    def __init__(self, degree=None, coefficient=0):
        if degree is None:
            self._poly_head = None
        else:
            self._poly_head = _PolyTermNode(degree, coefficient)
        self._poly_tail = self._poly_head
 
    def degree(self):
        
        if self._poly_head is None:
            return -1
        
        current_node = self._poly_head
        degree_temp = current_node.degree
        
        while current_node is not None:
            if current_node.degree > degree_temp:
                degree_temp = current_node.degree
            current_node = current_node.next
                
        return degree_temp
        
    def __getitem__(self, degree):
        assert degree <= self.degree(), "degree out of bound"
        
        current_node = self._poly_head
        while current_node is not None and current_node.degree > degree:
            current_node = current_node.next
            
        if current_node is not None and current_node.degree == degree:
            return current_node.coefficient
        else:
            return 0
    
    def __str__(self):
        if self._poly_head is None:
            return 'empty polynomial'
        
        string_list = []
        current_node = self._poly_head
        
        while current_node is not None:
            temp_str = ''
            coefficient = current_node.coefficient
            degree = current_node.degree
            
            if coefficient != 0:
                sign = '+' if coefficient > 0 else ''
                
                if abs(coefficient) == 1:
                    if degree == 0:
                        temp_str = '+1' if coefficient > 0 else '-1'
                    elif degree == 1:
                        temp_str = '+x' if coefficient > 0 else '-x'
                    else:
                        temp_str = ('+' if coefficient > 0 else '-') + 'x^' + str(degree)
                else:
                    if degree == 0:
                        temp_str = sign + str(coefficient)
                    elif degree == 1:
                        temp_str = sign + str(coefficient) + 'x'
                    else:
                        temp_str = sign + str(current_node.coefficient) + 'x^' + str(current_node.degree)
        
            string_list.append(temp_str)
            current_node = current_node.next
        
        if string_list[0][0] == '+':
            string_list[0] = string_list[0][1:]
        
        return ''.join(string_list)
        
    def evaluate(self, scalar):
        assert self._poly_head is not None, "cannot evaluate empty polynomial"
        
        result = 0
        current_node = self._poly_head
        
        while current_node is not None:
            result += current_node.coefficient * scalar ** current_node.degree
            current_node = current_node.next
            
        return result
        
    def _append_term(self, degree, coefficient):
        if coefficient != 0.0:
            new_node = _PolyTermNode(degree, coefficient)
            if self._poly_head is None:
                self._poly_head = new_node
            else:
                self._poly_tail.next = new_node
            self._poly_tail = new_node
                
    def __add__(self, rhs_poly):
        if self._poly_head is None or rhs_poly._poly_head is None:
            if self._poly_head is None and rhs_poly is not None:
                return rhs_poly
            else: 
                return self
        
        current_node_self = self._poly_head
        current_node_rhs = rhs_poly._poly_head
        
        new_poly = Polynomial()
        
        if current_node_self.degree > current_node_rhs.degree:
            new_poly._append_term(current_node_self.degree, current_node_self.coefficient)
            current_node_self = current_node_self.next
        else:
            new_poly._append_term(current_node_rhs.degree, current_node_rhs.coefficient)
            current_node_rhs = current_node_rhs.next
            
        while current_node_self is not None and current_node_rhs is not None:
            if current_node_self.degree == current_node_rhs.degree:
                degree = current_node_self.degree
                coefficient = current_node_self.coefficient + current_node_rhs.coefficient
                new_poly._append_term(degree, coefficient)
                current_node_self = current_node_self.next
                current_node_rhs = current_node_rhs.next
                
            elif current_node_self.degree > current_node_rhs.degree:
                new_poly._append_term(current_node_self.degree, current_node_self.coefficient)
                current_node_self = current_node_self.next
                
            elif current_node_self.degree < current_node_rhs.degree:
                new_poly._append_term(current_node_rhs.degree, current_node_rhs.coefficient)
                current_node_rhs = current_node_rhs.next
            
        if current_node_self is not None:
            while current_node_self is not None:
                new_poly._append_term(current_node_self.degree, current_node_self.coefficient)
                current_node_self = current_node_self.next
        
        if current_node_rhs is not None:
            while current_node_rhs is not None:
                new_poly._append_term(current_node_rhs.degree, current_node_rhs.coefficient)
                current_node_rhs = current_node_rhs.next
                
        return new_poly
        
    def __sub__(self, rhs_poly):
        rhs_poly_copy = deepcopy(rhs_poly)
        current_node = rhs_poly_copy._poly_head
        
        while current_node is not None:
            current_node.coefficient = -current_node.coefficient
            current_node = current_node.next
        
        return self + rhs_poly_copy
        
    def __mul__(self, rhs_poly):
        current_node_self = self._poly_head
        new_poly = rhs_poly._term_multiply(current_node_self)
        current_node_self = current_node_self.next
        
        while current_node_self is not None:
            new_poly += rhs_poly._term_multiply(current_node_self)
            current_node_self = current_node_self.next
        
        return new_poly

    def _term_multiply(self, term):
        
        new_poly = deepcopy(self)
        current_node = new_poly._poly_head
        
        while current_node is not None:
            current_node.coefficient *= term.coefficient
            current_node.degree += term.degree
            current_node = current_node.next
        
        return new_poly


class _PolyTermNode(object):
    
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None
        
        
def main():
    poly_1 = Polynomial(4,3)
    poly_2 = Polynomial(3,2)
    poly_3 = Polynomial(2,1)
    poly_4 = Polynomial(1,1)
    poly_5 = Polynomial(0,1)

    poly1 = poly_1 + poly_2 + poly_3 + poly_4 + poly_5

    poly_1 = Polynomial(-2,3)
    poly_2 = Polynomial(3,-2)
    poly_3 = Polynomial(-2,1)
    poly_4 = Polynomial(1,-1)
    poly_5 = Polynomial(0,0)

    poly2 = poly_1 + poly_2 + poly_3 + poly_4 + poly_5
     
    print("poly1:")
    print(poly1)
    print()
    
    print("poly2:")
    print(poly2)
    print()

    print("poly1 + poly2:")
    print(poly1 + poly2)
    print()
    
    print("poly1 - poly2:")
    print(poly1 - poly2)
    print()
    
    print("poly1 * poly2:")
    print(poly2 * poly1)
    print()
    
    print("poly1.evaluate(0):")
    print(poly1.evaluate(0))
    print()
    
    print("poly1.evaluate(-1)")
    print(poly1.evaluate(-1))
    print()
    
    print("poly1.evaluate(2):")
    print(poly1.evaluate(2))
    print()


if __name__ == "__main__":
    main()