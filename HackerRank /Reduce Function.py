from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x,y:x*y,fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

'''
input
3
1 2
3 4
10 6

output
5 8

explanation
Required product is 1/2 * 3/4 * 10/6 = 5/8



'''
