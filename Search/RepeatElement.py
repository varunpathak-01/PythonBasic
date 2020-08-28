# First n-1 natural numbers where one element is repeated.Find that one.

def naturalSum(arr):
    n=len(arr)
    return sum(arr) - (n*(n-1)/2)

arr=[1, 2, 3, 4, 5, 3]
print(naturalSum(arr))