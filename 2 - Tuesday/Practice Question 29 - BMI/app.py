def calculateBmi(weight: float, height: float) -> float:
    bmi = weight * 703 / (height**2)
    return bmi


weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

bmi = calculateBmi(weight, height)

print("Your BMI is", bmi)
