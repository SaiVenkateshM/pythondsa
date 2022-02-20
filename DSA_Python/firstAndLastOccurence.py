def firstOccurence(A, n, key):
    s = 0
    e = n - 1
    mid = s + (e - s) // 2
    ans = -1
    while s <= e:
        if A[mid] == key:
            ans = mid
            e = mid - 1

        elif key > A[mid]:
            s = mid + 1

        else:
            e = mid - 1

        mid = s + (e - s) // 2
    return ans


def lastOccurance(A, n, key):
    s = 0
    e = n - 1
    mid = s + (e - s) // 2
    ans = -1
    while s <= e:
        if A[mid] == key:
            ans = mid
            s = mid + 1

        elif key > A[mid]:
            s = mid + 1

        elif key < A[mid]:
            e = mid - 1

        mid = s + (e - s) // 2
    return ans


A = [1,2,2,2,2,2,4]
first = firstOccurence(A,7,2)
second = lastOccurance(A,7,2)
print('First occurance index :', first)
print('Last Occurance Index :', second)
