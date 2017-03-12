import random
"""
array_a : 정렬할 배열
array_b : 정렬된 결고를 담을 배열
max_k : 배열에 담긴 값들의 가장 큰값
"""
def counting_sort(array_a, array_b, max_k):
    array_c = [0 for _ in range(0, max_k)]
    #array_c는 각 인덱스에 array_a가 담은 값이 몇개가 존재하는지 표기하는 용도
    for int_i in range(0, len(array_a)):
        array_c[array_a[int_i]] = array_c[array_a[int_i]] + 1
    #print('C배열 개수{} 요소{}'.format(len(array_c), array_c))
    #임시배열에 자신보다 작은 수들의 개수를 입력
    for int_i in range(1,max_k):
        array_c[int_i] = array_c[int_i] + array_c[int_i - 1]
    print('C배열 개수{} 요소{}'.format(len(array_c), array_c))
    #임시배열의 가장 큰 인덱스부터 진행
    #동일한 값이 있는 경우 해당 값을 확인된 개수만큼 array_b에 채우고
    #array_c에 있는 값은 array_b에 입력된 수만큼 제거하면 진행
    for int_j in range(len(array_a)-1, -1, -1) :
    #    print('{} {} {}'.format(int_j, array_a[int_j], array_c[array_a[int_j]]))
        array_b[array_c[array_a[int_j]]-1] = array_a[int_j]
        array_c[array_a[int_j]] = array_c[array_a[int_j]] - 1


    print('결과 A배열 개수{} 요소{}'.format(len(array_test_a), array_test_a))
    print('B배열 요소 {}'.format( array_b))

array_test_a = [random.choice(range(0,20)) for _ in range(0,20)]
array_test_b = [0 for _ in range(0,20)]
print('A배열 개수{} 요소{}'.format(len(array_test_a), array_test_a))
print('B배열 개수{} 요소{}'.format(len(array_test_b), array_test_b))
counting_sort(array_test_a, array_test_b, 20)
