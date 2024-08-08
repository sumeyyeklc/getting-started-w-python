x =2 
while x<10:
    print(x)
    x+= 1
print("x = ",x)

i =1
while True:
    print(i)
    i+=1
    if i == 1001:
        break

n = int(input("Kaç tane Fibonacci sayısı görmek istersiniz? "))

a, b = 0, 1
print(a, b, end=" ")

for _ in range(2, n):
    a, b = b, a + b
    print(b, end=" ")
