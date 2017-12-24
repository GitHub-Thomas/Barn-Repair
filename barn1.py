"""
ID:wzch_di3
TASK:barn1
LANG:PYTHON3
"""
fin = open("barn1.in","r")
fout = open("barn1.out","w")
message = fin.readline()
index = message.find(" ")
m = int(message[0:index])
index2 = message.find(" ",index+1)
s = int(message[index+1:index2])
c = int(message[index2+1:])
if (m >= c):
    fout.write(str(c)+'\n')
    fin.close()
    fout.close()
    exit(0)
barn = []
for i in range(0,s+5):
    barn.append(0)
for i in fin.readlines():
    barn[int(i)] = 1
for i in range(0,s):
    if (barn[i] == 1):
        l = i
        break
for i in range(0,s+5):
    if (barn[s-i] == 1):
        r = s-i
        break
space = []
sum = 0
num = 0
for i in range(l,r+1):
    if (barn[i] == 0):
        sum = sum + 1
    else:
        space.append(sum)
        num = num + 1
        sum = 0
for i in range(0,num):
    for j in range(i+1,num):
        if (space[i] < space[j]):
            temp = space[j]
            space[j] = space[i]
            space[i] = temp
total = 0
for i in range(0,m-1):
    total = total + space[i]
ans = m - total - (l-1) - (m - r)
fout.write(str(ans)+'\n')
fin.close()
fout.close()
