def insertion_sort(array0):
    index_j = 1
    for index_val in array0:
        if array0.index(index_val) == 0:continue

        index_i = index_j - 1#직전항에 있는 값과 비교를 위한 인덱스 설정

        #현재 불려진 값과 다음 값과 비교대상이 유효한 범위일때 동작
        #이전값이 현재값보다 큰경우 반복문이 동작하여 이전항들과의 전체 비교 수행
        while index_i > -1 and array0[index_i] > int(index_val):
            array0[index_i + 1] = array0[index_i]
            index_i = index_i - 1

        index_j = index_j + 1#다음 항의 위치를 가리키기 위한 연산
        array0[index_i+1] = int(index_val)

        print(array0)


insertion_sort([4,5,22,21,3])
