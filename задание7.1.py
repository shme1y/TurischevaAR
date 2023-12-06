from random import randint
l = [randint(10,100) for x in range(10)]
def func(l):
    l=sorted(l)
    for i in range(len(l)):
        if l[i]%2!=0:
            print(l[i])
            break
func(l)
