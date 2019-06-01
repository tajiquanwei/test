from random import randint

list = {1,2,3,4,5,6,7,8,9,0}

ans = ''
randint(0, 9)
while (len(ans) < 4):
    a = randint(0, 9)
    if(a in list):
        ans = ans + str(a)
        list.remove(a)
print (ans)

for i in range (0,4):
    print (ans[i])

temp = ''
while temp != ans:
    temp = input("input:")
    countA = 0
    countB = 0
    for i in range(0,4):
        for j in range(0,4):
            if ans[i] == temp[j]:
                if i == j:
                    countA = countA + 1
                else:
                    countB = countB + 1

    print(temp + '    ' + str(countA) + 'A' + str(countB) + 'B')