from animal import Animal
from leg import Leg

cat = Animal()
dog = Animal()

cat.eyes = 1
dog.eyes = 4 #ignored 4 because its > 3, look at class

how_many_eyes = dog.eyes

cat.show()
dog.show()
print(how_many_eyes)

left_leg = Leg()
left_leg.smelly = False
print(left_leg.is_Smelly())