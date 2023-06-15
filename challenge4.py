
#challenge 4
#Write a function which would divide two numbers, design the function in a manner that it handles the divide by zero exception

def division(a,b):
    try:
        print(a/b)
    except:
        print("there is a division error")

a=int(input("enter dividend "))
b=int(input("enter divisor "))
q=division(a,b)
