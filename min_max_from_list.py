a_list = [20, 150, 20, 4, 100]
max_number = a_list[0]
min_number = a_list[0]
for i in range(0, len(a_list)):
    if max_number < a_list[i]:
        max_number = a_list[i]
for i in range(0, len(a_list)):
    if min_number > a_list[i]:
        min_number = a_list[i]
print("Max Number ", max_number)
print("Mininum Number ", min_number)
