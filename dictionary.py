x={
    "chair":500,
    "table":300,
    34:"python"
}
print(x[34])
print(len(x))
x["vegetables"]=120
print(x)
x.update({12:"django"})
print(x)
x.pop("table")
print(x)
print("------------------------")
for i in x:
    print(i)
print("------------------------")
for i in x.values():
    print(i)
print("------------------------")
for i in x.items():
    print(i)