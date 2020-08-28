# Find that one element that occurred once while all other twice.
# XOR of all array elements gives us the number with a single occurrence. The idea is based on the following two facts.
# a) XOR of a number with itself is 0.
# b) XOR of a number with 0 is number itself.

def xor(arr):
    n = len(arr)
    result = arr[0]
    for i in range(1, n):
        result = result ^ arr[i]
    return result


arr = [1, 2, 1, 3, 4, 3, 4]

print(xor(arr))
