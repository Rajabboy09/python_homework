txt = input("Enter text :")
word_remove = input("Removable word : ")
word_add = input("Word to be addes : ")
if word_remove not in txt.split():
    print("Please check removable word")
else:
    txt = txt.replace(word_remove, word_add)
    print("Modified sentence:", txt)