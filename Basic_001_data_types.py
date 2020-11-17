#Ref https://www.programiz.com/python-programming/methods/built-in/abs
def basic_001_data_types():
  x = "Hello World" 	
  print(x, type(x), "\n")

  x = str("Hello World")
  print(x, type(x), "\n")

  x = 20  	
  print(x, type(x), "\n")

  x = int(20)  	
  print(x, type(x), "\n")

  x = 20.5  	
  print(x, type(x), "\n")

  x = float(20.5)
  print(x, type(x), "\n")

  x = 1j
  print(x, type(x), "\n")

  x = complex(1j)
  print(x, type(x), "\n")

  x = ["apple", "banana", "cherry"] 	
  print(x, type(x), "\n")

  x = list(["apple", "banana", "cherry"])
  print(x, type(x), "\n")

  xtuple = ("apple", "banana", "cherry")
  x = list(xtuple)
  print(x, type(x), "\n")

  x = range(6) 	
  print(x, list(x), type(x), "\n")

  x = range(0, 6) 	
  print(x, list(x), type(x), "\n")

  x = range(0, 6, 1) 	
  print(x, list(x), type(x), "\n")

  x = range(-6, 0) 	
  print(x, list(x), type(x), "\n")

  x = {"name" : "John", "age" : 36} 	
  print(x, type(x), "\n")

  x = dict({"name" : "John", "age" : 36})
  print(x, type(x), "\n")

  x = {"apple", "banana", "cherry"} 	
  print(x, type(x), "\n")

  x = set({"apple", "banana", "cherry"})
  print(x, type(x), "\n")

  x = frozenset({"apple", "banana", "cherry"}) 	
  print(x, type(x), "\n")

  x = True 	
  print(x, type(x), "\n")

  x = False 	
  print(x, type(x), "\n")

  x = b"Hello" 	
  print(x, type(x), "\n")

  x = bytearray(5) 
  print(x, type(x), "\n") 	


