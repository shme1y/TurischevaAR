def Task12A(a, b):
    if a<b :
        Task12A(a, b-1)
        print(b)
    elif a>b :
        print(a)
        Task12A(a-1, b)
    else :
        print(a)
a=int(input('Введите число 1'))
b=int(input('Введите число 2'))
Task12A(a, b)
