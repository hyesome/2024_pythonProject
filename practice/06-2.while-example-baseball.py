# 야구게임
#
# 3자리의 랜덤숫자가 정답이고, 그 3개의 숫자는 겹치지 않음
#
# ###   (935)
# 123  -> XX등장 -> 1B
# 765  -> XX맞음 -> 1S
# 903 -> 1S 1B
# 935 -> 이기는 게임

import random

### 숫자 풀이
# result = 0
# result % 10
##  (result // 10) % 10
###  result // 100
#
# while result // 100 == (result // 10) % 10 or result // 100 == result % 10 or (result // 10) % 10 == result % 10:
#     result = random.randrange(1,1000) # 숫자를 쓰는 경우
#     print(result)
#


result = [0,0,0]
while result[0] == result[1] or result[1] == result[2] or result[2] == result[0]:
    result[0] = random.randrange(1,10)
    result[1] = random.randrange(1,10)
    result[2] = random.randrange(1,10)
    #result = str(random.randrange(100,1000))
    print(result)

S = 0

while S !=3:
    #user_input = str("000"+input("정답을 맞춰보세요"))[-3:]
    user_input2 = int(input("정답을 맞춰보세요"))
    user_input = [user_input2 // 100, (user_input2 // 10) % 10, user_input2 % 10]
    print(user_input)

    S = 0
    B = 0

    if result[0] == user_input[0]:
        S = S + 1
    elif result[0] == user_input[1] or result[0] == user_input[2]:
        B = B + 1

    if result[1] == user_input[1]:
        S = S + 1
    elif result[1] == user_input[0] or result[1] == user_input[2]:
        B = B + 1

    if result[2] == user_input[2]:
        S = S + 1
    elif result[2] == user_input[0] or result[2] == user_input[1]:
        B = B + 1

    if S == 3:
        print("정답입니다!")
    else:
        print("S ",S, " B",B)