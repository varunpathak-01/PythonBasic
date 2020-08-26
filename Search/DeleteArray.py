arr=[1,2,3,4,5,6,7,8]
dele=int(input("Enter element to delete :"))
for i in range(len(arr)):
    if arr[i]==dele:
        break
for i in range(i,len(arr)-1):
    if i!=len(arr):
        arr[i]=arr[i+1]
arr=arr[:-1]
print(arr)