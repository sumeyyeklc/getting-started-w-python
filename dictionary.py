book_info = {
    "Title": "1983",
    "Author": "George Orwell",
    "Type": "Dystopian"
}
print(book_info)
book_info.update({"Title":"1984"})
print(book_info)
book_info["Publication year"] = "1949" 
#adds new "key" and "value" to the dictionary

del book_info["Publication year"]
print(book_info)

print(book_info.keys())
print(book_info.values())
print(book_info.items())

#for a in book_info:    
    #print(a)

#for a in book_info:
    #print(book_info[a])

#for a in book_info.items():
    #print(a)

#for k,v in book_info.items():
    #print(k.v)

print(book_info.get("Publication year","Error"))