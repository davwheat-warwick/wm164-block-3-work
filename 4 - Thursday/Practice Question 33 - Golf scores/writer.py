import PlayerScorecard


def main() -> None:
    player_count = int(input("How many players are there? "))

    player_scorecards = []

    for _ in range(player_count):
        player_name = input("What is the name of the player? ")
        score = int(input("What is their score? "))

        player_scorecards.append(PlayerScorecard.PlayerScorecard(player_name, score))

    dict_scorecards = [scorecard.toDict() for scorecard in player_scorecards]

    with open("scores.txt", "w") as file:
        file.write(str(dict_scorecards))


if __name__ == "__main__":
    main()
