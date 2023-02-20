# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

def PieceDerChokolate (m1, n1, k1):
    amount = n1 * m1
    if k1 == 0: print('NO')
    elif((k1 % m1 == 0) and (k1 <= amount)) or ((k1 % n1 == 0) and (k1 <= amount)):
        print('YES')
    else: print('NO')
  
print('Введите размеры шоколдаки - m и n')
print('Введите m:')
m = int(input())
print('Введите n:')
n = int(input())

print('А теперь введите k долек, которые хотите отломить:')
k = int(input())
PieceDerChokolate(m, n, k)
