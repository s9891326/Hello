from hello_pattern.strategy_pattern.hero import Hero, SkillEnum, Hero2
from hello_pattern.strategy_pattern.skill import Colliding, WaterBall


class Battle:
    def __init__(self, hero1: Hero, hero2: Hero):
        self.hero1 = hero1
        self.hero2 = hero2
    
    def start(self):
        _attack_hero, _be_attacked_hero = self.hero1, self.hero2
        
        while _attack_hero.hp >= 0 and _be_attacked_hero.hp >= 0:
            _attack_hero.attack(_be_attacked_hero)
            _attack_hero, _be_attacked_hero = self.hero2, self.hero1
            print(self.hero1)
            print(self.hero2)
        
        winner = self.hero1 if self.hero1.hp >= 0 else self.hero2
        print(f"winner: {winner.name}, {winner}")


class Battle2:
    def __init__(self, hero1: Hero2, hero2: Hero2):
        self.hero1 = hero1
        self.hero2 = hero2
    
    def start(self):
        _attack_hero, _be_attacked_hero = self.hero1, self.hero2
        
        while _attack_hero.hp >= 0 and _be_attacked_hero.hp >= 0:
            _attack_hero.attack(_be_attacked_hero)
            _attack_hero, _be_attacked_hero = self.hero2, self.hero1
            print(self.hero1)
            print(self.hero2)
        
        winner = self.hero1 if self.hero1.hp >= 0 else self.hero2
        print(f"winner: {winner.name}, {winner}")


if __name__ == '__main__':
    # h = Hero("eddy")
    # eddy = Hero("eddy", hp=10, mp=2, strength=30, wisdom=4, defense=5, skill=SkillEnum.COLLIDE)
    # eddy2 = Hero("eddy2", hp=100, mp=2, strength=3, wisdom=50, defense=5, skill=SkillEnum.WATER_BALL)
    # Battle(eddy, eddy2).start()

    eddy = Hero2("eddy", hp=10, mp=2, strength=30, wisdom=4, defense=5, skill=Colliding())
    eddy2 = Hero2("eddy2", hp=100, mp=2, strength=3, wisdom=50, defense=5, skill=WaterBall())
    Battle2(eddy, eddy2).start()
    

