
def find_common_participants(group1, group2, delimiter=','):
    # Разделяем строки на списки участников по заданному разделителю
    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))

    # Находим общих участников с помощью пересечения множеств
    common_participants = participants1.intersection(participants2)

    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)

# Пример использования функции
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверка работы функции с разделителем '|'
common_participants = find_common_participants(participants_first_group, participants_second_group, '|')
print(common_participants)  # Вывод: ['Петров', 'Сидоров']