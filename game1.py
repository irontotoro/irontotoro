import random
def g1():
    list1 = ['가위', '바위', '보']
    result = []
    print("5번의 게임을 진행합니다.")
    for x in range(5):
        user = input("가위, 바위, 보 중에서 입력해주세요.")
        cpt = random.choice(list1)
        print("나 :", user)
        print("컴퓨터 :", cpt)
        if user == cpt:
            print("비겼습니다.")
            result.append("D")
        elif user == '가위':
            if cpt == '바위':
                print("졌습니다.")
                result.append("L")
            elif cpt == '보':
                print("이겼습니다.")
                result.append("W")
        elif user == '바위':
            if cpt == '보':
                print("졌습니다.")
                result.append("L")
            elif cpt == '가위':
                print("이겼습니다.")
                result.append("W")
        elif user == '보':
            if cpt == '가위':
                print("졌습니다.")
                result.append("L")
            elif cpt == '바위':
                print("이겼습니다.")
                result.append("W")
    print(result)