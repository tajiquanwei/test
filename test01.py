
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


for m in range(1,10):
    for n in range(1,10):
        ans = m * n
        if n == 9:
            print(m , ' * ' , n , ' = ' , str(ans).rjust(2) , ' ')
        else:
            print(m, ' * ', n, ' = ', str(ans).rjust(2), ' ', end="")

#tuple  內容無法修改   要修改請用list
t = "a","bb","cc",1 ,2,3
print (t)
print (t[1])
print (t.index("cc"))
print(t[:2])

if "a" in t:
    print ('a' + ' is in the tuple t')


#list

l = ["a","bb","ccc",1,2,3,4,5]
for i in l:
    print(i)

l.reverse()
for i in l:
    print(i)


lst = []
for i in range(1,10):
    lst.append(i)

for i in lst:
    print(i)

code = []
for sex in 'MF':
    for size in 'SMLX':
        for color in 'RWBG':
            code.append(sex+size+color)

cnt = 0
for i in code:
    cnt = cnt + 1
    print(cnt , ': ' , i)

#map   dictionary

nato = {'A':'alpha','B':'bravo','c':'charlie'}
print(nato.get('A'))
print(nato.keys())
print(nato.values())
nato.__setitem__('c','delta')
print(nato.keys())
print(nato.values())

for i,j in enumerate(nato,2):
    print(i)
    print(j)
    print(nato.get(j))

# try except finally
try:
    print(t[100])
    print('try')
except Exception:
    print('exception  happened !!!!!')
    print(Exception)
finally:
    print('finally')


class QqException(Exception):pass
try:
    print('try')
    word = 'QQ1'
    if word.__contains__('QQ'):
        raise QqException()
    else:
        print('word doesn\'t contain QQ' )
except QqException:
    print('word contains QQ')
finally:
    print('finally')

# read write file
text = 'This is for reading and writing file.'
my_test_file = open('testFile.txt','w')  # w for write
my_test_file.write(text)
my_test_file.close()

append_text = '\nappend text test'
my_test_file = open('testFile.txt','a')    # a for append
my_test_file.write(append_text)
my_test_file.close()

file = open('testFile.txt','r')   # r for read
content = file.read()
print(content)

