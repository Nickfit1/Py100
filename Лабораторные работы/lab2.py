list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle_index = int(len(list_players)/2) # индекс середины

Team1 = list_players[0:middle_index]

Team2 = list_players[middle_index:]

print(Team1)
print(Team2)