#we cannot add or remove elents from tuples when created

x=(12,5,"hi")
y=list(x)
print(y)
print(type(y))
y.insert(2,"hello")
print(y)
x=tuple(y)
print(x)
print(type(x))
