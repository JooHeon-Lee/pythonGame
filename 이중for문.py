balls = [1, 2, 3, 4]
weapons = [11, 22, 3, 44]

for ball_idx, ball_val in enumerate(balls):
    print("ball ", ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapons : ", weapon_val)
        if ball_val == weapon_val: # 충돌체크
            print("공과 무기가 충돌")
            break # 해당 for문 탈출
    else: # for문을 순회할게 없으면 들어옴
        continue 
    print("바깥 for문 break")
    break