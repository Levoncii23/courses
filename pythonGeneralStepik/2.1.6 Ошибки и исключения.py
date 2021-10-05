

def foo(x, y):
    print(x / y)


try:
    # foo(1, 0)
    # foo(2, 1)
    foo(2, [])
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")

