weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {round(bmi, 2)} — you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {round(bmi, 2)} — normal weight.")
elif bmi < 30:
    print(f"Your BMI is {round(bmi, 2)} — overweight.")
else:
    print(f"Your BMI is {round(bmi, 2)} — obese.")
  
