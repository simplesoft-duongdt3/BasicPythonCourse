def basic_002_operations():
  print("Arithmetic Operators")
  # Arithmetic Operators (Mathematical Operations)
  #   + 	Addition
  x = 14 + 7
  print("14 + 7 =", x, type(x), "\n")

  # - 	Subtraction
  x = 25 - 12
  print("25 - 12 =", x, type(x), "\n")

  # * 	Multiplication
  x = 2 * 5
  print("2 * 5 =", x, type(x), "\n")

  # / 	Division
  x = 25 / 12
  print("25 / 12 =", x, type(x), "\n")

  # % 	Modulus
  x = 25 % 12
  print("25 % 12 =", x, type(x), "\n")

  # ** 	Exponentiation
  x = 2 ** 5
  print("2 ** 5 =", x, type(x), "\n")

  # // 	Floor division
  x = 25 // 12
  print("25 // 12 =", x, type(x), "\n")

  # Comparison Operators
  print("Comparison Operators")
  # == 	Equal
  x = 25 == 12	
  print("25 == 12 =", x, type(x), "\n")

  # != 	Not equal	
  x = 25 != 12	
  print("25 != 12 =", x, type(x), "\n")

  # > 	Greater than
  x = 25 > 12	
  print("25 > 12 =", x, type(x), "\n")

  # < 	Less than 	
  x = 25 < 12	
  print("25 < 12 =", x, type(x), "\n")

  # >= 	Greater than or equal to	
  x = 25 >= 12	
  print("25 >= 12 =", x, type(x), "\n")

  # <= 	Less than or equal to
  x = 25 <= 12	
  print("25 <= 12 =", x, type(x), "\n")

  #  Logical Operators
  print("Logical Operators")

  # and  	Returns True if both statements are true
  x = 100
  print("x=", x, "x > 99 and x < 101 =", x > 99 and x < 101, "\n")
  print("x=", x, "x > 99 and x < 90 =", x > 99 and x < 90, "\n")

  # or 	Returns True if one of the statements is true
  x = 100
  print("x=", x, "x > 99 or x < 101 =", x > 99 or x < 101, "\n")
  print("x=", x, "x > 99 or x < 90 =", x > 99 or x < 90, "\n")
  print("x=", x, "x > 100 or x < 90 =", x > 100 or x < 90, "\n")

  # not 	Reverse the result, returns False if the result is true
  x = 100
  print("x=", x, "not(x > 99 and x < 101) =", not(x > 99 and x < 101), "\n")
  print("x=", x, "not(x > 99 and x < 90) =", not(x > 99 and x < 90), "\n")


  # Identity Operators
  print("Identity Operators")

  # is  	Returns True if both variables are the same object
  # is not 	Returns True if both variables are not the same object
  a = 100
  b = 101 - 1
  print("a=", a, "b=", b, "a is b", a is b, "\n")

  a = 100
  b = 989
  print("a=", a, "b=", b, "a is b", a is b, "\n")

  a = "I'm here"
  b = "I'm here"
  print("a=", a, "b=", b, "a is b", a is b, "\n")

  list_1 = ['a', 'b', 'c']
  list_2 = list_1
  list_3 = list(list_1)
  print("list_1 =", list_1)
  print("list_2 =", list_2)
  print("list_3 =", list_3)
  print("list_1 is list_2", list_1 is list_2, "\n")
  print("list_1 is list_3", list_1 is list_3, "\n")
  print("list_1 is not list_3", list_1 is not list_3, "\n")

  # Membership Operators
  print("Membership Operators")
  # in  	Returns True if a sequence with the specified value is present in the object
  # not in 	Returns True if a sequence with the specified value is not present in the object
  list_1 = ['a', 'b', 'c']
  print("list_1 =", list_1)

  print("'a' in list_1", 'a' in list_1, "\n")
  print("'a' not in list_1", 'a' not in list_1, "\n")
