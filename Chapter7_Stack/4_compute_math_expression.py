from liststack import MyStack

def infix2postfix(expression):
    precedence = {'+': 0,  '-': 0, '*' : 1, '/': 1, '^': 2}
    
    result = list()
    stack = MyStack()
    
    for ch in expression:
        # Check if ch is a number
        if ch.isnumeric():
            result.append(ch)
            continue
        
        # Check if ch is a space
        if ch == ' ':
            continue
            
        # Check if ch is an operator
        if ch in precedence:
            if stack.is_empty() or stack.peek() == '(' or (precedence[ch] > precedence[stack.peek()]) or (ch == '^' and stack.peek() == '^'):
                stack.push(ch)
            else:
                while not stack.is_empty() and (stack.peek() == '(' or precedence[ch] <= precedence[stack.peek()]):
                    if stack.peek() == '(':
                        break
                    result.append(stack.pop())
                stack.push(ch)
                    
        elif ch == '(':
            stack.push(ch)
            continue
        
        elif ch == ')':
            while not stack.is_empty() and stack.peek() != '(':
                result.append(stack.pop())
                
                if stack.is_empty():
                    raise ValueError("invalid expression")
                
                if stack.peek() == '(':
                    stack.pop()
                    break
        else:
            raise ValueError("invalid character: %s" % ch)
            
    while not stack.is_empty():
        result.append(stack.pop())

    return ''.join(result)


def postfix2value(expression):
    stack = MyStack()

    for ch in expression:
        if not ch.isnumeric() and ch not in "+-*/^":
            raise ValueError('invalid character: %s' % ch)

        if ch.isnumeric():
            stack.push(ch)

        else:
            if stack.is_empty():
                raise ValueError("invalid expression")
            op2 = float(stack.pop())

            if stack.is_empty():
                raise ValueError("invalid expression")
            op1 = float(stack.pop())

            result = None
            if ch == '+':
                result = op1 + op2

            if ch == '-':
                result = op1 - op2

            if ch == '*':
                result = op1 * op2

            if ch == '/':
                result = op1 / op2

            if ch == '^':
                result = op2 ** op1

            stack.push(result)

    result = stack.pop()
    if stack.is_empty():
        return result
    else:
        raise ValueError("invalid expression")


def main():
    e1 = "3+5*4*(5+3*7)+(4*5/9)-(1+1)*2^2^2"
    
    print("e1: %s" % e1)
    postfix_e1 = infix2postfix(e1)
    print("e1 to postfix: %s" % postfix_e1)
    print()
    
    print('compute the result: ')
    result = postfix2value(postfix_e1)
    print('%.2f' % result)
   
    
if __name__ == "__main__":
    main()
