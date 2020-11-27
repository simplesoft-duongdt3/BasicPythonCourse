def control_flow():
    items = [1, 2, 3, 4, 5]
    for i in range(len(items) -1, -1, -1):
      print(str(i) + " " + str(items[i]))