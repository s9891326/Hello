from __future__ import annotations

import enum

from hello_pattern.strategy_pattern.skill import Skill


class SkillEnum(enum.Enum):
    COLLIDE = "collide"
    WATER_BALL = "water_ball"


class Hero:
    def __init__(self, name: str, hp: int, mp: int, strength: int, wisdom: int, defense: int, skill: SkillEnum):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.strength = strength
        self.wisdom = wisdom
        self.defense = defense
        self.skill = skill

    def lose_hp(self, hp):
        self.hp -= hp
    
    def lose_mp(self, mp):
        self.mp -= mp

    def attack(self, target_hero: Hero):
        if self.skill == SkillEnum.COLLIDE:
            target_hero.lose_hp(self.strength - target_hero.defense)
        elif self.skill == SkillEnum.WATER_BALL:
            self.lose_mp(5)
            target_hero.lose_hp(self.wisdom * 2)
    
    def __str__(self):
        return f"{self.name}, hp: {self.hp}, skill: {self.skill.value}"


class Hero2:
    def __init__(self, name: str, hp: int, mp: int, strength: int, wisdom: int, defense: int, skill: Skill):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.strength = strength
        self.wisdom = wisdom
        self.defense = defense
        self.skill = skill
    
    def lose_hp(self, hp):
        self.hp -= hp
    
    def lose_mp(self, mp):
        self.mp -= mp
    
    def attack(self, target_hero: Hero2):
        self.skill.attack(self, target_hero)
    
    def __str__(self):
        return f"{self.name}, hp: {self.hp}, skill: {self.skill}"


