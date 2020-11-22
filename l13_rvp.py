import l13_stack as mystack
def rvp(s:str):
    """
    calculate expresnexton in postfix form
    >>> rvp("9 5 3 + 2 4 ^ - +")
    1.0
    >>> rvp("2 3 11 + 5 -*")
    18.0
    >>> rvp("3 11 + 5 -")
    9.0
    >>> rvp("3 11 5 + -")
    -13.0
    >>> rvp("3 11 +")
    14.0
    >>> rvp("3 -11 +")
    -8.0
    >>> rvp("-3-11--12-")
    20.0
    >>> rvp("5 2 3 ^ +")
    13.0
    >>> rvp("3 2 * 11 -")
    -5.0
    >>> rvp("2 1 12 3 /-+")
    -1.0
    >>> rvp("6 3 - 2 ^ 11 -")
    -2.0
    >>> rvp("6 3 2 ^ - 11 -")
    -14.0
    >>> rvp("162 2 1 + 4 ^ /")
    2.0
    >>> rvp("162 2 1 & 4 ^ /")
    >>> rvp("12/323/adhaksjdhasjdh")
    Traceback (most recent call last):
    IndexError: pop from empty list
    >>> rvp("")
    Traceback (most recent call last):
    IndexError: list index out of range
    """
    mystack.clear()
    number=""
    for i in range(len(s)):
        if s[i].isspace():
            continue
        elif s[i].isdigit():
            number+=s[i]
            if not(s[i+1].isdigit()): # last character cannot be digital
                mystack.push(float(number))
                number=""
        elif s[i]=="-":
            if  i<(len(s)-1) and s[i+1].isdigit():
                number=s[i]
            else:
                result=-mystack.pop()+mystack.pop()
                mystack.push(result)
        elif s[i]=="+":
            result=mystack.pop()+mystack.pop()
            mystack.push(result)
        elif s[i]=="*":
            result=mystack.pop()*mystack.pop()
            mystack.push(result)
        elif s[i]=="/":
            devisor=mystack.pop()
            result=mystack.pop()/devisor
            mystack.push(result)
        elif s[i]=="^":
            power=mystack.pop()
            result=mystack.pop()**power
            mystack.push(result)
        else:
            return
    return mystack.top()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
