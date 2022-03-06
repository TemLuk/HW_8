list1 = [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
list_sort = sorted(list1, key=lambda x: x[1])
print(list_sort)