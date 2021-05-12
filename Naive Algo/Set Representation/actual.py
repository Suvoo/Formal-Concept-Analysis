# set representation to bit representation and then return answer

a,arr,temp= [],[],''
start,end = 90,91
with open('Naive Algo\Set Representation\mushroomContext') as file:
    for line in file:
        line = line.strip()
        # print(line)
        new_line = line.replace('\t', ' ')
        # print(new_line)
        a = new_line.split(' ')
        a = [int(i) for i in a]
        arr.append(a)
        a = []
# print(arr)

rows= arr[-1][0]
cols=0
#print(arr[-1][0])
for i in range(len(arr)):
    #print(arr[i][1:])
    cols = max(arr[i][-1],cols)
    arr[i] = arr[i][1:]
#print(arr)
#print(rows,cols)

brr = [[0 for i in range(cols)] for j in range(rows)]
#print(brr)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        # t = arr[i][j]
        # print(t)
        # print(i,arr[i][j]-1)
        brr[i][arr[i][j] - 1] = 1
    # print(brr[i])

s = set()
for st in range(start, end+1):
    for i in range(len(brr)):
        for j in range(len(brr[i])):
            if j == st - 1 and brr[i][j] == 1:
                s.add(i + 1)
            #if j == end - 1 and arr[i][j] == 1:
                #s.add(i + 1)
# print(s) # Gr

s1 = set()
coun = 0
k = 0
ans = 0
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
print(s1) #attributes

f = open('Naive Algo\Set Representation\output', 'a')
f.write('For ')
f.write(str(start))
f.write(' and ')
f.write(str(end))
f.write('\n\n')
f.write('Gr is : \n\n')
f.write(str(s))
f.write('\n\n')
f.write('The final attribute set is : \n\n')
f.write(str(s1))
f.close()