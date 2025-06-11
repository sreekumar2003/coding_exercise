#Vowels and consance
s = input("Enter the string")
v = ["a","e","i","o","u","A","E","I","O","U"]
vo = 0
con = 0
for i in s:
    if i in v:
        vo += 1
    else:
        con += 1
print(f'volwes:{vo}')
print(f'consants:{con}')
        
