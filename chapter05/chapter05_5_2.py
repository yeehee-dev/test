def two_times(numberlist):
    result = []
    for number in numberlist:
        result.append(number*2)
    return result

def two_times_fun(x): return x*2

result = two_times([1,2,3,4])
print(result)
list(map(two_times_fun,[1,2,3,4]))