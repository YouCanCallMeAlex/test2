x = int(input("сумма вклада:"))
p = int(input("годовой процент:"))
y = int(input("итоговая сумма вклада:"))
b = 0 
while x < y :
    x += (x//100*p)
    b+=1
print(b)