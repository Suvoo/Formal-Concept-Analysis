
grp_id =''
attr = []
with open('Visualization\Input\wdem100-35.txt') as file: #reading the info from input file which has
    for line in file:
        line = line.strip()
        if line[0] == '"':
            grp_id = line
        else:
            for i in range(len(line)):
                if line[i] == '.':
                    attr.append(float(line[i-1:]))
                    
# print(attr)

per = 0.7 # threshold
cou = 0

for i in attr: # stores all similarity of attributs less than start
    if i >=per:
        #print(i)
        cou += 1 # counts
print(cou)

f = open('Visualization/Output/webdocs(100-135).txt', 'a')
f.write(str(cou))
f.write(" ")