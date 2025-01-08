def coincidence(list=None, range=None):
  
  if list is None or range is None:
      return []

  result = []

  for item in list:
      if isinstance(item, (int, float)) and item >= range.start and item < range.stop:
          result.append(item)

  return result


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))  # [3, 4, 5]
print(coincidence())  # []
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))  # [1, 2, 2.5]
