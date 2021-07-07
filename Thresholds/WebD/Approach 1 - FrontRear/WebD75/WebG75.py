threshold = 423089
theta = 1269267

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
rear = 1

for i in range(51): # do unitl elements start repeating
    begin = arr[i][0]
    to_append = arr[i][1]
    ans.append(to_append)

    for j in range(len(arr) - rear,-1,-1): # minus lenght from rear
        sgr = sgr + arr[j][0]

        if(sgr + begin >= theta):
            rear += len(ans) - 1
            break
        else:
            ans.append(arr[j][1])
    print(ans)
    ans = []
    sgr = 0

# [183, 184, 185, 186]