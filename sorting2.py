# mergesort and quicksort as well as a modified quicksort
import random

def main():

    B = CreateRandomList(10)
    C = B.copy()
    C.sort()
    mergesort(B)
    if C != B:
        print("Error in mergesort")
    else:
        print(f"Mergesort used {B} copy of Mergesort {C}")
        
    D = CreateRandomList(10)
    E = D.copy()
    E.sort()
    quicksort(D)
    if E != D:
        print("Error in quicksort")
    else:
        print(f"Quicksort used {D} copy of Quicksort {E}")
        
    R = CreateRandomList(10)
    W = R.copy()
    W.sort()
    modquicksort(R)
    if R != W:
        print("Error in modquicksort")
    else:
        print(f"modquicksort used {R}, copy of modquicksort {W}")


def mergesort(A):
    k = 0
    i = 0
    j = 0
    # Base case
    if(len(A) <= 1):
        return
    # Split the list into 2
    x = len(A)//2
    L = A[0:x]
    R = A[x:len(A)]
    # Sort L and R
    mergesort(L)
    mergesort(R)
    # 3 varible loop
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
            k += 1
        else:
            A[k] = R[j]
            j += 1
            k += 1
        if i < len(L) and j == len(R):
             while i < len(L):
                A[k] = L[i]
                i += 1
                k += 1
    if j < len(R) and i == len(L):
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1


def CreateRandomList(size):
    # create a list with A number of integers so 0-9 as the index.
    b = []
    for i in range(size):
        b.append(random.randrange(0, size))
    return b

        
def quicksortr(A, low, high, mod):
    if high - low == 0:
        return
    # modified part
    if mod == True:
        mid = (low + high)//2
        A[low], A[mid] = A[mid], A[low]
    lmgt = low + 1
    
    for i in range(low + 1 , high, 1):
        if A[i] < A[low]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1
    pivot = lmgt - 1
    A[low], A[pivot] = A[pivot], A[low]
    quicksortr(A, low, pivot, False)
    quicksortr(A, pivot + 1, high, False)


def quicksort(A):
    quicksortr(A, 0, len(A), False)


def modquicksort(A):
    quicksortr(A, 0, len(A), True)

main()
