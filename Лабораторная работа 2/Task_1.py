money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0  # Количество месяцев

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while money_capital + salary > spend:
    money_capital = money_capital + salary - spend
    spend *= 1 + increase
    month += 1


print("Количество месяцев, которое можно протянуть без долгов:", month)
