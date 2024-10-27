salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
# Инициализация переменной для накопления необходимых средств
total_needed = 0

# Цикл по каждому месяцу
for month in range(months):
    # Если расходы увеличиваются на 5% в начале месяца, обновляем spend
    if month > 0:
        spend *= (1 + increase)

    # Рассчитываем нехватку средств
    deficit = spend - salary

    # Если есть нехватка, добавляем ее к общей необходимой сумме
    if deficit > 0:
        total_needed += deficit

# Округление до целого числа
total_needed = round(total_needed)

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", total_needed)
