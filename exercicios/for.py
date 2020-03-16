a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [a[num]for num in range(len(a)) if (num % 2) != 0]
print(b)
# nao entedi o pq precisa ser diferente(if (num % 2) != 0), se for igual (if (num % 2) == 0) imprimi os impares