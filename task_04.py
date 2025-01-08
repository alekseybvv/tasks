def sort_list(list):
  if not list:
      return list

  minEl = min(list)
  maxEl = max(list)

  minIndex = list.index(minEl)
  maxIndex = list.index(maxEl)

  list[minIndex], list[maxIndex] = list[maxIndex], list[minIndex]

  list.append(minEl)

  return list

print(sort_list([]))  # []
print(sort_list([2, 4, 6, 8]))  # [8, 4, 6, 2, 2]
print(sort_list([1]))  # [1, 1]
print(sort_list([1, 2, 1, 3]))  # [3, 2, 3, 1, 1]
