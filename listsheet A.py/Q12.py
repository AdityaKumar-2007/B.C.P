#a^0=a
#a^a=0

arr = [2,3,4,5,6,7,8,]
ans=0
for i in range(len(arr)):
    ans = ans^arr[i]
print(ans)