a = int(input())  '''Ряд - 1'''
b = int(input())
for i in range(a, b + 1):
    print(i)
    
    

a = int(input())  '''Ряд - 2'''
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)



n = int(input())  '''Сумма N чисел'''
sum = 0
for i in range(n):
    sum += int(input())
print(sum)



res = 1  '''Факториал'''
n = int(input())
for i in range(1, n + 1):
    res *= i
print(res)




n = int(input())  '''Лесенка'''
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()


