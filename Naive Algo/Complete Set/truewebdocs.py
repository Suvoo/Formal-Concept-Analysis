# set representation to bit representation and then return answer

a,arr= [],[]
start,end = 233,233
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
    # print(coun1,coun2)
    if coun1 == coun2 and coun1 !=0 and coun2 !=0:
        # print('new',coun1,coun2)
        s1.append(ans)
    coun1,coun2 = 0,0
print('Attributes are',s1) #attributes

# For Similarity,:
s1dash = []
for i in range(1,start):
    s1dash.append(i)
# print(s1dash)

ansDict = {}
grDash = []
for atrans in s1dash:
    for i in range(len(arr)):
        if atrans in arr[i]:
            grDash.append(i+1)
    # print(grDash)
    num = []
    for gtrans in grDash:
        if gtrans in s:
            num.append(gtrans)
    # print(len(num)/len(grDash))
    ansDict[atrans] = len(num)/len(grDash)
    grDash = []

# print(ansDict)
for i in ansDict:
    print(i,ansDict[i])

# to write to file
# f = open('Naive Algo\Output\Finop1', 'a')
# f.write(str(ansDict))