<<<<<<< HEAD
#Dutch Flag
red, white, blue = range(3)

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    for i in reversed(range(len(A))):
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break
    
=======
#Dutch Flag
red, white, blue = range(3)

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    for i in reversed(range(len(A))):
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break
    
>>>>>>> 2cb9e49e883400a268731c5612315df24d5dccef
    return A