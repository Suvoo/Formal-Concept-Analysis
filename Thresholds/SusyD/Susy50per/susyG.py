threshold = 929794
theta = 2500000
# 1 mil
# 3.75 mil
# 5 mil

a,brr=[],[]
ac=''
with open('Thresholds\SusyD\susy_support_att') as file:
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

begin = arr[16][0]
to_append = arr[16][1]

ans.append(to_append)

for i in range(len(arr)-146,-1,-1): # minus lenght from rear
    sgr = sgr + arr[i][0]

    if(sgr + begin >= theta):
        break
    else:
        ans.append(arr[i][1])
print(ans)
print(len(ans) - 1)

f = open('Thresholds\SusyD\grSusy.txt', 'a')
f.write(str(ans))
f.write(" ")

# [148, 146, 147, 148] LEFT