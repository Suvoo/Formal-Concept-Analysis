# To Find an algorithm for giving selected attributes in a formal concept analysis acc to given conditions
a,arr= [],[]
start,end = 3,5
with open('Naive Algo/test2.txt') as file:
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
s = set()
for st in range(start, end+1):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j == st - 1 and arr[i][j] == 1:
                s.add(i + 1)
            #if j == end - 1 and arr[i][j] == 1:
                #s.add(i + 1)
print(s) # Gr

s1 = set()
coun = 0
k = 0
ans = 0
for r in range(start):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j == r - 1 and arr[i][j] == 1:
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
print(s1) # attributes

