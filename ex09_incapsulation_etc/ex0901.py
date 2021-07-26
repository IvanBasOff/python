class Dog():
    def __init__(self,
                 name,
                 breed,
                 owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self, name):
        self.name = name

mick = Person("Mike")
stan = Dog("Stanly", "Bobik", mick)

print(stan.owner.name)

class Shape():
    def __init__(self):
        self.who_am_i = "Im figure"
    def who(self):
        print("Its figure")
    

class Rectangle(Shape):
    recs = [] # class peremennaya
    
    def __init__(self,
                 width,
                 height):
        self.width = width # peremennaya exemplyara
        self.height = height
        self.recs.append((self.width, self.height))
    def calc_s(self):
        return self.width * 2 + self.height * 2
    def change_size(self, h_plus, w_plus):
        self.width += w_plus
        self.height += h_plus
    def __repr__(self):
        return 'Im Rectangle'



a_rec = Rectangle(10, 10)
print(a_rec.calc_s())
a_rec.change_size(2, 2)
print(a_rec.calc_s())
a_rec.who()
#print(a_rec.who())
print(a_rec.recs)
print(a_rec)


class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)
