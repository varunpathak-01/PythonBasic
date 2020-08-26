def findCommon(a1, a2, a3, n1, n2, n3):
    i = 0
    j = 0
    k = 0
    while i < n1 and j < n2 and k < n3:
        if a1[i] == a2[j] and a2[j] == a3[k]:
            print(a1[i])
            i += 1
            j += 1
            k += 1
        elif a1[i] < a2[j]:
            i += 1
        elif a2[j] < a3[k]:
            j += 1
        else:
            k += 1


a1 = [1, 2, 3, 4, 5, 6, 7]
a2 = [1, 3, 7, 10, 13, 17]
a3 = [1, 3, 7, 11, 15, 19]
n1 = len(a1)
n2 = len(a2)
n3 = len(a3)
print("Common elements are", findCommon(a1, a2, a3, n1, n2, n3))