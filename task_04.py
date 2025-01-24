def sort_list(lst):
    if not lst:  
        return []
    
    minEl = min(lst)
    maxEl = max(lst)

    newLst = []

    for x in lst:
        if x == minEl:
            newLst.append(maxEl) 
        elif x == maxEl:
            newLst.append(minEl) 
        else:
            newLst.append(x)  

    newLst.append(minEl)

    return newLst

print(sort_list([]))               
print(sort_list([2, 4, 6, 8]))     
print(sort_list([1]))               
print(sort_list([1, 2, 1, 3]))     
