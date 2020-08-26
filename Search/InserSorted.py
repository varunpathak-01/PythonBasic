arr = [1, 2, 3, 5, 6, 7, 8, 9]
arr.sort()
arr.append(0)
temp=0
ele = int(input("Enter element :"))
for i in range(len(arr)):
    if arr[i]>ele:
        break
if i!=len(arr):
    j=i
    for i in range(len(arr)-1,j,-1):
        arr[i]=arr[i-1]
arr[j]=ele
print(arr)