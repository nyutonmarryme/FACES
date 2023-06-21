def neyron(a, o):
    sch = 0
    p = 25
    omega = 0
    i=0
    rez = 0
    for i in range(100):
        if (i==4)or(i==14)or(i==24)or(i==34)or(i==44)or(i==54)or(i==64)or(i==74)or(i==84)or(i==94):
            for j in range(9):
                omega = omega + a[i][j]*o[j]

            if omega >= p:
                rez = o
            else:
                for k in range(9):
                    o[k] = o[k] + a[i][k]
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
        print(sch)
        return sch


#9 ошибок в строке
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

#Петрова Александра УИБ-312 ЛР№2
arr = 10*arr1
om = [17, 25, 50, 0, 0, 0, 0, -5, -8]

sch = neyron(arr, om)
while sch!=0:
    sch = neyron(arr, om)





