# set representation to bit representation and then return answer

a,arr= [],[]
start,end = 90,91
with open('Naive Algo\Input\mushroomContext') as file:
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
    # print(arr[i])

# find and store Gr in a set s
s = set()
for st in range(start, end+1):
    for i in range(len(arr)):
        if st in arr[i]:
            s.add(i+1)
# print('Gr is',s)

s1 = []
coun1,coun2 = 0,0
for r in range(start):
    for i in range(len(arr)):
        if r in arr[i]:
            coun1+=1
            if i+1 in s:
                coun2+=1
                ans = r
    if coun1 == coun2 and coun1 !=0 and coun2 !=0:
        s1.append(ans)
    coun1,coun2 = 0,0
print('Attributes are',s1) #attributes

# VERIFICATION
s2 = set()
for atrans in s1:
    for i in range(len(arr)):
        if atrans in arr[i]:
            s2.add(i+1)
# print('new gr is ',s2)
flag = 0
for i in s2:
    if i in s: # is a subset
        pass
    else: # not a subset
        flag = 1
        break
print('verify ans is ',flag) #if 0, then ANSWER is verified

# to write to file
f = open('Naive Algo\Output\Finop', 'a')
f.write('For ')
f.write(str(start))
f.write(' and ')
f.write(str(end))
f.write('\n')
f.write(str(s1))
f.close()
