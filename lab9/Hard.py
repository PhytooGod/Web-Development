c = input().split(' ')
n = int(c[0])
m = int(c[1])
a = []
for i in range(n):
    a.append([])
    b = input()
    for j in range(m):
        a[i].append(b[j])
k = []
l = []
for j in range(m):
    for i in range(n):
        k.append(a[i][j].isalnum())
        l.append(a[i][j])
while k[-1] == False:
    k.pop(-1)
indexes = []
offset = -1
while True:
    try:
        offset = k.index(False, offset+1)
    except ValueError:
        break
    indexes.append(offset)
for i in indexes:
    l[i] = ' '
print(*l, sep='')