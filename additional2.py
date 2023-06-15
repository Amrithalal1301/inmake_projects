#additional challenge 2
#simple interest=(p*n*r/100)

def simple_interest(P,R,T):
    return (P*R*T)/100
a= float(input("enter principal amount,P = "))
b=float(input("enter the rate of interest,R = "))
c= float(input("enter the time period ,T = "))
si=simple_interest(a,b,c)
print(si)