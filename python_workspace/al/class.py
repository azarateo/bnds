class Dog:
	kind = ''
	name = ''
	sound = ''

	def __init__(self,name,kind,sound):
		self.name = name
		self.kind = kind
		self.sound = sound

	def objectBark(self,times):
		for i in range(times):
			print(self.sound)

	@staticmethod
	def bark(times):
		for i in range(times):
			print('wuf')
	

x = Dog('Fluffy','Akita','Wuffffff')

print(x.name)
print(x.kind)
x.objectBark(5)
Dog.bark(6)
