def binarysearch_recursive(A, key, l, r):
    if l > r:
        return -1
    else:
        mid = l + (r - l)// 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binarysearch_recursive(A,key,l,mid-1)
        elif key > A[mid]:
            return binarysearch_recursive(A,key,mid+1,r)

A = [15, 21, 47, 84, 96]
found = binarysearch_recursive(A,21,0,4)
print('Result to find binarysearch:', found)


