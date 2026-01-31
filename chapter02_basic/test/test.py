# 1. 

korean = 80
eng = 75
math = 55

mean = (korean+eng+math)/3

print(mean)

# 2

def bool_eve(num):
    if num/2 == 0:
        return("even")
    else:
        return("odd")

bool_flag = bool_eve(13)
print(bool_flag)

#3 
pin = "881120-1068234"
pin_list = [8, 8, 1, 1, 2, 0,  1, 0, 6, 8, 2, 3, 4]
yyyymmdd = pin_list[:7]
num = pin_list[7:]
print(yyyymmdd)
print(num)

#4 
if num[0]==2:
    print("woman")
else:
    print("man")


#5
a = "a:b:c:d"
b = a.replace(":","#")
print(b)

#6 
aa = [1,3,5,4,2]
aa.sort()
aa.reverse()
print(aa)

#7 
a_word = ['life', 'is', 'too', 'short']
result = " ".join(a_word)
print(result)

#8 
a_tup = (1,2,3)
print(a_tup)

#10
a_dic = {'A':90, 'B':80, 'C':70}
result = a_dic.pop('B')
print(a_dic)
print(result)

#11
a_list = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a_list)
b = list(aSet)
print(b)

#12 
a = b = [1,2,3]
a[1] = 4
print(b)