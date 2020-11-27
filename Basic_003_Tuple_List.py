def basic_003_Tuple_List():
  fruits = ("apple", "apple", "banana", "cherry")
  print(fruits)

  fruits = tuple((("apple1", "banana", "cherry", "apple2")))
  print(fruits)

  print(len(fruits))

  print(type(fruits))

  print(fruits[0])

  print(fruits[0:2])

  print(type(fruits[0:2]))

  print(fruits[-1])
  print(fruits[-2:-1])

  print("dog" in fruits)
  print("banana" in fruits)

  # List
  # Negative indexing
  fruits = ["apple", "bannana", "chery", "apple"]
  print(fruits[-1])
            
  # Range indexing ([0:2] = from 0 to 1)
  print(fruits[0:2])
  print(fruits[:2])
  print(fruits[1:])
  print(fruits[-2:-1])

  # Check item in
  print("dog" in fruits)
  print("apple" in fruits)