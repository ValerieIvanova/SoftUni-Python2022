class Controller:
    def __init__(self):
        self.players = []  # all the players (objects)
        self.supplies = []  # all the supplies (objects)

    def __find_player(self, player_name):
        for p in self.players:
            if player_name == p.name:
                return p

    def __find_supply(self, sustenance_type):
        if sustenance_type not in [s.__class__.__name__ for s in self.supplies]:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        for i in range(len(self.supplies) - 1, -1, -1):
            if type(self.supplies[i]).__name__ == sustenance_type:
                return self.supplies.pop(i)

    def add_player(self, *players):
        players_to_add = []
        for player in players:
            if player not in self.players:
                players_to_add.append(player.name)
                self.players.append(player)
        return f"Successfully added: {', '.join(players_to_add)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player(player_name)
        if not player:
            return
        if sustenance_type not in ['Food', 'Drink']:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        supply = self.__find_supply(sustenance_type)

        if player.stamina + supply.energy > 100:
            player.stamina = 100
        else:
            player.stamina += supply.energy

        return f"{player.name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_1 = self.__find_player(first_player_name)
        player_2 = self.__find_player(second_player_name)
        if player_1.stamina == 0 and player_2.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina.\n" \
                   f"Player {second_player_name} does not have enough stamina."
        if player_1.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        elif player_2.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        turns = [player_1, player_2] if player_1.stamina < player_2.stamina else [player_2, player_1]

        if turns[1].stamina - turns[0].stamina / 2 <= 0:
            turns[1].stamina = 0
            return f"Winner: {turns[0].name}"
        else:
            turns[1].stamina -= (turns[0].stamina / 2)

        if turns[0].stamina - turns[1].stamina / 2 <= 0:
            turns[0].stamina = 0
            return f"Winner: {turns[1].name}"
        else:
            turns[0].stamina -= (turns[1].stamina / 2)

        return f"Winner: {turns[0].name if turns[0].stamina > turns[1].stamina else turns[1].name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - player.age * 2 < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2
        for player in self.players:
            self.sustain(player.name, 'Food')
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        [result.append(str(player)) for player in self.players]
        [result.append(supply.details()) for supply in self.supplies]

        return '\n'.join(result)
