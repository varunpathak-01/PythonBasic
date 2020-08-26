def bs(arr,low,high,ele):
    if high<low:
        retun -1
    mid=(low+high)/2
    if ele == arr[int(mid)]:
        return mid
    if(ele>arr[int(mid)]):
        return bs(arr,(mid+1),high,ele)
        return bs(arr,low,(mid-1),ele)


arr=[12,124,1123,213,123,123,12312,123,12313,123,52314,35,132]
arr.sort()
low=0
high=len(arr)
ele=12312
print("Index is:",int(bs(arr,low,high,ele)))


print(arr)