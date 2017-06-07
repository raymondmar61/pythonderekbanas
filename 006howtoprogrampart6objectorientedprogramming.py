class Animal:
	def __init__(self, name="No Name"):
		self._name = name

	def set_name(self, name ="No Name"):
		self._name = name

	def get_name(self):
		return self._name

	def noise(self):
		print("Errrrr")

	def move(self):
		print("Moving Forward")

	def eat(self):
		print("Crunch, Crunch")

dog = Animal("Puppy")
dog.noise()
dog.move()
dog.eat()
print(dog.get_name())
dog.set_name("Jake")
print(dog.get_name())
