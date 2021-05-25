# set representation to bit representation and then return answer

a,arr= [],[]
start,end = 10,20
with open('C:\\Users\\91865\\Desktop\\webdocs10') as file:
    for line in file:
        line = line.strip()
        new_line = line.replace('\t', ' ')
        a = new_line.split(' ')
        a = [int(i) for i in a]
        arr.append(a)
        a = []
# print(arr)

# alter the array to store only attributes
for i in range(len(arr)):
    arr[i] = arr[i][1:]
    #print(arr[i])

# find and store Gr in a set s
s = set()
for st in range(start, end+1):
    for i in range(len(arr)):
        if st in arr[i]:
            s.add(i+1)
# print('Gr is',s)
ans = 0
s1 = []
coun1,coun2 = 0,0
for r in range(start):
    for i in range(len(arr)):
        if r in arr[i]:
            coun1+=1
            if i+1 in s:
                coun2+=1
                ans = r
                # print('im here')
    print(coun1,coun2)
    if coun1 == coun2 and coun1 !=0 and coun2 !=0:
        print('new',coun1,coun2)
        s1.append(ans)
    coun1,coun2 = 0,0
print('Attributes are',s1) #attributes
