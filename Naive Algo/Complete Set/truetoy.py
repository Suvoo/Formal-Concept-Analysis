# set representation to bit representation and then return answer

# to read input form file
a,arr= [],[]
start,end = 3,4
with open('Naive Algo\Input\Toycontext(bit)') as file:
    for line in file:
        line = line.strip()
        for c in line:
            if c != ' ':
                # print(int(c))
                a.append(int(c))
                # print(a)
        arr.append(a)
        a = []
# print(arr)

# modify the 2d array
for i in range(len(arr)):
    arr[i] = arr[i][1:]
    # print(arr[i])

# find and store Gr in a set s
s = set()
for st in range(start, end+1):
    for i in range(len(arr)):
        if st in arr[i]:
            s.add(i+1)
print('Gr is',s)

coun1,coun2 = 0,0
s1 = set()
for r in range(start):
    for i in range(len(arr)):
        if r in arr[i]:
            #print(r,i+1,arr[i])
            coun1+=1
            if i+1 in s:
                coun2+=1
                ans = r
                #print(r,i+1,arr[i])
    if coun1 == coun2 and coun1 !=0 and coun2 !=0:
        s1.add(ans)
    coun1,coun2 = 0,0
        
            
print('Attributes are',s1) #attributes

# to verify
'''s2 = set()
for atrans in s1:
    for i in range(len(arr)):
        if atrans in arr[i]:
            s2.add(i+1)
print('new gr is ',s2)

flag = 0
for i in s2:
    if i in s:
        print('sfb',i) #glitch
    else:
        print('bad')
        flag = 1
        break
print('verify ans is ',flag)'''


        