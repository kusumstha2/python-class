# def sum(a,b):
#    retutn a+b


# sum= lambda a,b:a+b
# print(sum(4,5))

# def func(n):
#     return lambda a:a*n

# #lambda a:a*2
# doubler=func(2)
# print(doubler(6))
# print(doubler(3))
# print(doubler(4))

def func(n):
    return lambda a:a*n
# lambda :a:a*3
tripler=func(3)
print(tripler(6))
print(tripler(5))
print(tripler(7))
# 3 times