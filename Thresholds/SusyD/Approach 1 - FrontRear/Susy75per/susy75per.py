attr = [[164, 5, 4, 3, 2, 1, 11, 10, 9, 8, 7, 6, 12, 14, 13, 15, 18, 16, 17, 19, 20, 22, 21, 25, 24, 23, 28, 26, 27, 
29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98],
[163, 99, 100, 101, 102, 103, 104, 105, 106, 107],
[162, 108, 109, 110, 111, 112, 113],
[161, 114, 115, 116, 117, 118],
[160, 119, 120, 121, 122, 123],
[159, 124, 125, 126, 127, 128, 129],
[158, 130, 131, 132, 133, 134, 135],
[157, 136, 137, 138, 139, 140, 141],
[156, 142, 143, 144, 145, 146],
[155, 147, 148, 149, 150, 151],
]
# print(attr)
a,arr= [],[]
theta = 3750000

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