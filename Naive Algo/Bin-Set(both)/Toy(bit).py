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

# extract the size of the matrix of which binary representation had to be made
rows= arr[-1][0]
cols=0
#print(arr[-1][0])
for i in range(len(arr)):
    #print(arr[i][1:])
    cols = max(arr[i][-1],cols)
    arr[i] = arr[i][1:]
# print(arr)
# print(rows,cols)

# store the binary representation of matrix in brr
brr = [[0 for i in range(cols)] for j in range(rows)]
# print(brr)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        # t = arr[i][j]
        # print(t)
        # print(i,arr[i][j]-1)
        brr[i][arr[i][j] - 1] = 1
    # print(brr[i])
#print(brr) # bit representation now their

# find and store Gr in a set s
s = set()
for st in range(start, end+1):
    for i in range(len(brr)):
        for j in range(len(brr[i])):
            if j == st - 1 and brr[i][j] == 1:
                s.add(i + 1)
            #if j == end - 1 and arr[i][j] == 1:
                #s.add(i + 1)
print('Gr is',s) # Gr

s1 = set()
coun = 0
k = 0
ans = 0
# store the final list of attributes in a set s1
for r in range(start):
    for i in range(len(brr)):
        for j in range(len(brr[i])):
            if j == r - 1 and brr[i][j] == 1:
                #print(r,i+1)
                # k = 0
                coun += 1
                if i+1 in s:
                    k+=1
                ans = j+1
    # print(coun,k)
    if coun == k and k!=0 and coun !=0:
        s1.add(ans)
    coun = 0
    k = 0
print('Attributes are',s1) #attributes