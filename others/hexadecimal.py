def hexdeci(a,b):
    
    int1 = int(a,16)
    int2 = int(b,16)
    
    if int1 == int2:
        return "SAME"
    else:
        diff = int1 - int2
        return f"Not same: {hex(diff)} int : {diff}"
        
print(hexdeci("7D","19"))



"""
Not same: 0x64 int : 100
"""
