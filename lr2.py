#однослойный персептрон
def neyron(a, o):
    sch = 0
    omega = 0
    mass = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i=0
    rez = 0
    f = 0
    max_om = 0
    prov = 0
    while f!=10:
        for i in range(100):
            if (a[i] == a[f]):
                for j in range(10):
                    for b in range(9):
                        omega = omega + a[i][b]*o[j][b]
                    mass[j] = omega
                    omega = 0
                max_om = max(mass)
                

                if max_om == mass[f]:
                    rez = o[f]
                    if rez!= prov:
                        prov = rez
                        print(rez)
                        
                
                else:
                    maxin = mass.index(max_om)
                    for b in range(9):
                        o[f][b] = o[f][b] + a[f][b]
                        o[maxin][b] = o[maxin][b] - a[maxin][b]
                    sch+=2
                

            else:
                for j in range(10):
                    for b in range(9):
                        omega = omega + a[i][b]*o[j][b]
                    mass[j] = omega
                    omega = 0
                max_om = max(mass)

                if max_om != mass[f]:
                    maxin = mass.index(max_om)
                    for b in range(9):
                        o[f][b] = o[f][b] + a[f][b]
                        o[maxin][b] = o[maxin][b] - a[maxin][b]
                    sch+=2
                
                else:
                    rez = o[f]
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


arr1 = [ 
[1, 1, 0, 1, 1, 0, 1, 0, 0],
[0, 1, 0, 1, 0, 0, 1, 0, 1],
[0, 0, 1, 0, 1, 1, 0, 1, 1],
[0, 1, 1, 0, 1, 0, 1, 0, 0],
[0, 0, 1, 1, 0, 0, 0, 1, 0],
[1, 1, 0, 0, 1, 0, 0, 1, 1],
[1, 1, 0, 1, 1, 1, 0, 1, 1],
[1, 1, 0, 1, 0, 1, 0, 1, 1],
[1, 0, 0, 1, 1, 0, 0, 1, 0],
[0, 1, 1, 0, 0, 1, 0, 0, 0]]
 
#Петрова Александра УИБ-312 ЛР№3
arr = 10*arr1
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

for i in range(10):
    print(om[i])
print('Конечная матрица:')
sch = neyron(arr, om)
while sch!=0:
    sch = neyron(arr, om)
