attr = [[164, 163, 162, 161],
[160, 159, 158, 157, 156],
[155, 154, 153, 152, 151],
[150, 149, 148, 147, 146, 145],
[144, 143, 142, 141, 140, 139, 138],
[137, 136, 135, 134, 133, 132, 131],
[130, 129, 128, 127, 126, 125, 124],
[123, 122, 121, 120, 119, 118, 117],
[116, 115, 114, 113, 112, 111, 110, 109],
[108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97],
[96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 27, 26, 28, 23, 24, 25, 21, 22, 20, 19, 17, 16, 18, 15, 13, 14, 12, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5]]

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
