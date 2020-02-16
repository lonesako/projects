s = input('πληκτρολογηστε μια λεξη :') #to string
b = ''.join(str(ord(c)) for c in s) #me to ord(c) ta kanoume se ascii kai me to join ta enwnoume
print ("η λεξη που γραψατε σε ascii :",int(b)) #ektypwsh tou arithou se ascii

if (int(b)> 1): 
      
    # epanalhpsi apo 2 ews ascii/2  
    for i in range(2, int(b)//2):    
       # ean o ascii arithos diaireitai apo opoiodhpote i metaksi 2 kai ascii/2 tote den einai prwtos   
       if (int(b) % i) == 0: 
        print("το",int(b), "δεν ειναι πρωτος") 
        break
       #ean den diaireitai me kanenan arithmo apo 2 ews ascii/2 tote einai prwtos
       else: 
        print("το",int(b), "ειναι πρωτος") 
        break
else: 
    print("το",int(b), "δεν ειναι πρωτος") 
