import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    revarr = arr[::-1]
    c = numpy.array(revarr,float)
    return c    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

'''
input
1 2 3 4 -8 -10
output
[-10.  -8.   4.   3.   2.   1.]
'''
