from liststack import MyStack

def delimeter_match(filename):

    stack = MyStack()
    with open(filename) as file:
        for (num, line) in enumerate(file):
            num += 1
            for s in line:
                if s in "<([{":
                    stack.push(s)
                elif s in ">)]}":
                    if stack.is_empty():
                        return "mismatch delimeter at line %d" % num
                    else:
                        s0 = stack.pop()
                        if s == '>' and s0 != '<' or s == ')' and s0 != '(' or s == ']' and s0 != '['  or s == '}' and s0 != '{':
                            return "mismatch delimeter at line %d" % num
        result = "all delimeter matches" if stack.is_empty() else 'delimeter in the end does not match'
        return result

def main():
    filename = "testFile.txt"
    check_result = delimeter_match(filename)
    print(check_result)
    
if __name__ == "__main__":
    main()