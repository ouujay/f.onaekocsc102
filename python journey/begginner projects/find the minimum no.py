def min_value(list_of_numbers):
  min_value = None
  for number in list_of_numbers:
    if min_value is None or number < min_value:
      min_value = number
      a =[]
      a.append(min_value)
      print (a)
  return min_value 

list_of_numbers = [10, 2, 5, 3, 1]
print(min_value(list_of_numbers))

