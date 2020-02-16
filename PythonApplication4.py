#αριθμοι απο 1 εως 8
import itertools
#παιρνουμε την λιστα απο το text1.py
from text1 import unq

#ελεγχος για μοναδικοτητα καθε pick
while True:
    userspick1 = input("name your 1st pick:")
    userspick1=int(userspick1)
    if (userspick1>0 and userspick1<9):
        break
while True:
    userspick2 = input("name your 2nd pick:")
    userspick2=int(userspick2)
    if (userspick2>0 and userspick2<9 and (userspick1<userspick2 or userspick1>userspick2) ):
        break
while True:
    userspick3 = input("name your 3rd pick:")
    userspick3=int(userspick3)
    if (userspick3>0 and userspick3<9 and (userspick1<userspick3 or userspick1>userspick3) and (userspick2<userspick3 or userspick2>userspick3) ):
        break
while True:
    userspick4 = input("name your 4th pick:")
    userspick4=int(userspick4)
    if (userspick4>0 and userspick4<9 and (userspick1<userspick4 or userspick1>userspick4) and (userspick2<userspick4 or userspick2>userspick4) and (userspick3<userspick4 or userspick3>userspick4) ):
        break
while True:
    userspick5 = input("name your 5th pick:")
    userspick5=int(userspick5)
    if (userspick5>0 and userspick5<9 and (userspick1<userspick5 or userspick1>userspick5) and (userspick2<userspick5 or userspick2>userspick5) and (userspick3<userspick5 or userspick3>userspick5) and (userspick4<userspick5 or userspick4>userspick5)):
        break
while True:
    userspick6 = input("name your 6th pick:")
    userspick6=int(userspick6)
    if (userspick6>0 and userspick6<9 and (userspick1<userspick6 or userspick1>userspick6) and (userspick2<userspick6 or userspick2>userspick6) and (userspick3<userspick6 or userspick3>userspick6) and (userspick4<userspick6 or userspick4>userspick6) and (userspick5<userspick6 or userspick5>userspick6)) :
        break
picks = [userspick1,userspick2,userspick3,userspick4,userspick5,userspick6]
print("your picks are:",picks)


#δημιουργουμε λιστα με επιλογες
f1 = list(itertools.combinations(picks, 4))
unqchoices = set(f1)


import collections 
flag = 0 
  
# εμφωλευμενη for για να εξεταστουν ολες οι περιπτωσεις απο τις 2 λιστες

for elem in unq: 
    for elem2 in unqchoices:
         if collections.Counter(elem) == collections.Counter(elem2) : 
            flag = 1   
            print ("selected picks available",elem2)
            break
    if (flag==1): 
        break
# ελεγχος αν υπαρχει διαθεσιμη 4αδα     
if flag == 0: 
    print("no available picks") 


