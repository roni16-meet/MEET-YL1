class Animal:
	def __init__(self, name, color, age, size, is_full,tired):
		self.name= name
		self.color= color
		self.age= age
		self.size= size
		self.is_full= is_full
		self.tired= tired
	def print_all(self):

		print(self.name)
		print(self.color)
		print(self.age)
		print(self.size)
		
	def be_hungry(self):
		self.is_full=False
		print(self.name + "be hungry!")
	
	def eat(self):
		if self.is_full==True:
			print(self.name +" eat:fuck you I am not hungry")
		else: 
			print(self.name +" "+"eat:what to eat?")
			food=input("what to eat?")
			print(self.name +" eat:Yum Yum Yum " + food)
			self.is_full=True
	def sleep(self):
		if self.tired==False:
			print(self.name +" sleep: Fuck you I'm not tired")
		else:
			print(self.name+" sleep: zzzzzz")
			self.tired=False		
		
	def jump_rope(self):
		if self.tired==True:
			print(self.name +" jump: I'm too tired fuck you, I want to sleep!")
		else:
			print(self.name +" jump: jump jump jump")
			self.tired=True
		
		
alpaka = Animal(name="Sokrates", color="purple", age=6, size="2.5  cubic roni gever ", is_full=False, tired= False)
lama= Animal(name="Nikolau", color="bezh", age= 17, size= "0.5 cubic roni gever", is_full=False, tired= False)

alpaka.print_all()
alpaka.eat()
lama.eat()

lama.jump_rope()
alpaka.eat()
lama.jump_rope()
lama.sleep()
lama.sleep()
