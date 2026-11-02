cisla = [100, 5, 70, 8, 4, 40, 9, 30, 1]

n = len(cisla)
for i in range(1,n):
  vlozit = i
  hodnota = cisla.pop(i)
  for j in range(i-1, -1, -1):
    if cisla[j] > hodnota:
      vlozit = j
  cisla.insert(vlozit, hodnota)

print(cisla)