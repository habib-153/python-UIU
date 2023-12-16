from math import sqrt

def calcMean(array, num_of_elem):
    return sum(array)/ num_of_elem

def calc_Std_deviation(array, num_of_elem):
    mean = calcMean(array, num_of_elem)
    v = sum((x - mean) ** 2 for x in array) / num_of_elem
    std_deviation = sqrt(v)
    return std_deviation

array = list(map(int, input().split()))
num_of_element = len(array)
print(round(calc_Std_deviation(array, num_of_element),2))
