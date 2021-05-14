# set representation to bit representation and then return answer

# to read input form file
a,arr= [],[]
start,end = 3,4
with open('Naive Algo\Set Representation\Toycontext(bit)') as file:
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

s1 = set()
for r in range(start):
    for i in range(len(arr)):
        if r in arr[i]:
            #print(r,i+1,arr[i])
            if i+1 in s:
                #print(r,i+1,arr[i])
                s1.add(r)
            else:
                #print('v2',r,i+1,arr[i]) 
                if r in s1:
                    s1.remove(r)       
print('Attributes are',s1) #attributes