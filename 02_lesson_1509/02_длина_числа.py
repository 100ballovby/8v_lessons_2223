# определение количества цифр в числе
number = input('Введите число: ')
# так как input возвращает строчку, можно померять длину строки
if len(number) == 2:
    number = int(number)  # превращаю ввод в целое число
    print('двузначное')
elif len(number) == 3:
    print('трехзначное')
elif len(number) == 4:
    print('четырехзначное')
else:
    print('Такие числа использовать нельзя.')
