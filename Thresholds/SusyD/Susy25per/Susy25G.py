threshold = 929794
theta = 1000000

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

arr = []
tindex = 15
for i in range(len(brr)):
    if i>= tindex:
        arr.append(brr[i])
# print(arr)

sgr = 0
ans = []

begin = arr[8][0]
to_append = arr[8][1]

ans.append(to_append)

for i in range(len(arr)-92,-1,-1): # minus lenght from rear
    sgr = sgr + arr[i][0]

    if(sgr + begin >= theta):
        break
    else:
        ans.append(arr[i][1])
print(ans)
print(len(ans) - 1)

f = open('Thresholds\SusyD\Susy25per\grSusy25.txt', 'a')
f.write(str(ans))
f.write(" ")
        