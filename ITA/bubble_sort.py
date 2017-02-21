def bubble_sort(A):
    #배열 자체의 마지막 전까지 비교
    for index_i in range(len(A)-1):
        #배열의 끝인덱스
        for index_j in range(len(A)-1, index_i, -1) :
            if A[index_j] < A[index_j - 1]:
                tmp = A[index_j]
                A[index_j] = A[index_j - 1]
                A[index_j - 1] = tmp
            print(index_j)

    return A

print(bubble_sort([1123,123,123,2,23,23,23,3,1,4,12,1]))


for index_j in range(10,2, -1) :
    print(index_j)
