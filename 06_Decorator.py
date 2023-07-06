list=[3, 2, 3, 4, 4, 5]
dup=[]
unique=[]

for i in range(0, len(list)):
    j=i+1
    for j in range(j, len(list)):
        if list[i]==list[j] and list[i] not in dup:
            dup.append(list[i])
    if list[i] not in unique:
        unique.append(list[i])

print(dup)
print(unique)
#using single for loop
for i in list:
    if i not in unique:
        unique.append(i)
    elif i not in dup:
        dup.append(i)

print(unique)
print(dup)
