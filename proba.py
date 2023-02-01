from random import *
a = randint(1, 101)
n = int(input("Попробуйте угадать число "))
while a != n:
    if n > a:
        print("Слишком много, попробуйте еще раз ")
    elif n < a:
        print("Слишком мало, попробуйте еще раз ")
    n = int(input())
if a == n:
    print("Вы угадали, поздравляем!")