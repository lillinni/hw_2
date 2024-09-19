# hometask - 4

from random import randint, choice

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if type(hero) == Berserk and self.defence != hero.ability:
                    blocked = choice([5, 10])
                    hero.blocked_damage = blocked
                    hero.health -= (self.damage - blocked)
                else:
                    hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def apply_super_power(self, boss, heroes):
        pass

    def attack(self, boss):
        boss.health -= self.damage


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_power(self, boss, heroes):
        coefficient = randint(2, 5)
        boss.health -= self.damage * coefficient
        print(f'Warrior {self.name} hit critically {self.damage * coefficient}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BOOST')

    def apply_super_power(self, boss, heroes):
        boost_amount = randint(1, 5)
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.damage += boost_amount
        print(f'Magic {self.name} boosted heroes damage by {boost_amount}')


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BLOCK_AND_REVERT')
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted {self.__blocked_damage} damage.')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, 'HEAL')
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points
        print(f'Medic {self.name} healed the team for {self.__heal_points} health')


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'RESURRECTION')

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health == 0:  
                hero.health = self.health
                self.health = 0
                print(f'Witcher {self.name} sacrificed his life to resurrect {hero.name}')
                break


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'HACK')

    def apply_super_power(self, boss, heroes):
        stolen_health = randint(20, 50)
        boss.health -= stolen_health
        healed_hero = choice(heroes)
        healed_hero.health += stolen_health
        print(f'Hacker {self.name} stole {stolen_health} health from the boss and gave it to {healed_hero.name}')


class Golem(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'PROTECT')
        self.health *= 2  

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                damage_taken = boss.damage * 0.2
                hero.health += damage_taken
                self.health -= damage_taken
        print(f'Golem {self.name} took 20% of the damage for the team')


class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'STUN')

    def apply_super_power(self, boss, heroes):
        stun_chance = randint(1, 3)
        if stun_chance == 1:
            print(f'Thor {self.name} stunned the boss for 1 round!')
            boss.damage = 0  



round_number = 0

def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and hero.ability != boss.defence:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def show_statistics(boss, heroes):
    print(f'---------- ROUND {round_number} ----------')
    print(boss)
    for hero in heroes:
        print(hero)


def start_game():
    boss = Boss(name = 'Elena', health = 1500, damage = 50)

    warrior = Warrior(name = 'Ahiles', health = 280, damage = 10)
    magic = Magic(name = 'Potter', health = 260, damage = 10)
    berserk = Berserk(name = 'Guts', health = 240, damage = 5)
    doc = Medic(name = 'Merlin', health = 200, damage = 5, heal_points = 15)
    witcher = Witcher(name = 'Geralt', health = 250, damage = 0)
    hacker = Hacker(name = 'Neo', health = 220, damage = 5)
    golem = Golem(name = 'Rocky', health = 400, damage = 5)
    thor = Thor(name = 'Thor', health = 270, damage = 15)

    heroes_list = [warrior, magic, berserk, doc, witcher, hacker, golem, thor]

    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()
