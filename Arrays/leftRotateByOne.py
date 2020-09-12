#left Rotate an array by one values

lst = [1,2,3,4,5]

length = len(lst)
temp = lst[0]
for i in range(1, length):
    lst[i-1] = lst[i]

lst[length-1] = temp
print(lst)

#o/p = [2,3,4,5,1]
