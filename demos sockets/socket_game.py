import json

FILENAME = 'socket_game.json'


class Player:

    def __init__(self, name=None):
        self._name = name
        self._position = None
        self._inventory = []
        self._game = None

    def __str__(self) -> str:
        return self._name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def inventory(self):
        return self._inventory

    def add_to_inventory(self, items):
        self._inventory.extend(items)

    def remove_from_inventory(self, item):
        self._inventory.remove(item)

    def describe_inventory(self) -> str:
        if self.inventory:
            return '\n  * '.join(('You have the following items in you inventory:',) +
                                 tuple(map(str, self.inventory)))
        else:
            return 'You have nothing in your inventory.'

    def play(self, game):
        self._game = game
        self._game.add_player(self)

        while True:
            print(self._game.locations[self.position].description)
            command_name = input(self._game.prompt)
            command = self._game.handle_command(self, command_name)
            new_position = command.move
            message = command.message
            if new_position:
                self.position = new_position
            if message:
                print(message)
            if command_name == 'quit':
                break


class InventoryItem:

    def __init__(self, name, description=None):
        self._name = name
        self._description = description

    def __str__(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @classmethod
    def parse_definition(cls, name, definition):
        description = definition['description']
        return cls(name, description=description)


class Command:

    def __init__(self, name, message=None, move=None):
        self._name = name
        self._message = message
        self._move = move

    def __str__(self) -> str:
        return self._name

    @property
    def message(self):
        return self._message

    @property
    def move(self):
        return self._move

    @classmethod
    def parse_definition(cls, name, definition):
        message = definition['message']
        move = definition['move']
        return cls(name, message=message, move=move)


class Location:

    def __init__(self, name, description=None, commands: dict = None):
        self._name = name
        self._description = description
        self._commands = commands

    def __str__(self) -> str:
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def commands(self) -> dict:
        return self._commands

    def add_commands(self, commands: dict):
        self._commands.update(commands)

    @classmethod
    def parse_definition(cls, name, definition):
        description = definition['description']
        commands = dict()
        for command_name, command_definition in definition['commands'].items():
            commands[command_name] = Command.parse_definition(command_name, command_definition)
        return cls(name, description, commands)


class CommandHandler:
    STANDARD_COMMANDS = {
        'help': 'You\'re on your own for now. No help available.',
        'commands': '',  # describe_inventory,
        'players': 'This is a single player game. You are the only player.',
        'inventory': '',  # describe_inventory,
        'quit': 'Bye.'
    }

    def __init__(self, game):
        self._game = game

    def handle_command(self, player, command_name):
        commands = self._game.locations[player.position].commands
        command = commands.get(command_name)
        if command:
            return command
        else:
            message = CommandHandler.STANDARD_COMMANDS.get(command_name)
            if command_name == 'commands':
                message = self.describe_available_commands(player)
            elif command_name == 'inventory':
                message = player.describe_inventory()
            if message is None:
                message = 'That is not a valid command. Try \'help\'.'
            return Command(command_name, message=message)

    def available_commands(self, player) -> tuple:
        commands = self._game.locations[player.position].commands
        return tuple(CommandHandler.STANDARD_COMMANDS.keys()) + tuple(map(str, commands))

    def describe_available_commands(self, player) -> str:
        return '\n  * '.join(('The following commands are available',) +
                             self.available_commands(player))


class Game:

    def __init__(self, name, prompt='> ', locations=None, new_player=None):
        self._name = name
        self._prompt = prompt
        self._locations = dict()
        self._new_player = {'message': 'Welcome.',
                            'start_position': 'start',
                            'inventory_items': []}

        if locations:
            self.add_locations(locations)
        if new_player:
            self._new_player = dict(new_player)

        self._command_handler = CommandHandler(self)
        self._players = []

    @property
    def prompt(self) -> str:
        return self._prompt

    @prompt.setter
    def prompt(self, prompt):
        self._prompt = prompt

    @property
    def locations(self) -> dict:
        return self._locations

    def add_locations(self, locations: dict):
        self._locations.update(locations)

    @property
    def players(self):
        return self._players

    def add_player(self, player):
        self._players.append(player)
        player.position = self._new_player['start_position']
        player.add_to_inventory(self._new_player['inventory_items'])

    @property
    def command_handler(self):
        return self._command_handler

    def handle_command(self, player, command_name):
        return self._command_handler.handle_command(player, command_name)

    @staticmethod
    def load_game_definition(definition_file=FILENAME):
        try:
            with open(definition_file) as f:
                return json.load(f)
        except IOError:
            return None

    @classmethod
    def parse_game_definition(cls, name, definition):
        prompt = definition['prompt']
        locations = dict()
        for location_name, location_definition in definition['locations'].items():
            locations[location_name] = Location.parse_definition(location_name, location_definition)
        new_player = definition['new_player']
        return cls(name, prompt, locations, new_player)

    @classmethod
    def load_game(cls, definition_file=FILENAME):
        definition = cls.load_game_definition(definition_file)
        name = definition['name']
        return cls.parse_game_definition(name, definition)


if __name__ == '__main__':
    the_game = Game.load_game()
    single_player = Player('Peter')
    single_player.play(the_game)
