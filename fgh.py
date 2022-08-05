i = 0
lst = []
while i < 10:
 n = int(input('Введите любые числа 10 раз: '))
 lst.append(n * 10)
 i += 1
lst.sort()
print(lst)
