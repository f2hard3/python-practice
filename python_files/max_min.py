index = [1, 52, 273, 32, 99]
max = index[0]
min = index[0]

for i in index:
    if max < i:
        max = i
    if min > i:
        min = i

print(max)
print(min)
