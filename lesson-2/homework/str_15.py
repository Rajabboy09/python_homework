txt = input("Enter text :")
txt = txt.upper()
words = txt.split()

acronym = ''.join(word[0] for word in words)
print(acronym)