#left Rotate an array by D values

lst = [1,2,3,4,5]

#Method-1- O(n**2)
d = int(input())
length = len(lst)
#if d is greater than the length of an array then d = len - 1
if(d>length):
    d = d - length
for i in range(0,d):
    temp=lst[0]
    for j in range(1, length):
        lst[j-1] = lst[j]

    lst[length-1]=temp

print(lst)
#if d = 2
#o/p = [3,4,5,1,2]


#Method-2- O(n+d)
if(d>length):
    d = d - length
s = list(range(d))
for i in range(0,d):
    s[i]=lst[i]
    
for j in range(d, length):
    lst[j-d]=lst[j]
    
for k in range(0,d):
        lst[length-d+k] = s[k]

print(lst)

#o/p = [5,1,2,3,4]
