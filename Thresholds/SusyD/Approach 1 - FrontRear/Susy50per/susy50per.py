theta = 2500000
a,arr= [],[]

with open('C:\\Users\\91865\\Desktop\\SusyInput') as file:# C:\\Users\\91865\\Desktop\\SusyInput
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

Gr1 = [149, 143, 144, 145] 

countObj = 0
s = set()
for i in Gr1:
    for j in range(len(arr)):
        if i in arr[j]:
            s.add(j + 1) # adding objects
            #countObj+=1
    # print(i, countObj)
    # countObj = 0
#print(s)
print(len(s))

# gr1obj = 1526401
# print(theta - 1526401)