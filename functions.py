def greeting(name):
    print("Hello " + name)
greeting("everybody")

def app_calculation(number):
    total = sum(number)
    count = len(number)
    app = total / count
    print(f"app : {app}")

app_calculation([1,2,3,4,5])

def upper_Letter(text):
    return text.upper()
text = input("Write something: ")
print(upper_Letter(text))