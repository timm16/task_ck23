list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
middle = len(set(list_players)) // 2
one_team = list_players[:middle]
two_team = list_players[middle:]
print(one_team)
print(two_team)