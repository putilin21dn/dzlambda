def minim(x,y,z):    #минимальое из трех чисел
    if x<y:
        if x<z:
            return x
        else:
            return z

    else:
        if y<z:
            return y
        else:

            return z

def equal(x,y,z):  # возвращает из тройки количество одинаковых чисел
    if x==y:
        if x==z:
            return 3
        else:
            return 2
    else:
        if x==z:
            return 2
        else:
            if y==z:
                return 2
            else:
                return 0

def sum_mas(s):  #сумма чисел в массиве
    summ = 0
    for i in range(len(s)):
        summ+=s[i]
    return summ

def kolvo_mas(s):  #количество чисел, равных нулю
    count = 0
    for i in range(len(s)):
        if s[i]==0:
            count+=1
    return count