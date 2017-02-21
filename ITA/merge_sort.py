def merge(A, p, q, r):
    n1 = q - p + 1 #왼쪽 배열의 끝인덱스
    n2 = r - q#오른쪽 배열의 끝인덱스

    left_array = []
    right_array = []
    #각 개 배열의 생성
    for left_i in range(0, n1):
        left_array.append(A[p + left_i])
    for right_i in range(0, n2):
        right_array.append(A[q  + 1 + right_i])

    #배열 끝을 비교하기 위한 마지막값 추가
    left_array.append(99999)
    right_array.append(99999)

    print('left : {}'.format(left_array))
    print('right : {}'.format(right_array))

    #좌우 배열의 처음부터 비교를 위한 인덱스 초기화
    left_i = 0
    right_i = 0

    #매개변수 배열의 값을 정렬하는 동작
    for merge_i in range(p, r + 1):
        #좌우 배열의 첫 값들을 비교하여 매개배열에 삽입하는 동작
        #둘의 값을 비교해서 왼쪽이 작거나 같으면 매개배열에 좌배열의 값삽입
        #만약 오른쪽 변수가 작으면 오른쪽 변수의 값을 넣고 오른쪽 키를 상승
        if left_array[left_i] <= right_array[right_i]:
            A[merge_i] = left_array[left_i]
            left_i = left_i + 1
        else:
            A[merge_i] = right_array[right_i]
            right_i = right_i + 1

#merge([333,23,7,8,9,10,1,2,3,4,655,667], 0, 5, 11)

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        print(q)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

    print(A)

merge_sort([2,34,23,23,2,1,2,23,1,1123,123,12412,444],0,12 )
