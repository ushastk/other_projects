from random import *
a = randint(1, 101)
n = int(input("���������� ������� ����� "))
while a != n:
    if n > a:
        print("������� �����, ���������� ��� ��� ")
    elif n < a:
        print("������� ����, ���������� ��� ��� ")
    n = int(input())
if a == n:
    print("�� �������, �����������!")