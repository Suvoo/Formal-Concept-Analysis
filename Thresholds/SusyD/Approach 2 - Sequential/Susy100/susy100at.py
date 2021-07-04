threshold = 929794
theta = 5000000

a,brr=[],[]
ac=''
with open('Thresholds\SusyD\Approach 1 - FrontRear\susy_support_att') as file:
    for line in file:
        line = line.strip()
        line = line + '\t'

        if(line[0] != 'S'):
            for c in line:
                if(c != '\t'):
                    ac = ac + c
                else:
                    a.append(int(ac))
                    # print(ac)
                    ac=''
            brr.append(a)
            a=[]
# print(brr)
brr.reverse()

# "Supp of the Att" "Att ID"

# tindex is if arr[i][0] == threshold - unique for all
# for i in range(len(brr)):
#     if brr[i][0] == threshold:
#         tindex = i
arr = []
tindex = 15
for i in range(len(brr)):
    if i>= tindex:
        arr.append(brr[i])
# print(arr)

sgr = 0
ans = []
front = 1
nxt = 0
for i in range(8): # do unitl elements start repeating
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

