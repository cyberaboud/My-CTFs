print("Hey there and welcome in our CTF : ")
print("Can you give me the flag please ?")

flag = str(input())

compare = ""
for i in range(len(flag)):
    compare = compare + chr(ord(flag[i]) + 1)

if (compare == "FOJU|qzu`jt`gvvo~"):
    print("Congratulations, you can validate with that flag !")
else:
    print("Oops, you gave me the wrong flag, try again?")