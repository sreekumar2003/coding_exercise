s1 = input("Enter the  string")
s2 = input("Enter the string")

if len(s1) != len(s2):
    print("false")
else:
    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1 == s2:
        print("true")
    else:
        print("false")

'''
Enter the  stringqwert
Enter the stringtrewa
false
'''
