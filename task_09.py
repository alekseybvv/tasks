def connect_dicts(dict1, dict2):
    sum_dict1 = sum(dict1.values())  
    sum_dict2 = sum(dict2.values())  

    if sum_dict1 > sum_dict2:
        first_dict = dict1
        second_dict = dict2
    else:
        first_dict = dict2
        second_dict = dict1

    total_dict = {}
    for key, value in first_dict.items():
        if value >= 10:
            total_dict[key] = value

    for key, value in second_dict.items():
        if value >= 10 and key not in total_dict:
            total_dict[key] = value

    sorted_items = sorted(total_dict.items(), key=lambda item: item[1]) 

    sorted_dict = dict(sorted_items)  

    return sorted_dict

print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }))
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }))
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }))
