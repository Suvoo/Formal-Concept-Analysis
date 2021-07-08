threshold = 423089
theta = 846041

a,brr=[],[]
ac=''
with open('Thresholds\WebD\Approach 1 - FrontRear\webdocs_Support') as file:
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
front = 1
nxt = 0
for i in range(83): # do unitl elements start repeating
    begin = arr[nxt][0]
    to_append = arr[nxt][1]
    ans.append(to_append)

    for j in range(front,len(arr)): # minus lenght from rear
        sgr = sgr + arr[j][0]

        if(sgr + begin >= theta):
            front += len(ans)
            nxt = j
            break
        else:
            ans.append(arr[j][1])
    print(ans)
    ans = []
    sgr = 0