i = 0
lst = []
while i < 10:
 n = int(input('Введите число 1'))
 lst.append(n * 10)
 i += 1
lst.sort()
print(lst)