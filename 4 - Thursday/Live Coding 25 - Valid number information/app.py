INPUT_NUMBERS = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]


def filter_invalid_numbers(numbers: list[int]) -> list[int]:
    """Filters out the invalid numbers from the given list.

    Args:
        numbers (list[int]): The list of numbers to filter

    Returns:
        list[int]: The list of valid numbers
    """
    # Make a list to store the valid numbers
    valid_numbers = []

    # For each number
    for number in numbers:
        # If the number is valid
        if number >= 0 and number <= 100:
            # Add it to the list of valid numbers
            valid_numbers.append(number)

    # Return the list of valid numbers
    return valid_numbers


def get_average(nums: list[int]) -> float:
    """Gets the average of the given numbers.

    Args:
        nums (list[int]): The numbers to get the average of

    Returns:
        float: The average of the numbers
    """
    return sum(nums) / len(nums)


def main() -> None:
    valid_numbers = filter_invalid_numbers(INPUT_NUMBERS)
    average = get_average(valid_numbers)
    print(f"The average of the valid numbers is {average}")


if __name__ == "__main__":
    main()
