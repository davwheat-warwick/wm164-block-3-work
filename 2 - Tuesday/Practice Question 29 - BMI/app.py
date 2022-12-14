def calculateBmi(weight: float, height: float) -> float:
    bmi = weight * 703 / (height**2)
    return bmi


def getBmiClassification(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Optimal"
    else:
        return "Overweight"


weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

bmi = calculateBmi(weight, height)

print("Your BMI is", bmi)

classification = getBmiClassification(bmi)

print("Your BMI classification is", classification)
