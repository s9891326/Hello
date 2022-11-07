from hello_pattern.adapter_pattern.joke_teller import JokeTeller
from hello_pattern.adapter_pattern.show_interface import ShowInterface


class JokeTellerAdapter(ShowInterface):
    
    def __init__(self, joke_teller: JokeTeller):
        self.joke_teller = joke_teller
    
    def show(self):
        return self.joke_teller.tell()
