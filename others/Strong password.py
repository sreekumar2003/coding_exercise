i=0
while i==0:
    n=input("enter the password: ")
    
    if not any(w.isupper() for w in n ):
        print("There should atleast one upper Case")
        continue 
        
    if not any(w.islower() for w in n ):
        print("There should atleast one Lower Case")
        continue
    
    if not any(w.isdigit() for w in n ):
        print("There should atleast one digit ")
        continue
        
    if not any(w.isalpha() for w in n ):
        print("There should atleast one Alphabet")
        continue
    
    if not any(not w.isalnum() for w in n ):
        print("There should atleast one Special Character")
        continue
    
    i += 1
    
print(f'Your password {n} is Strong')
    
