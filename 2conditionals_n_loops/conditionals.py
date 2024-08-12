#if True:
    #print("True")
    #print("Still inside the if block")

num1= 7
num2=88
if not num1 == num2:
    print(f"{num1} is not equals to {num2}")
else:
    print(f"{num1} = {num2}")

user= "admin"
logged_in= False
if user == "admin" and logged_in:
    print("Admin Page")
else:
    print("not admin page")

x=3
y=2
z=8
if x<z or y>z:
    print("True")
else:
    print("False")

num= [1,2,5,8,3,7]
k =9
if k in num:
    print(f"{k} is in the list")
else:
    print(f"{k} is not in the list.")


a = [1, 2, 3]
b = [1, 2, 3]
a = b
print(a is b)
print(id(a))
print(id(b))