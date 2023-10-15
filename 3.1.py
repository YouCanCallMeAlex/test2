def area(a,b,c):
    p = a + b + c
    return (p*(p - a)*(p - b)*(p - c))**0.5
result = area(4,5,6)
print(result)