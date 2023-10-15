l = [1,4,1,6,'hello','a',5,'hello']
m = []
a = []
for i in l:
    if i not in m:
        m.append(i)
    else:
        a.append(i)
print(l , a)