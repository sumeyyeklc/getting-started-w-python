message= "hello world"
print(message.startswith("m"))
print(message[0]) #index numbers start from zero.
print(message[2:5]) #prints second index to fifth index. (does not include the fifth index.)
print(message[:4]) #prints from first index(zero) to fourth index.
print(message[3:]) #prints from third index to last index
print(message[::2])#prints in twos
print(len(message)) #counts the characters in the word
print(message.upper())
print(message.lower())
message = message.capitalize() 
print(message) 
print(message.count("l")) #counts the character written in the text 
print(message.find("world")) #prints the index number of the word written
 #find command is suitable for strings only.
print(message.find("python"))

message_1= "Hello World"
print(message_1)
new_message= message_1.replace("World", "Mars") #omits the firs word and places the second word in first words place
print(new_message)

greeting="Hello"
name= "Sümeyye"
saying_hello= greeting+ "," + name
print(saying_hello)
saying_hello2 = f"{greeting}, {name.upper()}.  Welcome!"
print(saying_hello2)
print(name.__add__("e"))
name= "Sümeyye"
print(name*3)
print((name+ " ") *3)

