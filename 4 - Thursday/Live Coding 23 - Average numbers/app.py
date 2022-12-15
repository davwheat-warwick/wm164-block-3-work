FILE_NAME = "test.txt"


def read_lines() -> list[str] | None:
    """Reads the lines from a file and returns them.

    Returns:
        list[str] | None: The lines from the file, or None if the file
            does not exist
    """
    try:
        with open(FILE_NAME, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Could not find file {FILE_NAME}")
        return None


def convertLinesToNums(lines: list[str]) -> list[float]:
    # Make a list of the numbers in the given lines
    nums = []

    # For each line
    for line in lines:
        # Try to convert it to a number
        try:
            nums.append(float(line))
        # If it isn't a number
        except ValueError:
            pass

    # Return the list of numbers
    return nums


def calculateAverage(nums: list[float]) -> float:
    return sum(nums) / len(nums)


def main() -> None:
    lines = read_lines()

    if lines is None:
        return

    nums = convertLinesToNums(lines)
    average = calculateAverage(nums)

    print(f"The average of the numbers is {average}")


if __name__ == "__main__":
    main()
