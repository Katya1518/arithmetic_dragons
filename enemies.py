# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice
def IsPrime(n):

    d = 2

    while n % d != 0:

        d += 1

    return d == n


def Factor(n):

    Ans = []

    d = 2

    while d * d <= n:

        if n % d == 0:

            Ans.append(d)

            n //= d

        else:

            d += 1

    if n > 1:

        Ans.append(n)

    return Ans


class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list
def generate_troll_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

class Troll(Enemy):
    def set_answer(self, answer):
        self._answer = answer
    def check_answer(self, answer):
        return answer == self.__answer


class GuessTroll(Troll):
    def __init__(self):
        self._health = 50
        self._attack = 5
        self._color = 'грязный'
    def question(self):
        x = randint(1,5)
        self.__quest = 'Угадай число от 1 до 5'
        self.set_answer(x)
        return self.__quest


class EasyNumberTroll(Troll):
    def __init__(self):
        self._health = 60
        self._attack = 5
        self._color = 'очень грязный'




    def question(self):
        x = randint(1,50)
        self.__quest = str(x) + 'это простое число?'
        k = IsPrime(x)
        self.set_answer(k)
        return self.__quest

class ComponentTroll(Troll):
    def __init__(self):
        self._health = 60
        self._attack = 5
        self._color = 'совсем грязный'
    def question(self):
        x = randint(1,100)
        self.__quest = str(x)+', разложи мне его!!!'
        n = Factor(x)
        self.set_answer(n)
        return self.__quest

class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 13
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest


class BlackDragon(Dragon):
    def __init__(self):
        self._health = 300
        self._attack = 17
        self._color = 'черный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest
#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.


enemy_types = [GreenDragon, RedDragon, BlackDragon]