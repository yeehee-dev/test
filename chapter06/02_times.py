def calcaulate_time(num):
    result = []
    i = 0
    while True:
        i = i+1
        list_3 = num*i
        if list_3 < 1000:
            result.append(list_3)
        else:
            break
    return result

list3 = calcaulate_time(3)
list5 = calcaulate_time(5)
list15 = calcaulate_time(15)

result = sum(list3)+sum(list5)-sum(list15)
print(result)