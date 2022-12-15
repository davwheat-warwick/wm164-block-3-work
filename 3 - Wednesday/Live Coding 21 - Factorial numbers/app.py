ITERATION_COUNT = 200_000

currentOperator = "+"
currentVal = 0

for i in range(1, 2 * ITERATION_COUNT + 1, 2):
    if currentOperator == "-":
        currentVal -= 4 / i
        currentOperator = "+"
    else:
        currentVal += 4 / i
        currentOperator = "-"

print(currentVal)
