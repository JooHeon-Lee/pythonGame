# ==== 게임 개발 프레임 ======

############################################################################################
# 기본 초기화 ( 반드시 해야하는 것들)
import pygame

pygame.init() 

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("게임 이름")

# FPS
clock = pygame.time.Clock()
#######################################################################################

# 1. 사용자 게임 초기화 ( 배경화면, 게임이미지, 좌표, 폰트,속도 등 설정)

running = True 

while running:
    dt = clock.tick(30) # 게임 화면의 초당 프레임수 설정


    #2. 이벤트 처리 ( 키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기

    pygame.display.update()

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기 (ms)

# 게임 종료
pygame.quit()