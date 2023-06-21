def neyron(a, o, t):
    sch = 0
    p = 25
    omega = 0
    i=0
    rez = 0
    for i in range(100):
        if (a[i] == t):
            for j in range(15):
                omega = omega + a[i][j]*o[j]

            if omega >= p:
                rez = o
            else:
                for k in range(15):
                    o[k] = o[k] + t[k]
                sch+=1
            omega = 0

        else:
            for j in range(15):
                omega = omega + a[i][j]*o[j]
            if omega > p:
                for k in range(15):
                    o[k] = o[k] - a[i][k]
                sch+=1
            omega = 0

    if sch==0:
        print (rez)
        for i in range(100):
            for j in range(15):
                omega = omega + a[i][j]*o[j]
            if omega>=p:
                print('Тройка', omega)
            else:
                print(omega)
            omega = 0
        return sch
    else:
        return sch



arr1 = [ 
[1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0],
[1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1],
[0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
[1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0],
[0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
[1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
[1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
[1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
[1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]]

#Петрова Александра УИБ-312 ЛР№1
arr = 10*arr1
om = [7, 3, 1, 5, 8, 0, 4, 3, 2, 7, 3, 1, 8, 5, 1]
three = [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0]

print(om)
sch = neyron(arr, om, three)
while sch!=0:
    sch = neyron(arr, om, three)

 

