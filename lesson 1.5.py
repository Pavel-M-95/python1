print('Программа расчет рентабельности фирмы')
proceeds = int(input('Введите сумму полученной выручки за период: '))
cost = int(input('Введите сумму понесенных затрат за период: '))

if proceeds > cost:
    profit = proceeds - cost
    print(f'Ваша прибыль составляет {profit} рублей')
    if proceeds > cost:
        rent = profit / proceeds
        print(f'Рентабельность выручки составляет: {rent} ')
        if proceeds > cost:
            emp = int(input('Введите количество сотрудников в вашей фирме: '))
            total = profit/ emp
            print(f'Прибыль фирмы на в расчете на одного сотрудника равна: {total:.2f} рублей')
else:
    loss = cost - proceeds
    print(f'Ваш убыток составил {loss} рублей')
