

a = 1
b = 1
fibo = 0


print("enter your number")
number_user = int(input())
print(a)
print(b)

for i in range(2, number_user):
    c = a + b
    print(c)
    a = b
    b = c