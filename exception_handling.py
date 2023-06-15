
#EXCEPTION HANDLING
try:
    a=int(input("enter 1st "))
    b=int(input("enter 2nd "))
    print(a/b)
except:
    print("there is a division error")
print("....------------------------------------------....")
try:
    a=[10,20,30,40,50]
    print(a[5])
except:
    print("there is a index error")

finally:
    print("finished")