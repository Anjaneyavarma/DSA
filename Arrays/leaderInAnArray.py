# Leader in an Array

#method-1- O(n**2)
lst = [7,10,4,10,6,5,2]
length = len(lst)
for i in range(0, length):
    leader = True

    for j in range(i+1, length):
        if(lst[i] <= lst[j]):
            leader = False
            break;

    if(leader == True):
        print(lst[i], end=",")
#o/p = 10,6,5,2

print()
print("######")

#Method-2- O(n)

cur_lead = lst[length-1]
print(cur_lead, end=",")
for i in range(length-2,0,-1):
    if(cur_lead < lst[i]):
        cur_lead = lst[i]
        print(cur_lead, end = ",")

#o/p = 2,5,6,10
