# Having Max Difference in an Array

#O(n**2)
lst = [2,3,10,6,4,8,1]
length = len(lst)
res = lst[1]-lst[0]
for i in range(0, length):
    for j in range(i+1, length):
        res = max(res,lst[j] - lst[i])

print(res)

#o/p = 8
            

