result= 1
for i in range(10):
    print(result)
    result *= 2

print(result)

list_num =range(100)
for numbers in list_num :
    if numbers % 2 != 0:
        continue
    if numbers ==50:
        break
    print(numbers)