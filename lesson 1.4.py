n = int(input('Введите целое положительное число: '))
mx = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > mx:
        mx = n % 10
    if n > 9:
        continue
    else:
        print('Максимальная цифра, в вашем числе: ' + str(mx))
        break
