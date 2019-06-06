from math import cos, factorial, pow

x = float(input('x: '))
n = int(input('n: '))

res = x

for i in range(1, n):
    res += -((pow(x, n))/factorial(n))

print(res)
print(cos(x))
