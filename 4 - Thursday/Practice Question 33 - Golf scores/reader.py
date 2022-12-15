import ast
import PlayerScorecard


def readScoreStrings() -> str:
    # Try to open the file scores.txt for reading
    try:
        with open("scores.txt", "r") as file:
            # If we can open the file, read the first line and return it
            return file.readline()
    # If we can't open the file, tell the user and exit the program
    except FileNotFoundError:
        print("Could not find file scores.txt")
        exit()


def scoresStringToDicts(score_strings: str) -> list[dict[str, str]]:
    return ast.literal_eval(score_strings)


def main() -> None:
    # Read score strings from a file
    score_strings = readScoreStrings()
    # Convert score strings to score dictionaries
    score_dicts = scoresStringToDicts(score_strings)
    # Convert score dictionaries to scorecards
    scorecards = [
        PlayerScorecard.PlayerScorecard.fromDict(score_dict)
        for score_dict in score_dicts
    ]
    # Print scorecards
    for scorecard in scorecards:
        print(scorecard)


if __name__ == "__main__":
    main()
