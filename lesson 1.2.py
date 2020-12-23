def Convert(x):
    day = int(x / 86400)
    x -= (day * 86400)
    hour = int(x / 3600)
    x -= (hour * 3600)
    mm = int(x / 60)
    x -= (mm * 60)
    sec = x
    print('Ввремя', day,':дд', hour,':чч', mm,':мм', sec,':cc')


Convert(int(input('Введите время в секунах: ')))
