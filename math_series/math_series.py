def fibonacci(n):
    """
    takes one argument and return Fibonacci nth-term
    """
    if type(n) != int:
        return "wrong input,please Enter integer value"
    if n < 0:
        return "please enter positive nth-term"
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
       takes one argument and return lucas nth-term
       """
    if type(n) != int:
        return "wrong input,please Enter integer value"
    if n < 0:
        return "please enter positive nth-term"
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n1, n2=0, n3=1):
    """
       takes one mandatory argument and  two optional arguments, If one argument passed to the function
       it will return fibonacci function according to the first argument,
       if it takes the extra two arguments and they were 2 and 1 respectively, it will return lucas function
       according to the first argument
    """
    if n2 == 0 and n3 == 1:
        return fibonacci(n1)
    if n2 == 2 and n3 == 1:
        return lucas(n1)
