print('Вас приветствует программа подсчета результат тренировок')
result = int(input('Введите результат пробежки в киллометрах в первый день - '))
final_result = int(input('Ведите целевой результат, которого вы хотите достичь - '))

days = 0


while final_result - result > 0:
    if days <= 0:
        print(f'Результат в 1 - й день: ' + f'{result:.2f}')
        days += 1
    else:
        result = result * 1.1
        days = days + 1
        print(f'Результат в {days} - й день: ' + f'{result:.2f}')
print(f'Желаемого результат вы достигнете на {days} - й день и пробежите\nне менеее {final_result:.2f} км')

