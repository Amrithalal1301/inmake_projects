#Write Python code which accepts name of a product and in turn returns their respective prices. Make sure to use dictionaries to store products and their respective prices.
#The dictionary should include at least 5 elements.

x={
    "pen":15,
    "book":30,
    "pencil":10,
    "milk":25,
    "egg":5,
    "eraser":5
}
a = input("enter item = ")
print("item name : ",a ,"--------------price : Rs",x[a],"/per")
