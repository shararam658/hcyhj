s = input('Введите строку:')

m1 = 0
m2 = 0
m3 = 0

glas_let = 'аеёиоуыэюя'
glas_cnt = 0

sogl_let = 'бвгджзйклмнпрстфхцчшщ'
sogl_cnt = 0 

a = set(s)

for k in glas_let:
    glas_cnt += glas_let.count(k)
print(glas_cnt)

for j in glas_let:
    sogl_cnt += sogl_let.count(j)
print(sogl_cnt)

print(s.count(' '))

for i in range(len(a)):
    print(max(s.count(a[i])))
        
