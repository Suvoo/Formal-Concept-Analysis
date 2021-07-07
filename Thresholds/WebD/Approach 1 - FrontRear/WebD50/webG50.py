threshold = 423089
theta = 846041 #50
# 423089
# 1269267
# 1692356
a,brr=[],[]
ac=''
with open('Thresholds\WebD\webdocs_Support') as file:
    for line in file:
        line = line.strip()
        line = line + ' '

        if(line[0] != '"'):
            for c in line:
                if c != ' ':
                    ac = ac + c
                else:
                    a.append(int(ac))
                    # print(ac)
                    ac=''
            brr.append(a)
            a=[]
    

# print(brr)
# "Supp of the Att" "Att ID"

# tindex is if arr[i][0] == threshold - unique for all
# for i in range(len(brr)):
#     if brr[i][0] == threshold:
#         tindex = i
arr = []
tindex = 28
for i in range(len(brr)):
    if i >= tindex:
        arr.append(brr[i])
# print(arr)

sgr = 0
ans = []

begin = arr[77][0]
to_append = arr[77][1]

ans.append(to_append)

for i in range(len(arr)-155,-1,-1): # minus lenght from rear
    sgr = sgr + arr[i][0]
    # print(sgr)
    if(sgr + begin >= theta):
        break
    else:
        ans.append(arr[i][1])
print(ans)

f = open('Thresholds\WebD\grWeb.txt', 'a')
f.write(str(ans))
f.write(" ")
