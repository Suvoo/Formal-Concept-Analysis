
grp_id =''
attr = []
with open('Visualization\Input\wdemo.txt') as file:
    for line in file:
        line = line.strip()
        if line[0] == '"':
            grp_id = line
        else:
            for i in range(len(line)):
                if line[i] == '.':
                    attr.append(float(line[i-1:]))
                    

# for 2 digit

start = int(grp_id[-5:-3])
end = int(grp_id[-2:])
gid = grp_id[1:-7]

per = 0.6
cou = 0

for i in attr:
    if i >=per:
        # print(i)
        cou += 1
print(cou)

f = open('Visualization/Output/webdocs(10-20).txt', 'a')
f.write(str(cou))
f.write(" ")



