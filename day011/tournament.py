"""
Task:
Implement a tournament management system using object-oriented programming
and algorithms.

Requirements:
- Create `Player`, `Match`, and `Tournament` classes.
- A Player has a name and a unique ID.
- A Match contains two players and their scores.
- A Tournament manages players and matches.
- Players can participate in multiple matches.
- A player cannot play against themselves.
- A match must have a winner.
- The tournament can determine a player's total points.
- The tournament can determine the player with the most points.
- The tournament can return a player's match history.
"""


class Player:
    def __init__(self, player_id: str, name: str) -> None:
        if not player_id or not name:
            raise ValueError("Player ID or name can not be empty.")

        self.player_id = player_id
        self.name = name

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Player):
            return NotImplemented

        return self.player_id == other.player_id


class Match:
    def __init__(
        self, player1: Player, player2: Player, score1: int, score2: int
    ) -> None:
        if player1 == player2:
            raise ValueError("player1 and player2 must be different players.")

        if score1 < 0 or score2 < 0:
            raise ValueError("Scores cannot be negative.")

        if score1 == score2:
            raise ValueError("The match cannot end in a draw.")

        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def winner(self) -> Player:
        if self.score1 > self.score2:
            return self.player1

        return self.player2


class Tournament:
    def __init__(self) -> None:
        self.players: list[Player] = []
        self.matches: list[Match] = []

    def add_player(self, player: Player) -> None:
        for existing_player in self.players:
            if existing_player == player:
                raise ValueError("Player already added.")

        self.players.append(player)

    def add_match(self, match: Match) -> None:
        if match.player1 not in self.players or match.player2 not in self.players:
            raise ValueError("Unknown player.")

        self.matches.append(match)

    def player_points(self, player_id: str) -> int:
        total = 0

        for match in self.matches:
            if match.winner().player_id == player_id:
                total += 3

        return total

    def top_player(self) -> Player | None:
        if not self.players:
            return None

        return max(
            self.players, key=lambda player: self.player_points(player.player_id)
        )

    def match_history(self, player_id: str) -> list[Match]:
        result = []
        player = None

        for existing_player in self.players:
            if existing_player.player_id == player_id:
                player = existing_player
                break

        if player is None:
            raise ValueError("Unknown player.")

        for match in self.matches:
            if match.player1 == player or match.player2 == player:
                result.append(match)

        return result
