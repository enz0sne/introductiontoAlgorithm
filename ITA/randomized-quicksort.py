import random
#퀵소트 함수작성

def randomized_quickSort(A, p, r):
    if  p < r:
        q = randomized_partitions(A, p, r)
        randomized_quickSort(A, p, q - 1)
        randomized_quickSort(A, q, r)
    return

"""넘어온 리스트에 대해서 가장 끝값을 기준값을 전체와 비교 후
좌측에는 자신보다 작거나 같은값을,
우측에는 자신보다 큰값으 배치하고 자신을 그사이에 배치한 뒤, 해당 인덱스를 반환한다."""
def randomized_partitions(A, p, r):
    arr_i = []
    middle_i = ''
    if r - p > 3:
        for key in range(0,3):
            while True:
                tmp_i = random.choice(range(p,r + 1))
                if not arr_i and A[tmp_i] in arr_i:
                    #뽑아낸 인덱스의 실제 값을 정렬
                    """"for  inner_key, inner_val in arr_i.items():
                        if inner_val <= A[tmp_i]:
                            inner_tmp = arr_i[inner_key]
                            arr_i[inner_key] = arr_i[key]
                            arr_i[key] = inner_tmp                        """
                    arr_i.append(tmp_i)
                    break
    #to-do 중간값 고르기
    print(arr_i)
    tmp = A[r]
    A[r] = A[i]
    A[i] = tmp
    return partitions(A, p, r)

def partitions(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            tmp  = A[i]
            A[i] = A[j]
            A[j] = tmp
        print('시작 : {}, 끝 : {}, 배열 : {}'.format(p, r, A))
    tmp      = A[i + 1]
    A[i + 1] = A[r]
    A[r] = tmp
    print('반환 : {}'.format(i + 1))
    return i + 1


A = [2, 8, 7, 1, 3, 5, 6, 4]
randomized_quickSort(A, 0, 7)

for i in range(0,len(A)):
    print(i)
