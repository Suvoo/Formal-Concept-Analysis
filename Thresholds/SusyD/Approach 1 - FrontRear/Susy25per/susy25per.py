attr = [[164, 5, 4, 3, 2, 1, 11, 10, 9, 8, 7, 6, 12, 14, 13, 15, 18, 16, 17, 19, 20, 22, 21, 25, 24, 
23, 28, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76],
[163, 77, 78, 79, 80, 81],
[162, 82, 83, 84],
[161, 85, 86],
[160, 87, 88],
[159, 89],
[158, 90],
[157, 91],
[156, 92],
[155, 93],
[154, 94],
[153, 95],
[152, 96],
[151, 97],
[150, 98],
[149, 99],
[148, 100],
[147, 101],
[146, 102],
[145, 103],
[144, 104],
[143, 105],
[142, 106],
[141, 107],
[140, 108],
[139, 109],
[138, 110],
[137, 111],
[136, 112],
[135, 113],
[134, 114],
[133, 115],
[132, 116],
[131, 117],
[130, 118],
[129, 119],
[128, 120],
[127, 121],
[126, 122],
[125, 123]]

# print(attr)
a,arr= [],[]
theta = 1000000

with open('C:\\Users\\91865\\Desktop\\SusyInput') as file:# C:\\Users\\91865\\Desktop\\SusyInput
    for line in file:
        line = line.strip()
        new_line = line.replace('\t', ' ')
        a = new_line.split(' ')
        a = [int(i) for i in a]
        arr.append(a)
        a = []
# print(arr)

# alter the array to store only attributes
for i in range(len(arr)):
    arr[i] = arr[i][1:]
    # print(arr[i])

countObj = 0
s = set()

for i in attr:
    for k in i:
        for j in range(len(arr)):
            if k in arr[j]:
                s.add(j + 1) # adding objects
    print(len(s),theta - len(s))
    s.clear()