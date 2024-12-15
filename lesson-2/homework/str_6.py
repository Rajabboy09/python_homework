txt = input("Enter text :")
word = input("Word to check :")
if word in txt.split():
    print("Yes")
else:
    print("No")