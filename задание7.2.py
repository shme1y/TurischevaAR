from random import randint
A = [randint(10,100) for x in range(10)]
B = [randint(10,100) for x in range(10)]
def func(A,B):
    print(A,B)
    A,B=B,A
    print(A,B)
func(A,B)
