marks = [90,25,67,45,80]
number = 0

for number in range(len(marks)):
    if marks[number] < 60: continue
    print("축하합니다. %d번 학생은 합격입니다." %(number+1))