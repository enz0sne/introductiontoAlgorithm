import math

def radix_sort(array_a, place_d):
    array_result = array_a
    #자릿수별로 비교
    for int_i in range(1, place_d+1):
        array_result = counting_sort_for_radix(array_result, int_i)
        print(array_result)

def counting_sort_for_radix(array_param, place_value):
    array_result = [0 for _ in range(len(array_param))]
    array_place = [0 for _ in range(10)]
    for int_j in range(0,len(array_param)):
        calc_val =int((array_param[int_j] / math.pow(10,place_value-1)) % 10)
        print(calc_val)
        array_place[calc_val] = array_place[calc_val] + 1
    print(array_place)
    for int_j in range(0,10):
        array_place[int_j] = array_place[int_j] + array_place[int_j - 1]
    print(array_place)
    for int_j in range(len(array_param)-1, -1, -1):
        calc_val =int((array_param[int_j] / math.pow(10,place_value-1)) % 10)
        array_result[array_place[calc_val ]-1] = array_param[int_j]
        array_place[calc_val] = array_place[calc_val] - 1
    return array_result



array_test_digit = [231,242,322,312,565,633]
radix_sort(array_test_digit, 3)
