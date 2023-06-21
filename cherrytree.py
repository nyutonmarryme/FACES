#15000
def oak(a, o, x, q):
    sch = 0
    omega = 0
    mass = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i=0
    rez = 0
    f = 0
    max_om = 0
    prov = 0
    while f!=len(x):
        for i in range(len(a)):
            if (a[i] == a[x[f]]):
                for j in range(10):
                    for b in range(9):
                        omega = omega + a[i][b]*o[j][b]
                    mass[j] = omega
                    omega = 0
                max_om = max(mass)
                

                if max_om == mass[x[f]]:
                    rez = o[x[f]]
                    if rez!= prov:
                        prov = rez
                        print(rez)
                        
                
                else:
                    maxin = mass.index(max_om)
                    for b in range(9):
                        o[x[f]][b] = o[x[f]][b] + a[x[f]][b]
                        o[maxin][b] = o[maxin][b] - a[maxin][b]
                    if i>q:
                        sch+=2
                

            else:
                for j in range(10):
                    for b in range(9):
                        omega = omega + a[i][b]*o[j][b]
                    mass[j] = omega
                    omega = 0
                max_om = max(mass)

                if max_om != mass[x[f]]:
                    maxin = mass.index(max_om)
                    for b in range(9):
                        o[x[f]][b] = o[x[f]][b] + a[x[f]][b]
                        o[maxin][b] = o[maxin][b] - a[maxin][b]
                    if i>q:
                        sch+=2
                
                else:
                    rez = o[x[f]]
                    if rez!= prov:
                        prov = rez
                        print(rez)
                        


        f+=1
    
    if sch==0:
        print (rez)
        return sch

    else:
        print(sch)
        return sch

def willow(a, o, t, z):
    sch = 0
    p = 25
    omega = 0
    i=0
    rez = 0
    for i in range(z):
        if (a[i] == t):
            for j in range(9):
                omega = omega + a[i][j]*o[j]

            if omega >= p:
                rez = o
            else:
                for k in range(9):
                    o[k] = o[k] + t[k]
                sch+=1
            omega = 0

        else:
            for j in range(9):
                omega = omega + a[i][j]*o[j]
            if omega > p:
                for k in range(9):
                    o[k] = o[k] - a[i][k]
                sch+=1
            omega = 0

    if sch==0:
        print (rez)
        return sch
    else:
        return sch


def remove(num):
    for i in range(len(num)):
        arr2.pop(num[i])


def recognition(num, w):
    error = 0
    arr = arr2*50
    sch = oak(arr, om, num, w)
    error += sch
    return error



arr1 = [ 
[0, 0, 1, 0, 0, 1, 0, 1, 1],
[1, 0, 1, 0, 1, 1, 0, 1, 0],
[1, 1, 0, 1, 0, 0, 1, 0, 0],
[1, 0, 0, 1, 0, 1, 0, 1, 1],
[1, 1, 0, 0, 1, 1, 1, 0, 1],
[0, 0, 1, 1, 0, 1, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 1, 0, 1, 0, 0],
[0, 1, 1, 0, 0, 1, 1, 0, 1],
[1, 0, 0, 1, 1, 0, 1, 1, 1]]


 
#Петрова Александра УИБ-312 ЛР№5
arr = 50*arr1
om = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]]

er = 0
print('Распознавание цифр 0-4 из цифр 0-9')
x1 = [7, 4, 1, 3, 8]
sch = oak(arr, om, x1, 390)
er += sch

#9, 2, 6, 3, 1, 5, 8, 0, 4, 7
#9, 2, 6, 3, 1, 5, 8, 4, 7
#9, 2, 6, 3, 5, 8, 4, 7
#9, 6, 3, 5, 8, 4, 7
#9, 6, 5, 8, 4, 7
#9, 6, 5, 8, 4, 7

#2, 3, 1, 0, 4


x2 = [0, 1, 3, 3, 5]
arr2 = arr1
remove(x2)

#2, 3, 1, 0, 4
print('Распознавание цифр 0-1')
z = [2, 3]
error = recognition(z, 240)
er += error
x2 = [0, 0, 2]
remove(x2)

print('Распознавание цифры 0')
arr = arr2*50
sch = willow(arr, om[0], arr2[1], len(arr))
while sch!= 0:
    sch = willow(arr, om[0], arr2[1], len(arr))

print('Распознавание цифры 1')
arr = arr2*50
sch = willow(arr, om[0], arr2[0], len(arr))
while sch!= 0:
    sch = willow(arr, om[0], arr2[0], len(arr))

arr1 = [ 
[0, 0, 1, 0, 0, 1, 0, 1, 1],
[1, 0, 1, 0, 1, 1, 0, 1, 0],
[1, 1, 0, 1, 0, 0, 1, 0, 0],
[1, 0, 0, 1, 0, 1, 0, 1, 1],
[1, 1, 0, 0, 1, 1, 1, 0, 1],
[0, 0, 1, 1, 0, 1, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 1, 0, 1, 0, 0],
[0, 1, 1, 0, 0, 1, 1, 0, 1],
[1, 0, 0, 1, 1, 0, 1, 1, 1]]


x2 = [0, 1, 3, 3, 5, 2, 2]
arr2 = arr1
remove(x2)
print('Распознавание цифр 2-3')
z = [0, 1]
error = recognition(z, 240)
er += error

x2 = [0, 0]
remove(x2)
print('Распознавание цифры 4')
arr = arr2*50
sch = willow(arr, om[0], arr2[0], len(arr))
while sch!= 0:
    sch = willow(arr, om[0], arr2[0], len(arr))


arr1 = [ 
[0, 0, 1, 0, 0, 1, 0, 1, 1],
[1, 0, 1, 0, 1, 1, 0, 1, 0],
[1, 1, 0, 1, 0, 0, 1, 0, 0],
[1, 0, 0, 1, 0, 1, 0, 1, 1],
[1, 1, 0, 0, 1, 1, 1, 0, 1],
[0, 0, 1, 1, 0, 1, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 1, 0, 1, 0, 0],
[0, 1, 1, 0, 0, 1, 1, 0, 1],
[1, 0, 0, 1, 1, 0, 1, 1, 1]]


x2 = [0, 1, 3, 3, 5, 2, 2, 2]
arr2 = arr1
remove(x2)
print('Распознавание цифры 2')
arr = arr2*50
sch = willow(arr, om[0], arr2[0], len(arr))
while sch!= 0:
    sch = willow(arr, om[0], arr2[0], len(arr))

print('Распознавание цифры 3')
arr = arr2*50
sch = willow(arr, om[0], arr2[1], len(arr))
while sch!= 0:
    sch = willow(arr, om[0], arr2[1], len(arr))


arr1 = [ 
[0, 0, 1, 0, 0, 1, 0, 1, 1],
[1, 0, 1, 0, 1, 1, 0, 1, 0],
[1, 1, 0, 1, 0, 0, 1, 0, 0],
[1, 0, 0, 1, 0, 1, 0, 1, 1],
[1, 1, 0, 0, 1, 1, 1, 0, 1],
[0, 0, 1, 1, 0, 1, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 1, 0, 1, 0, 0],
[0, 1, 1, 0, 0, 1, 1, 0, 1],
[1, 0, 0, 1, 1, 0, 1, 1, 1]]



arr = 50*arr1
#9, 2, 6, 3, 1, 5, 8, 0, 4, 7

print('Распознавание цифр 5-9 из цифр 0-9')
x1 = [5, 2, 9, 6, 0]
sch = oak(arr, om, x1, 390)
er += sch

x2 = [1, 2, 2, 4, 4]
arr2 = arr1
remove(x2)

#9, 6, 5, 8, 7
print('Распознавание цифр 5-6')
z = [2, 1]
error = recognition(z, 240)
er += error
x2 = [0, 2, 2]
remove(x2)

print('Распознавание цифры 5')
arr = arr2*50
sch = willow(arr, om[0], arr2[1], len(arr))
while sch!= 0:
    sch = willow(arr, om[0], arr2[1], len(arr))

print('Распознавание цифры 6')
arr = arr2*50
sch = willow(arr, om[0], arr2[0], len(arr))
while sch!= 0:
    sch = willow(arr, om[0], arr2[0], len(arr))

arr1 = [ 
[0, 0, 1, 0, 0, 1, 0, 1, 1],
[1, 0, 1, 0, 1, 1, 0, 1, 0],
[1, 1, 0, 1, 0, 0, 1, 0, 0],
[1, 0, 0, 1, 0, 1, 0, 1, 1],
[1, 1, 0, 0, 1, 1, 1, 0, 1],
[0, 0, 1, 1, 0, 1, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 1, 0, 1, 0, 0],
[0, 1, 1, 0, 0, 1, 1, 0, 1],
[1, 0, 0, 1, 1, 0, 1, 1, 1]]

#9, 8, 7
x2 = [1, 2, 2, 4, 4, 1, 1]
arr2 = arr1
remove(x2)
print('Распознавание цифр 7-8')
z = [2, 1]
error = recognition(z, 240)
er += error

x2 = [1, 1]
remove(x2)
print('Распознавание цифры 9')
arr = arr2*50
sch = willow(arr, om[0], arr2[0], len(arr))
while sch!= 0:
    sch = willow(arr, om[0], arr2[0], len(arr))


arr1 = [ 
[0, 0, 1, 0, 0, 1, 0, 1, 1],
[1, 0, 1, 0, 1, 1, 0, 1, 0],
[1, 1, 0, 1, 0, 0, 1, 0, 0],
[1, 0, 0, 1, 0, 1, 0, 1, 1],
[1, 1, 0, 0, 1, 1, 1, 0, 1],
[0, 0, 1, 1, 0, 1, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 1, 0, 1, 0, 0],
[0, 1, 1, 0, 0, 1, 1, 0, 1],
[1, 0, 0, 1, 1, 0, 1, 1, 1]]


x2 = [1, 2, 2, 4, 4, 1, 1, 0]
arr2 = arr1
remove(x2)
print('Распознавание цифры 8')
arr = arr2*50
sch = willow(arr, om[0], arr2[0], len(arr))
while sch!= 0:
    sch = willow(arr, om[0], arr2[0], len(arr))

print('Распознавание цифры 7')
arr = arr2*50
sch = willow(arr, om[0], arr2[1], len(arr))
while sch!= 0:
    sch = willow(arr, om[0], arr2[1], len(arr))

print(er)
