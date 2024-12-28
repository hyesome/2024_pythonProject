# print("=========range 예제======")
#
# for i in range(10):
#     print(i)

attitudes = [9,9,9,8,9,9,8,9,9,9]

for attitude in attitudes:
    print(attitude)
    attitude = attitude + 1

print("참조하는 attitude 값에 더한것 - attribute: call by value")
print(attitudes)

for i in range(len(attitudes)):
    attitudes[i] = attitudes[i] + 1

print("attitudes의 i번째 index에 더한 값을 넣어준 것 - attribute[i]: call by reference")
print(attitudes)

# 10명이 10문제를 하는 쪽지 시험
# 모두 객관식으로 이루어졌음.
# 모든 배점은 10점씩
# 학생은 0번 학생 ~ 9번 학생
# 문제도 0번 문제 ~ 9번 문제

# import random
#
# students = []
# for i in range(10): # i번째 학생
#     student = []
#     for j in range(10): #j번째 문제
#           student.append(random.randrange(1,6))
#     students.append(student)
#
# print(students)

students = [[1, 2, 5, 5, 1, 2, 4, 4, 5, 4],
            [2, 2, 2, 4, 1, 5, 2, 4, 2, 2],
            [4, 2, 3, 1, 4, 3, 5, 2, 4, 3],
            [5, 2, 2, 2, 2, 1, 3, 4, 2, 4],
            [3, 2, 2, 4, 2, 5, 4, 1, 5, 4],
            [4, 5, 5, 4, 2, 4, 5, 1, 5, 2],
            [3, 3, 3, 3, 2, 5, 1, 1, 3, 4],
            [4, 3, 1, 4, 3, 2, 3, 1, 2, 2],
            [5, 2, 3, 4, 3, 3, 1, 4, 4, 5],
            [5, 3, 5, 5, 2, 4, 1, 5, 4, 3],
            [5, 3, 5, 5, 2, 4, 1, 5, 4, 3]]

answer = [5, 2, 3, 4, 3, 3, 1, 4, 4, 5]

# 1. 각 student의 점수를 구하시오 (scores)
# 2. 두번째 문제에 대해서 3번도 정답 인정했을때의 점수를 구하시오. (score -> scores_final)

score = []
for i in range(len(students)):
    score.append(0)
    for j in range(len(answer)):
        if students[i][j] == answer[j]:
            score[i] = score[i] + 10
print(score)