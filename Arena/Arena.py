class Dice:
	def __init__(self, number_of_sides = 6):
		self.__number_of_sides = number_of_sides

	def return_number_of_sides(self):
		return self.__number_of_sides

	def roll_the_dice(self):
		import random as _random
		return _random.randint(1, self.__number_of_sides)

class Hero:
	def __init__(self, name, life, attack, defense, dice):
		self._name = name
		self.__life = life
		self.__max_life = life
		self.__attack = attack
		self.__defense = defense
		self._dice = dice
		self.__message = ""
	
	def __str__(self):
		return str(self._name)

	def _set_message(self, message):
		self.__message = message

	def return_last_message(self):
		return self.__message 

	@property
	def alive(self):
		return self.__life > 0


	def life_bar(self):
		sum = 20
		count = int(self.__life / self.__max_life * sum)
		if count == 0 and self.alive:
			count = 1
		return "[{0}{1}]".format("@" * count, " " * (sum - count))


	def start_defending(self, hit):
		damage = hit - (self.__defense + self._dice.roll_the_dice())
		if damage > 0:
			message = "{0} utrpěl poškození {1}".format(self._name,damage)
			self.__life = self.__life - damage
			if self.__life < 0:
				self.__life = 0
				message = message[:-1] + " a zemřel."
		else:
			message = "{0} se ubránil!".format(self._name)
		self._set_message(message)

	def start_attacking(self, enemy):
		hit = self.__attack + self._dice.roll_the_dice()
		message = "{0} zaútočil o síle {1}!".format(self._name, hit)
		enemy.start_defending(hit)
		self._set_message(message)

class Mage(Hero):

	def __init__(self, name, life, attack, defense, dice, mana, magic_attack):
		super().__init__(name, life, attack, defense, dice)
		self.__mana = mana
		self.__mana_max = mana
		self.__magic_attack = magic_attack

	def start_attacking(self, enemy):
		if self.__mana == self.__mana_max:
			self.__mana = self.__mana - 50
			hit = self.__magic_attack + self._dice.roll_the_dice()
			message = "{0} zaútočil magií o síle {1}!".format(self._name, hit)
			enemy.start_defending(hit)
			self._set_message(message)

		else:
			self.__mana = self.__mana + 10
			super().start_attacking(enemy)
		
			



class Arena:
	def __init__(self, hero_1, hero_2, dice):
		self.__hero_1 = hero_1
		self.__hero_2 = hero_2
		self._dice = dice

	def basic_info(self):
		self.__clean_the_cmd
		print("-----------ARENA-----------\n")
		print(hero_1)
		print("Život: {0}".format(hero_1.life_bar()))
		print("---------------------- \n")
		print(hero_2)
		print("Život: {0}".format(hero_2.life_bar()))
		print("\n")

	def __clean_the_cmd(self):
		import sys as _sys
		import subprocess as _subprocess
		if _sys.platform.startswith("win"):
			_subprocess.call("cmd.exe", "/C","cls")
		else:
			_subprocess.call(["clear"])

	def __drop_the_message(self, message):
		import time as _time
		print(message)
		_time.sleep(1)

	def fight(self):
		import random as _random
		print("Vítejte v aréně!")
		print("Dnes se utkají {0} s {1}!".format(self.__hero_1, self.__hero_2))
		print("Zápas může začít...", end=" ")
		input()

		if _random.randint(0,1):
			(self.__hero_1 , self.__hero_2) = (self.__hero_2, self.__hero_1)

		while (self.__hero_1.alive and self.__hero_2.alive):
			self.__hero_1.start_attacking(self.__hero_2)
			self.basic_info()
			self.__drop_the_message(self.__hero_1.return_last_message())
			self.__drop_the_message(self.__hero_2.return_last_message())
			if self.__hero_2.alive:
				self.__hero_2.start_attacking(self.__hero_1)
				self.basic_info()
				self.__drop_the_message(self.__hero_2.return_last_message())
				self.__drop_the_message(self.__hero_1.return_last_message())
			print("")



dice = Dice(15)
hero_1 = Hero("Warrior", 100, 20, 10, dice)
hero_2 = Mage("Mág", 100, 20, 10, dice, 50, 20)
arena = Arena(hero_1,hero_2,dice)
arena.fight()
input()



#input();






