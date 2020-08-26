arr = [1, 2, 3, 4, 5, 6, 7, 1]
ele = int(input("Enter element you want to search :"))
counter = 0
for x in arr:
    if x == ele:
        counter += 1
if counter > 0:
    print("Element occurred ", counter, " times")
else:
    print("Element not present")
