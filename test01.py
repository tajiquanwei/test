
# for i in range( 1 , 5):
#     print ( i )

import math
import decimal

a =  3**2
print(int(a))

a = pow(3, 3, 4)
print(a)

a = 7654321.3456789
print(round(a, 0))      #7654321
print(round(a, -1))     #7654320
print(round(a, 1))      #7654321.3
print(round(a, 3))      #7654321.346

i = 123
print(bin(i))
print(hex(i))
print(oct(i))

print(math.pi)
print(math.hypot(7,24))

x = decimal.Decimal("123456789.9876543210123456789")
print(x)

print("QQ\nTT")

s = "This is a book"
print (s[:8] + 'not' + s[9:])

print(s.lower())
print(s.upper())



def print_x_times(msg,counts):
    i = 0
    while True:
        if i < counts:
            print(msg)
            i += 1    #沒有 i++
        else:
            break

print_x_times("XD",3)



