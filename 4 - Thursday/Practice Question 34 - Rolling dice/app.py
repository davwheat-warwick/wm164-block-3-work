import random


def roll(number_of_throws: int) -> list[int]:
    """Rolls a number of dice and returns the sorted results.

    Args:
        number_of_throws (int): The number of dice to roll

    Returns:
        list[int]: The results of the dice rolls
    """
    nums = [random.randint(1, 6) for _ in range(number_of_throws)]

    nums.sort()

    return nums


def main() -> None:
    number_of_throws = int(input("How many dice do you want to roll? "))

    if number_of_throws < 1:
        print("You must roll at least one die")
        return

    results = roll(number_of_throws)

    print(f"Your dice rolls were {results}")


if __name__ == "__main__":
    main()
