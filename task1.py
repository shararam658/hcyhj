from random import randint
a = randint(1, 100)
print(a)
atts = 0
x = 0
while x != a:
    x = int(input('Введите число:'))
    if x > a:
        print('Загаданное число меньше')
    if x < a:
        print('Загаданное число больше')
    if x == a:
        print("Вы угадали")
        break
    atts += 1
    if atts == 3:
        if a % 2==0:
            print('Загаданное число является четным')
        else:
            print('Загаданное число является нечетным')
            
    
    