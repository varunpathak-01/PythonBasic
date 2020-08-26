arr=[1, 2, 3, 4, 5]
arr.sort()

ele=int(input("Enter element to delete:"))
for i in range(len(arr)):
    if arr[i]==ele:
        break
for i in range(i,len(arr)-1):
    arr[i]=arr[i+1]

arr=arr[:-1]
print(arr)