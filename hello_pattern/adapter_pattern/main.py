from hello_pattern.adapter_pattern.joke_teller import JokeTeller
from hello_pattern.adapter_pattern.joke_teller_adapter import JokeTellerAdapter
from hello_pattern.adapter_pattern.piano_player import PianoPlayer
from hello_pattern.adapter_pattern.piano_player_adapter import PianoPlayerAdapter


class Program:
    
    # first design
    # 才藝表演 主持人覺得需要知道每位表演者的表演方式(play、tell) 有點麻煩
    def run(self):
        result = []
        result.append(PianoPlayer().play())
        result.append(JokeTeller().tell())
        return result
    
    # use adapter pattern to fix 主持人需要知道每位表演者的表演方式(play、tell)
    def run2(self):
        prepare_performers = self.get_preparePerformers()
        
        result = []
        for performer in prepare_performers:
            result.append(performer.show())
        
        return result
    
    def get_preparePerformers(self):
        preparePerformers = [PianoPlayerAdapter(PianoPlayer()), JokeTellerAdapter(JokeTeller())]
        return preparePerformers


if __name__ == '__main__':
    program = Program()
    
    # 1
    print(program.run())
    
    # 2
    print(f"use adapter pattern\n{program.run2()}")
