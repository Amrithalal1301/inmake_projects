def bmi_calculator(weight, height):
    return (weight) / (height)**2

w = float(input("enter your weight in Kg "))
h = float(input("enter your Height in m "))
bmi = bmi_calculator(w, h)
print("BMI = ", (bmi))
