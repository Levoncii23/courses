# try:
#     x = [1, 4, 2, "hello", 12]
#     print(x.sort())
# except TypeError:
#     print("Что то пошло не так :(")
#
# print("Я поймал")
# def f(x, y):
#     try:
#         return x / y
#     except (TypeError, ZeroDivisionError) as e:
#         print(type(e))
#         print(e)
#         print(e.args)
#
#
# print(f(5, 0))
# print(f(5, []))

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero")
    else:
        print(f"resuilt is {result}")
    finally:
        print("finally")


print(divide(2, 10))
print(divide(2, 0))
print(divide(2, []))