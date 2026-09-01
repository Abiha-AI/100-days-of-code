# Day: 3 Practicing Python with a Basic BMI Calculator
# What actullay BMI is a measuring calculator Body Mass Index
# What is BMI?
#It is a simple calculation using your height and weight.
#It estimates if your body weight is in a healthy range.
#Doctors use it as a basic screening tool for health risks

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
