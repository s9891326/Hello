from abc import ABC, abstractmethod


class Skill(ABC):
    @abstractmethod
    def attack(self, attacking_hero, attacked_hero):
        pass


class Colliding(Skill):
    def attack(self, attacking_hero, attacked_hero):
        attacked_hero.lose_hp(attacking_hero.strength - attacked_hero.defense)


class WaterBall(Skill):
    def attack(self, attacking_hero, attacked_hero):
        attacking_hero.lose_mp(5)
        attacked_hero.lose_hp(attacking_hero.wisdom * 2)
