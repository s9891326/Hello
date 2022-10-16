from hello_pattern.adapter_pattern.piano_player import PianoPlayer
from hello_pattern.adapter_pattern.show_interface import ShowInterface


class PianoPlayerAdapter(ShowInterface):
    
    def __init__(self, piano_player: PianoPlayer):
        self.piano_player = piano_player
    
    def show(self):
        return self.piano_player.play()
