#parent class for every animals (lion, elephant, tas monkey)
class Animal:
  def __init__ (self,name):
    self.name=name
  #default na pagkain ng animal
  def eat(self):
    print(self.name, "eats.")
  #default na pag gawa ng sound ng animal
  def make_sound(self):
    print (self.name, "makes a sound.")
#child class ng Animal
class Lion(Animal):
 #ung lion nag mamake ng sound na "roars loudly"
  def make_sound(self):
    print(self.name, "roars loudly!")
  #ung pagkain ng lion is fresh meat
  def eat(self):
    print(self.name, "eats fresh meat.")
#child class ng Animal
class Elephant(Animal):
 #sound ng elephant
  def make_sound(self):
    print(self.name, "trumpets!")
  #pagkain ng elephant
  def eat(self):
    print(self.name, "eats grass and fruits.")
#child class ulit ng Animal
class Monkey(Animal):
  #sound ng Monkey is "chatters!"
  def make_sound(self):
    print(self.name, "chatters!")
  #pagkain ng Monkey is bananas
  def eat(self):
    print(self.name, "eats bananas.")
#makes the objects for each Animal
lion= Lion("Simba")
elephant= Elephant("Dumbo")
monkey= Monkey("George")
#contains all the animals sa iisang list
animals= [lion, elephant, monkey]
#tinatawag isa-isa ung methods ng bawat animal
for animal in animals:
  animal.make_sound()
  animal.eat()
  print("-----")
