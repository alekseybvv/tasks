def max_odd(array):
  maxNum = None

  for element in array:
      if isinstance(element, (int, float)):
          if element == int(element) and int(element) % 2 != 0:
              element = int(element)  
              if maxNum is None or element > maxNum:
                  maxNum = element

  return maxNum

print(max_odd([1, 2, 3, 4, 4])) # 3
print(max_odd([21.0, 2, 3, 4, 4])) # 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None])) # 3
print(max_odd(['ololo', 'fufufu'])) # None
print(max_odd([2, 2, 4])) # None


