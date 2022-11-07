from hello_pattern.command_pattern.chef import Chef
from hello_pattern.command_pattern.command import Command


class CookSirloinSteakCommand(Command):
    def __init__(self, chef: Chef):
        self.chef = chef

    def execute(self):
        return self.chef.cook_sirloin_steak()
