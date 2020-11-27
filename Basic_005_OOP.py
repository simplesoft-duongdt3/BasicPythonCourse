# Ref https://realpython.com/python3-object-oriented-programming/#classes-vs-instances
class Person:
  walkSpeed = 10
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print("Person init")
  
  def changeName(self, name):
    self.name = name

  def walk(self):
    print("I'm walking speed = " + str(self.walkSpeed))

  def __str__(self):
    #return super.__str__(self)
    return "Person(name={} age={} walkSpeed={})".format(self.name, self.age, self.walkSpeed)

class FlyingCreature():
  def __init__(self, flySpeed):
    self.flySpeed = flySpeed
    print("FlyingCreature init")

  def __str__(self):
    #return super.__str__(self)
    return "FlyingCreature(flySpeed={})".format(self.flySpeed)


class FlyingPerson(Person, FlyingCreature):
  def __init__(self, name, age, flySpeed):
    Person.__init__(self, name, age)
    FlyingCreature.__init__(self, flySpeed)
    print("FlyingPerson init")

  def __str__(self):
    return Person.__str__(self) + " " + FlyingCreature.__str__(self)

def changeNamePerson():
  person = FlyingPerson("Duong", 30, 108)
  person.name = "Duong1"

  person1 = person
  print(person)
  person1.walk()

  person.walkSpeed = 100
  person.flySpeed = 100
  person.age = 31
  person.changeName("Duong2")
  person2 = person
  person1.walk()
  print(person)

  print("person1 == person2 => " + str(person1 == person2))
