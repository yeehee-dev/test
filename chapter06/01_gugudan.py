def gugu(num):
    for i in range(10):
        i = i+1
        print("%d * %d = %d" %(num,i,num*i))
        
def gugu_list(num):
    result = []
    for i in range(10):
        i =  i+1
        result.append(num*i)
    return result

num = int(input("원하는 단을 입력하세요: "))
gugu(num)

print(gugu_list(num))