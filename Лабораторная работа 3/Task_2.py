# TODO Напишите функцию find_common_participants
def find_common_participants(str1,str2, separator = ','):
    group1 = str1.split(separator)
    group2 = str2.split(separator)
    common = list(set(group1).intersection(group2))
    common.sort()
    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group))