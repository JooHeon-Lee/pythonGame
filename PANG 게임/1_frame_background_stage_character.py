# ==== 게임 개발 프레임 ======

############################################################################################
# 기본 초기화 ( 반드시 해야하는 것들)
import pygame
import os

pygame.init() 

#화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("PANG")

# FPS
clock = pygame.time.Clock()
#######################################################################################

# 1. 사용자 게임 초기화 ( 배경화면, 게임이미지, 좌표, 폰트,속도 등 설정)
current_path = os.path.dirname(__file__) # 현재 파일 위치 반환
image_path = os.path.join(current_path)

#배경
background = pygame.image.load(os.path.join(image_path,"background.png"))

#스테이지
stage =  pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지 높이에대해 공을 튕기기 위함

#캐릭터 생성
character =  pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_heigth = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_heigth - stage_height





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
    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_height - stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update()

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기 (ms)

# 게임 종료
pygame.quit()