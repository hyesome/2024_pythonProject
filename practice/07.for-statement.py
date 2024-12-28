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

