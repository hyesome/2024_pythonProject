# (0,0) 시작
# 사용자가 UP 입력하면 위로, DOWN 입력하면 아래로, LEFT 입력하면 왼쪽으로, RIGHT 입력하면 오른쪽으로
# MAP의 범위는 (0,0)~(100,100)
# (0,0) 가장 왼쪽의 아래, (100,100) 가장 오른쪽의 위
# 1. 잘못입력하면 처리x
# 2. 맵 밖에 못나가게 처리 (0,0) 에서 아래 누르면 잘못된 방향이라고 알려주고 (0,0) 유지
# EXIT 입력하면 종료

user_input = ""
X = 0
Y = 0

directions = ["UP", "DOWN", "LEFT","RIGHT"]
dx = [0,0,-1,1]
dy = [1, -1, 0,0]
valid_inputs = ["EXIT"]+directions

while user_input != "EXIT":
    user_input = ""  # user_input 초기화
    while user_input not in valid_inputs:
        user_input = input("움직일 방향을 입력하세요 (종료는 EXIT) :: ")

    if user_input in directions:
        index = directions.index(user_input)

        tmpX = X+dx[index]
        if tmpX > 100 or tmpX < 0:
            print("map의 범위를 벗어날 수 없습니다.")
        else:
            X = tmpX

        tmpY = Y+dy[index]
        if tmpY > 100 or tmpY < 0:
            print("map의 범위를 벗어날 수 없습니다.")
        else:
            Y = tmpY

    print("현재 위치 : (",X,",",Y,")" )

print("프로그램을 종료합니다.")