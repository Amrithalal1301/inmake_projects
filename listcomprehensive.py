result=["python","django","flask","people"]
new=[]
for i in result:
    if 'p'in i:
        new.append(i)
print(new)
#new=[i for i in result if 'p' in i]
#print(new)