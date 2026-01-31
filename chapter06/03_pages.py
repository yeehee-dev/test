def getTotalPage(m,n):
    total = 0
    if m%n == 0:
        total = int(m/n)
    else: 
        total = int(m/n) + 1
    return total




m = int(input("게시물의 총 건수를 입력하세요: "))
n = int(input("한 페이지에 보여 줄 게시물의 수를 입력하세요: "))

print(getTotalPage(m,n))