class Person:
	def Hello(self, name=None,age=None):
        self.name=name
        self.age=age
        print("Name:", self.name,"Age:",self.age)

p1=Person()
p1.Hello()
p1.Hello('GouthamAS')
p1.Hello('GouthamAS',25)