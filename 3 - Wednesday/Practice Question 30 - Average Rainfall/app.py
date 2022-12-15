numberOfYears = int(input("Enter the number of years: "))

totalRainfall = 0

for year in numberOfYears:
    for month in range(1, 13):
        print("Month", month, "of", year)
        totalRainfall += float(
            input("Enter the total rainfall for the month (inches):")
        )

totalMonths = numberOfYears * 12
averageRainfall = totalRainfall / totalMonths

print("The average rainfall for", totalMonths, "months is", averageRainfall)
print("The total rainfall is", totalRainfall, "inches")
