arr=[1,2,3,4,5,6,7,8]
x=int(input("Enter sum:"))
sum=0
count=0
for i in range(len(arr)):
    for j in range(len(arr)):
        sum=arr[i]+arr[j]
        if sum==x:
            count+=1
print("There are ",count," possible pairs.")