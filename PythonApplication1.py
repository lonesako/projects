with open("file.txt","r") as f: #anoigma txt
    data = f.read().split()
f.close()

print(data)
good = list("bdghjlmnpqstvwxzBDGHJLMNPQSTVWXZ") #kala symfwna
bad = list("fckrFCKR") #kaka symfwna

for word in data:
    goodss = sum(word.count(gd) for gd in good) #pairnoume to sunolo twn kalwn
    badss = sum(word.count(bd) for bd in bad) #antistoixa twn kakwn
    if (badss>goodss): #ta sygkrinoume kai vgazoyme apotelesma
        print('Κακη λεξη', word)
    else :
        print("Καλη λεξη" , word)
