theta = 1692356

a,brr=[],[]
ac=''

path='Thresholds\WebD\Approach 1 - FrontRear\WebD100\websumper100'

with open(path) as file:
    for line in file:
        line = line.strip()
        line = line + ' '

        if(line[0] != 's'):
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

res = []
for i in range(len(brr)):
    diffs = brr[i][1]
    ans = diffs/theta

    res.append(ans * 100)

# print(res)
print('Theta is ',theta)

print('Mininimum is', min(res))
print('Maximum is', max(res))
f = sum(res)/len(res)
print('Average is', f)

