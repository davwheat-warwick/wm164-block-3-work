class PlayerScorecard:
    def __init__(self, player_name: str, score: int) -> None:
        self.player_name = player_name
        self.score = score

    def toDict(self) -> dict[str, str | int]:
        return {"player_name": self.player_name, "score": self.score}

    def __str__(self) -> str:
        return f"{self.player_name}: {self.score}"

    @staticmethod
    def fromDict(dict: dict[str, str | int]):
        name = dict["player_name"]
        score = dict["score"]

        if not isinstance(name, str):
            raise TypeError("player_name must be a string")
        if not isinstance(score, int):
            raise TypeError("score must be an int")

        return PlayerScorecard(name, score)
