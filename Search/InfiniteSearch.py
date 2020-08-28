# Search an element from infinite sized sorted array

def binary(arr, l, h, key):
    if l < h:
        mid = (l + h) / 2
        mid = int(mid)
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            return binary(arr, mid, h, key)
        return binary(arr, l, mid, key)
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8]
l = 0
h = 1
key = 0
while arr[h] < key:
    l = h
    h *= 2
print(binary(arr, l, h, key))
