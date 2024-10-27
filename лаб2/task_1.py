money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
# Переменная для подсчета месяцев
months = 0

# Цикл, пока расходы меньше или равны общему бюджету
while spend <= (salary + money_capital):
    # Увеличиваем количество месяцев
    months += 1

    # Вызываем текущий бюджет
    budget = salary + money_capital

    # Уменьшаем финансовую подушку на текущие расходы
    money_capital -= spend - salary

    # Увеличиваем расходы на 5%
    spend *= (1 + increase)

# Выводим результат
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", months)
