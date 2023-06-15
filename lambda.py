 #lambda   arguments:expr

x = lambda a,b:a+b
print(x(2,3))

y = lambda a :a+30
print(y(7))

z = lambda a,b,c :a+30+b+c
print(z(7,8,5))

def func(a):
    return lambda a:a+n
print(func(2))